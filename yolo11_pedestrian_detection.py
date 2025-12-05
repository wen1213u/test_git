import cv2
from ultralytics import YOLO
import os


def main():
    # 載入 YOLO11 模型
    model_path = "model/yolo11n.pt"

    if not os.path.exists(model_path):
        print(f"錯誤: 找不到模型文件 {model_path}")
        return

    print("正在載入 YOLO11 模型...")
    model = YOLO(model_path)
    print("模型載入完成")

    # 開啟預設相機
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("無法開啟相機")
        return

    print("YOLO11 行人辨識啟動中...")
    print("按 'q' 鍵退出")
    print("按 's' 鍵保存當前畫面")

    # 建立儲存資料夾
    save_dir = "detections"
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)

    save_count = 0

    while True:
        ret, frame = cap.read()

        if not ret:
            print("無法讀取畫面")
            break

        # 使用 YOLO 進行偵測
        # class 0 是 'person'（行人）
        results = model(frame, classes=[0], verbose=False)

        # 在畫面上繪製偵測結果
        annotated_frame = results[0].plot()

        # 計算偵測到的行人數量
        num_persons = len(results[0].boxes)

        # 在畫面上顯示行人數量
        cv2.putText(
            annotated_frame,
            f"Pedestrians: {num_persons}",
            (10, 30),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0, 255, 0),
            2
        )

        # 顯示畫面
        cv2.imshow("YOLO11 Pedestrian Detection", annotated_frame)

        key = cv2.waitKey(1) & 0xFF

        # 按 's' 鍵保存當前畫面
        if key == ord('s'):
            from datetime import datetime
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = os.path.join(save_dir, f"detection_{timestamp}.jpg")
            cv2.imwrite(filename, annotated_frame)
            save_count += 1
            print(f"已儲存: {filename} (共 {save_count} 張)")

        # 按 'q' 鍵退出
        elif key == ord('q'):
            break

    # 釋放資源
    cap.release()
    cv2.destroyAllWindows()
    print(f"程式結束，共保存 {save_count} 張偵測畫面")


if __name__ == "__main__":
    main()
