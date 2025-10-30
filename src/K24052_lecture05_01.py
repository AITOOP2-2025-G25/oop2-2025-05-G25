import numpy as np
import cv2
# 別のファイル（K24052_lecture05_camera_image_capture.py）から MyVideoCapture クラスを読み込む
from my_module.K24052.K24052_lecture05_camera_image_capture import MyVideoCapture
import os # フォルダ作成のために追加

def lecture05_01():

    # カメラキャプチャ実行
    app = MyVideoCapture()
    app.run()

    # 画像をローカル変数に保存
    google_img : cv2.Mat = cv2.imread('images/google.png') # 元のGoogle画像を読み込み
    
    # appオブジェクトからキャプチャした画像（BGR形式）を取得
    # MyVideoCaptureクラスにより、これは 640x480 のはず
    capture_img : cv2.Mat | None = app.get_img()

    # --- 安全のためのチェック ---
    if google_img is None:
        print("エラー: 'images/google.png' が読み込めませんでした。")
        return
    if capture_img is None:
        print("エラー: 画像がキャプチャされませんでした。'q'キーで終了しましたか？")
        return
    # --------------------------

    # ★修正点 1: キャプチャ画像の高、幅、チャンネル数を取得 (640x480)
    c_hight, c_width, _ = capture_img.shape
    
    # ★修正点 2: Googleロゴ画像をキャプチャ画像と同じサイズ (640x480) にリサイズ
    #google_img = cv2.resize(google_img_orig, (c_width, c_hight))

    print(google_img.shape) # リサイズ後のGoogleロゴサイズ
    print(capture_img.shape) # キャプチャ画像サイズ

    # 1ピクセルずつループ処理 (x=幅, y=高さ)
    # ★修正点 3: ループ範囲をキャプチャ画像の幅と高さ (c_width, c_hight) に変更
    for x in range(c_width):
        for y in range(c_hight):
            # リサイズ後のgoogle_imgのピクセルを取得
            b, g, r = google_img[y, x]
            
            # もし白色(255,255,255)だったら置き換える
            if (b, g, r) == (255, 255, 255):
                # ★修正点 4: (リサイズしていない) 元のキャプチャ画像のピクセルで上書き
                google_img[y, x] = capture_img[y, x]

    # 書き込み処理
    
    # 1. 保存先フォルダを指定
    output_dir = 'output_images'
    # 2. フォルダが存在しない場合に自動で作成 (exist_ok=True)
    os.makedirs(output_dir, exist_ok=True) 
    
    # 3. 保存ファイルパスを結合
    output_filepath = os.path.join(output_dir, 'lecture05_01_K24052.png')

    # 4. 合成後の画像 (google_img) を指定したパスに書き込む
    cv2.imwrite(output_filepath, google_img)
    print(f"画像を {output_filepath} に保存しました。")

# このスクリプトが直接実行されたときだけ lecture05_01() を呼び出す
if __name__ == "__main__":
    lecture05_01()

