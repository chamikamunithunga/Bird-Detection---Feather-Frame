# 🐦 BirdScanAI

BirdScanAI is a powerful AI-powered bird detection system that uses the YOLOv8 deep learning model to identify birds in images. Built with a Flask backend, this project serves as an intelligent and lightweight API that returns detection results in real time.

--- 
<img width="1440" alt="Screenshot 2025-06-19 at 3 09 17 PM" src="https://github.com/user-attachments/assets/2ebab40b-1837-4022-9720-aed04188c862" />

<img width="1435" alt="Screenshot 2025-06-19 at 3 20 59 PM" src="https://github.com/user-attachments/assets/03d44e6b-1a43-42e1-bab2-3e4c2f147e44" />

In the BirdScanAI system, the YOLOv8 (You Only Look Once, version 8) model is used for detecting birds in images. While it is one of the most powerful real-time object detection models, its performance depends significantly on the type and quality of input data.



🧠 Model Input Requirements: Real vs. Animated Images
The BirdScanAI system utilizes the YOLOv8 (You Only Look Once) deep learning model to detect birds in user-submitted images. While the model is highly effective with real-world photographs, it is not optimized for animated or artificially rendered images (e.g., cartoons, vector graphics, or CGI birds). Below is a technical explanation of this limitation:

✅ Why YOLOv8 Excels with Real Images
Training Domain: YOLOv8 is trained on large-scale datasets such as COCO and ImageNet, which consist of photographic images taken in natural environments.

Feature Learning: The model learns complex visual features like feather textures, natural lighting, background noise, and shape variations from real-world images.

High Confidence Detection: When tested on real images, the model can confidently localize and classify birds with high accuracy.

❌ Why Animated Images Perform Poorly
Lack of Realistic Features: Animated images lack essential real-world cues such as shadow gradients, depth, and texture details that the model expects.

Domain Gap: This is a classic domain shift problem, where the testing data (animated birds) differs significantly from the training data (real birds). As a result, the model fails to generalize, often producing low confidence scores or false negatives.

🔬 Theoretical Insight: Domain Shift
Deep learning models are highly dependent on the visual distribution of the data they were trained on. If the input distribution changes significantly (from realistic to synthetic), model performance degrades due to what is known as domain gap.

💡 Best Practice
To ensure optimal detection results:

✅ Use realistic, high-quality bird photographs taken with cameras or phones.

❌ Avoid using cartoons, illustrations, or heavily edited images unless the model is fine-tuned for such inputs.

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

