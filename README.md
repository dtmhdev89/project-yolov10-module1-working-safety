
# Using Python version:
3.9

* For Mac M1:
brew install python@3.9

* Create venv using virtualenv in project folder:
python3.9 -m venv ./venv

source venv/bin/activate

# At the root folder of project, clone YoloV10:
git clone git@github.com:THU-MIG/yolov10.git

# Change directory into YoloV10 folder, and install requirements:
pip install -q -r requirements.txt

or

python3.9 -m pip install -q -r requirements.txt

# For Mac M1: onnxruntime installation
python3 -m pip install onnxruntime

# Copy following files into yolov10 folder to run:
my-app.py
my-app-helmet-safety.py

# Create results folders in yolov10 folder to save the prediction:
mkdir -p images
mkdir -p video_images

# First result for video:
    results = model(source=..., stream=True)  # generator of Results objects
    for r in results:
        boxes = r.boxes  # Boxes object for bbox outputs
        masks = r.masks  # Masks object for segment masks outputs
        probs = r.probs  # Class probabilities for classification outputs

0: 384x640 5 persons, 1 car, 1 motorcycle, 1 bus, 93.3ms
0: 384x640 3 persons, 1 car, 2 motorcycles, 71.0ms
0: 384x640 3 persons, 2 cars, 88.8ms
0: 384x640 3 persons, 3 cars, 2 motorcycles, 1 backpack, 64.2ms
0: 384x640 5 persons, 2 cars, 2 motorcycles, 1 bus, 1 backpack, 72.5ms
0: 384x640 7 persons, 9 motorcycles, 2 buss, 1 backpack, 83.5ms
0: 384x640 7 persons, 2 cars, 3 motorcycles, 1 bus, 73.4ms
0: 384x640 6 persons, 6 motorcycles, 2 buss, 73.7ms
0: 384x640 4 persons, 1 car, 3 motorcycles, 1 bus, 69.7ms
0: 384x640 4 persons, 2 cars, 3 motorcycles, 1 bus, 73.6ms
0: 384x640 1 person, 2 motorcycles, 1 bus, 81.4ms
0: 384x640 4 persons, 5 motorcycles, 1 bus, 1 truck, 67.3ms
0: 384x640 6 persons, 5 motorcycles, 1 bus, 66.0ms
0: 384x640 7 persons, 2 cars, 1 motorcycle, 71.8ms
0: 384x640 3 persons, 1 car, 3 motorcycles, 2 buss, 66.6ms
0: 384x640 2 persons, 1 car, 3 motorcycles, 1 bus, 73.7ms
0: 384x640 4 persons, 1 car, 3 motorcycles, 1 bus, 2 trucks, 77.4ms
Speed: 0.9ms preprocess, 74.6ms inference, 1.1ms postprocess per image at shape (1, 3, 384, 640)


# Second result for video:
Example:
    results = model(source=..., stream=True)  # generator of Results objects
    for r in results:
        boxes = r.boxes  # Boxes object for bbox outputs
        masks = r.masks  # Masks object for segment masks outputs
        probs = r.probs  # Class probabilities for classification outputs

0: 384x640 5 persons, 1 car, 1 motorcycle, 1 bus, 124.5ms
0: 384x640 3 persons, 2 motorcycles, 1 backpack, 85.3ms
0: 384x640 1 person, 4 cars, 3 motorcycles, 1 backpack, 86.1ms
0: 384x640 8 persons, 1 car, 2 motorcycles, 2 buss, 1 backpack, 96.1ms
0: 384x640 6 persons, 2 motorcycles, 3 buss, 1 backpack, 84.8ms
0: 384x640 6 persons, 1 car, 2 motorcycles, 83.5ms
0: 384x640 7 persons, 1 car, 4 motorcycles, 1 bus, 93.3ms
0: 384x640 4 persons, 1 car, 4 motorcycles, 1 bus, 1 truck, 81.8ms
0: 384x640 6 persons, 1 car, 2 motorcycles, 86.7ms
0: 384x640 5 persons, 1 car, 3 motorcycles, 80.8ms
0: 384x640 4 persons, 1 car, 3 motorcycles, 1 bus, 2 trucks, 69.8ms
Speed: 1.2ms preprocess, 88.4ms inference, 1.4ms postprocess per image at shape (1, 3, 384, 640)

# Validation results:
val: Scanning project-yolov10-module1-working-safety/safety_helmet_dataset/test/label
val: New cache created: project-yolov10-module1-working-safety/safety_helmet_dataset/test/labels.cache
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 7/7 [00:21<00:00,  3.
                   all        109        320      0.729      0.769      0.775      0.418
                  head        109         16      0.661       0.75      0.657      0.318
                helmet        109        162      0.779      0.848      0.889      0.475
                person        109        142      0.748       0.71       0.78      0.462
Speed: 1.0ms preprocess, 192.2ms inference, 0.0ms loss, 0.2ms postprocess per image
