import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk, ImageOps
import monitor_size as mns
from drag import Drag
import cv2
import time


class Motion(tk.Frame):
    def __init__(self, filepath='', master=None):
        super().__init__(master)
        self.pack()

        def onKeyPressed(event):
            if event.keycode == 27:
                self.master.destroy()

        width = mns.getWidth()
        height = mns.getHeight()

        self.master.overrideredirect(True)
        self.master.geometry(str(width) + 'x' + str(height))
        self.master.attributes("-topmost", True)

        self.master.bind("<Key>", onKeyPressed)

        # Canvasの作成
        self.canvas = tk.Canvas(self.master, bg="#003300", width=str(
            width * 3), height=(height * 3))
        # Canvasを配置
        self.canvas.place(x=-width, y=-height)

        # Canvasのドラッグ設定
        drag = Drag(False, (0, 0), self.master)
        self.canvas.bind("<Button>", drag.mouseDown)
        self.canvas.bind("<ButtonRelease>", drag.mouseRelease)
        self.canvas.bind("<Motion>", drag.mouseMove)

        # 背景色の制定
        self.master.attributes('-transparentcolor', self.canvas['bg'])

        # 動画ファイルを読み込む
        self.capture = cv2.VideoCapture(filepath)

        print(self.capture.isOpened())

        self.disp_id = None

        if self.disp_id is None:
            # 動画を表示
            self.disp_image_loop()
        else:
            # 動画を停止
            self.after_cancel(self.disp_id)
            self.disp_id = None

    def canvas_keypress(self, event):
        '''キーを押したとき'''

        if self.disp_id is None:
            # 動画を表示
            self.disp_image_loop()
        else:
            # 動画を停止
            self.after_cancel(self.disp_id)
            self.disp_id = None

    def disp_image_loop(self):
        '''画像をCanvasに表示し、無限ループ'''

        # フレーム画像の取得
        ret, frame = self.capture.read()

        if ret:
            # BGR→RGB変換
            cv_image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            # NumPyのndarrayからPillowのImageへ変換
            pil_image = Image.fromarray(cv_image)

            # キャンバスのサイズを取得
            canvas_width = self.canvas.winfo_width()
            canvas_height = self.canvas.winfo_height()

            # 画像のアスペクト比（縦横比）を崩さずに指定したサイズ（キャンバスのサイズ）全体に画像をリサイズする
            pil_image = ImageOps.pad(pil_image, (300, 300))

            # PIL.ImageからPhotoImageへ変換する
            self.photo_image = ImageTk.PhotoImage(image=pil_image)

            # 画像の描画
            self.canvas.create_image(
                canvas_width / 2,       # 画像表示位置(Canvasの中心)
                canvas_height / 2,
                image=self.photo_image  # 表示画像データ
            )
        else :
            self.capture.set(cv2.CAP_PROP_POS_FRAMES, 0)

        # disp_image()を10msec後に実行する
        self.disp_id = self.after(60, self.disp_image_loop)
        
    def disp_image(self):
        '''画像をCanvasに表示する'''

        # フレーム画像の取得
        ret, frame = self.capture.read()
    
        # BGR→RGB変換
        cv_image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        # NumPyのndarrayからPillowのImageへ変換
        pil_image = Image.fromarray(cv_image)

        # キャンバスのサイズを取得
        canvas_width = self.canvas.winfo_width()
        canvas_height = self.canvas.winfo_height()

        # 画像のアスペクト比（縦横比）を崩さずに指定したサイズ（キャンバスのサイズ）全体に画像をリサイズする
        pil_image = ImageOps.pad(pil_image, (300, 300))

        # PIL.ImageからPhotoImageへ変換する
        self.photo_image = ImageTk.PhotoImage(image=pil_image)

        # 画像の描画
        self.canvas.create_image(
                canvas_width / 2,       # 画像表示位置(Canvasの中心)
                canvas_height / 2,                   
                image=self.photo_image  # 表示画像データ
                )

        # disp_image()を10msec後に実行する
        self.disp_id = self.after(10, self.disp_image)
