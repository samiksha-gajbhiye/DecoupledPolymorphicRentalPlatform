from ultralytics import YOLO

model = YOLO("models/yolo/weights/yolo11n.pt")

results = model("test_images/chair.jpg")

for result in results:

    for box in result.boxes:

        print(
            result.names[int(box.cls)],
            float(box.conf),
        )