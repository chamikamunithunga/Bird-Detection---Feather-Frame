from ultralytics import YOLO
from PIL import Image
import cv2
import numpy as np
import os

# Load pretrained YOLOv8 model (best for object detection)
model = YOLO("yolov8n.pt")  # lightweight and fast; you can also use 'yolov8m.pt' for better accuracy

# List of class names YOLOv8 can detect
bird_class_id = 14  # COCO class ID for "bird"

def detect_bird_in_image(image_path):
    if not os.path.exists(image_path):
        print("❌ Image path does not exist.")
        return


    results = model(image_path)[0]


    for box in results.boxes:
        cls = int(box.cls.item())
        if cls == bird_class_id:
            print("✅ YES – Bird detected in image.")
            return

    print("❌ NO – No bird detected in image.")


detect_bird_in_image("/Users/chamikamunithunga/Desktop/bird detection /birdenv/imgs/10.jpg")
