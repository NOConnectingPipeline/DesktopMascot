import tkinter as tk
from PIL import Image, ImageTk, ImageOps
import cv2
from canvas import Canvas
from capture import Capture

class dispImage(Capture) :
    def __init__(self, master, filepath, disp_id):
        super().__init__(master, filepath)
        self.canvas = Canvas(self.master).draw_canvas()
        self.disp_id = disp_id

    def disp_loop(self) :
        '''画像をCanvasに表示し、無限ループ'''

        capture = self.new_capture()
        # フレーム画像の取得
        ret, frame = capture.read()

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
            photo_image = ImageTk.PhotoImage(image=pil_image)

            # 画像の描画
            self.canvas.create_image(
                canvas_width / 2,       # 画像表示位置(Canvasの中心)
                canvas_height / 2,
                image=photo_image  # 表示画像データ
            )

            #print('disp_loop')
        else :
            capture.set(cv2.CAP_PROP_POS_FRAMES, 0)
        