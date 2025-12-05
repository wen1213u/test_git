import cv2
import os
from datetime import datetime


def main():
    # 開啟預設相機
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("無法開啟相機")
        return

    # 建立照片儲存資料夾
    save_dir = "photos"
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)

    print("相機拍照程式啟動")
    print("按 'c' 鍵拍照")
    print("按 'q' 鍵退出")

    photo_count = 0

    while True:
        ret, frame = cap.read()

        if not ret:
            print("無法讀取畫面")
            break

        # 顯示畫面
        cv2.imshow("Camera - Press 'c' to capture", frame)

        key = cv2.waitKey(1) & 0xFF

        # 按 'c' 鍵拍照
        if key == ord('c'):
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = os.path.join(save_dir, f"photo_{timestamp}.jpg")
            cv2.imwrite(filename, frame)
            photo_count += 1
            print(f"已儲存: {filename} (共 {photo_count} 張)")

        # 按 'q' 鍵退出
        elif key == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
    print(f"程式結束，共拍攝 {photo_count} 張照片")


if __name__ == "__main__":
    main()
