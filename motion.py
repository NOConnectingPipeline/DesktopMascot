import sys
import tkinter as tk
import monitor_size as mns
from canvas import Canvas
from capture import Capture
from PIL import Image, ImageTk, ImageOps
import cv2
import json

class Motion(tk.Frame):
    def __init__(self, filepath='', master=None):
        super().__init__(master)
        self.pack()

        def onKeyPressed(event):
            json_open = open('animation_resource.json', 'r')
            animation_resource = json.load(json_open)
            if event.keycode == 27:#Escキーを押すと終了
                self.master.destroy()
            for i in animation_resource['animation'] :
                if event.keycode == i['keycode'] :
                    self.after_cancel(self.disp_id)
                    self.capture.release()
                    self.disp_id = None
                    self.capture = Capture(self.master, i['path']).new_capture()
                    self.disp_image()

        width = mns.getWidth()
        height = mns.getHeight()

        self.master.overrideredirect(True)
        self.master.geometry(str(width) + 'x' + str(height))
        self.master.attributes("-topmost", True)

        self.master.bind("<Key>", onKeyPressed)

        self.canvas = Canvas(self.master).draw_canvas()
        self.capture = Capture(self.master, filepath).new_capture()

        # 背景色の制定
        self.master.attributes('-transparentcolor', self.canvas['bg'])

        self.disp_id = None
        if self.disp_id is None :
            print(sys.getrecursionlimit())
            self.count = 0
            self.disp_image_loop()

    def disp_image_loop(self):
        '''画像をCanvasに表示し、無限ループ'''

        # フレーム画像の取得
        ret, frame = self.capture.read()

        if ret:
            print(self.count)
            self.count += 1
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
        self.disp_id = self.after(10, self.disp_image_loop)
        
    def disp_image(self):
        '''画像をCanvasに表示する'''

        # フレーム画像の取得
        ret, frame = self.capture.read()
    
        if ret:
            print(self.count)
            self.count += 1
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
            self.after_cancel(self.disp_id)
        # disp_image()を10msec後に実行する
        self.disp_id = self.after(10, self.disp_image)