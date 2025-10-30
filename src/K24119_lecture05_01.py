# src/K24119_lecture05_01.py
import sys
import os
import cv2
import numpy as np

# 親ディレクトリをモジュール検索パスに追加
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from my_module.K24119.lecture05_camera_image_capture import MyVideoCapture  # 学籍番号フォルダ

def K24119_lecture05_01():
    # 1. カメラ画像取得
    app = MyVideoCapture()
    print("カメラを起動します。画面が出たら 'q' キーを押して撮影してください")
    app.run()
    capture_img = app.get_img()
    if capture_img is None:
        print("カメラ画像が取得できません")
        return

    # 2. Google画像読み込み
    google_img = cv2.imread(os.path.join(os.path.dirname(__file__), '../images/google.png'))
    if google_img is None:
        print("Google画像が読み込めません")
        return

    g_height, g_width, _ = google_img.shape
    c_height, c_width, _ = capture_img.shape
    print(f"Google画像サイズ: {g_width}x{g_height}")
    print(f"カメラ画像サイズ: {c_width}x{c_height}")

    # 3. 白色部分をカメラ画像で置換
    for y in range(g_height):
        for x in range(g_width):
            b, g, r = google_img[y, x]
            if (b, g, r) == (255, 255, 255):
                # グリッド状に繰り返して置換
                google_img[y, x] = capture_img[y % c_height, x % c_width]

    # 4. 加工後画像の保存
    
    output_filename = os.path.join(os.path.dirname(__file__), '../output_images/lecture05_01_K24119.png')
    cv2.imwrite(output_filename, google_img)
    print(f"画像を保存しました: {output_filename}")

if __name__ == '__main__':
    K24119_lecture05_01()