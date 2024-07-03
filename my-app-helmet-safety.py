from ultralytics import YOLOv10

MODEL_PATH = 'yolov10n.pt'
model = YOLOv10(MODEL_PATH)

YAML_PATH = '../safety_helmet_dataset/data.yaml'
EPOCHS = 50
IMG_SIZE = 640
BATCH_SIZE = 128

model.train(data=YAML_PATH,
            epochs=EPOCHS,
            batch=BATCH_SIZE,
            imgsz=IMG_SIZE)

TRAINED_MODEL_PATH = 'runs/detect/train5/weights/best.pt'
trained_model = YOLOv10(TRAINED_MODEL_PATH)

trained_model.val(data=YAML_PATH,
                  imgsz=IMG_SIZE,
                  split='test')
