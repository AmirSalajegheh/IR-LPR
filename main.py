import cv2
from ultralytics import YOLO

# بارگذاری مدل آموزش دیده
model = YOLO("best (2).pt")

# باز کردن وبکم (0 = default webcam)
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("❌ وبکم باز نشد!")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # پیش‌بینی YOLOv9 روی فریم
    results = model.predict(frame, conf=0.25, save=False)

    # گرفتن خروجی دتکشن‌ها
    for r in results:
        boxes = r.boxes.xyxy.cpu().numpy()  # [x1, y1, x2, y2]
        scores = r.boxes.conf.cpu().numpy()
        classes = r.boxes.cls.cpu().numpy()

        for box, score, cls in zip(boxes, scores, classes):
            x1, y1, x2, y2 = map(int, box)
            label = f"plate {score:.2f}"
            # رسم مستطیل
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
            # نوشتن متن
            cv2.putText(frame, label, (x1, y1-10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)

    # نمایش فریم
    cv2.imshow("YOLOv9 Plate Detection", frame)

    # خروج با زدن 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
