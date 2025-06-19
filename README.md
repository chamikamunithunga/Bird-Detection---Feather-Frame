# 🐦 BirdScanAI

BirdScanAI is a powerful AI-powered bird detection system that uses the YOLOv8 deep learning model to identify birds in images. Built with a Flask backend, this project serves as an intelligent and lightweight API that returns detection results in real time.

--- 
<img width="1440" alt="Screenshot 2025-06-19 at 3 09 17 PM" src="https://github.com/user-attachments/assets/2ebab40b-1837-4022-9720-aed04188c862" />

<img width="1435" alt="Screenshot 2025-06-19 at 3 20 59 PM" src="https://github.com/user-attachments/assets/03d44e6b-1a43-42e1-bab2-3e4c2f147e44" />

In the BirdScanAI system, the YOLOv8 (You Only Look Once, version 8) model is used for detecting birds in images. While it is one of the most powerful real-time object detection models, its performance depends significantly on the type and quality of input data.

✅ 1. YOLOv8 is Trained on Real-World Datasets
YOLOv8, like its predecessors, is primarily trained on natural image datasets such as:

COCO (Common Objects in Context)

ImageNet

Open Images

These datasets consist of real-world photographs, meaning the model has learned to identify patterns, textures, shadows, and environmental cues that naturally occur in photographed birds, not artificially created ones.


Animated or Artificial Images Lack Real-World Features
Animated or artificially rendered images — such as:

Cartoon birds

Vector illustrations

CGI-generated birds

— often lack the pixel-level realism such as:

Natural lighting and shadow variations

Complex feather textures

Realistic color gradations

Occlusions and background noise

Since these characteristics were not present in the model's training data, YOLOv8 struggles to generalize to such inputs, resulting in low confidence scores or complete misdetection.

<img width="1439" alt="Screenshot 2025-06-19 at 3 22 58 PM" src="https://github.com/user-attachments/assets/c3a76c4a-8c9e-43c2-aa4f-10cc755aee57" />


<img width="1439" alt="Screenshot 2025-06-19 at 3 24 33 PM" src="https://github.com/user-attachments/assets/f5489ef8-127d-4959-8a39-4e83ec000422" />



## 🚀 Features

- 🔍 Real-time bird detection using Ultralytics YOLOv8
- 🖼️ Image upload and processing via REST API
- 🌐 CORS-enabled Flask backend for frontend integration
- 🧠 Supports `.pt` custom or pre-trained YOLOv8 models
- 🧪 Easily extendable for more species or multi-object detection





---

## 🧠 Model Details
Model: YOLOv8n (Ultralytics)

Type: Object detection

Classes: Bird (default YOLO classes or custom-trained)

