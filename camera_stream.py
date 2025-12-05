import cv2


def main():
    # 開啟預設相機 (0 是預設相機編號)
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("無法開啟相機")
        return

    print("相機串流啟動中... 按 'q' 鍵退出")

    while True:
        # 讀取一幀畫面
        ret, frame = cap.read()

        if not ret:
            print("無法讀取畫面")
            break

        # 顯示畫面
        cv2.imshow("Camera Stream", frame)

        # 按 'q' 鍵退出
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # 釋放資源
    cap.release()
    cv2.destroyAllWindows()
    print("相機串流已關閉")


if __name__ == "__main__":
    main()
