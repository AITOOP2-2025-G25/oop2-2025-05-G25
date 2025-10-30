import os
import numpy as np
import cv2
from my_module.K24046.lecture05_camera_image_capture import MyVideoCapture

def lecture05_01():

    # カメラキャプチャ実行
    app = MyVideoCapture()
    app.run()

    # 画像をローカル変数に保存
    # このファイルの絶対パスを取得して、imagesフォルダを指定
    base_dir = os.path.dirname(os.path.abspath(__file__))
    img_path = os.path.join(base_dir, "../images/google.png")
    output_path = os.path.join(base_dir, "../output_images/lecture05_01_K24046.png")

    # google画像を読み込み
    google_img = cv2.imread(img_path)

    # ここでget_img関数を呼び出す（保存せずに取得）
    capture_img = app.get_img()

    # google_img : cv2.Mat = cv2.imread('images/google.png')
    # capture_img : cv2.Mat = cv2.imread('images/camera_capture.png') # 動作テスト用なので提出時にこの行を消すこと
    # capture_img : cv2.Mat = "implement me"

    g_height, g_width, g_channel = google_img.shape
    c_height, c_width, c_channel = capture_img.shape
    print(google_img.shape)
    print(capture_img.shape)

    for x in range(g_width):
        for y in range(g_height):
            g, b, r = google_img[y, x]
            # もし白色(255,255,255)だったら置き換える
            if (b, g, r) == (255, 255, 255):
                google_img[y, x] = capture_img[y % c_height, x % c_width]
                pass
                #implement me

    # 書き込み処理
    os.makedirs(os.path.join(base_dir, "../output_images"), exist_ok=True)
    cv2.imwrite(output_path, google_img)
    print(f"✅ 出力完了: {output_path}")
    # implement me

