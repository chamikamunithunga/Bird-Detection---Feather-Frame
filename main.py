import tensorflow as tf
import numpy as np
from PIL import Image
import os

# Load EfficientNetB3 pretrained on ImageNet (better accuracy)
model = tf.keras.applications.EfficientNetB3(weights='imagenet')

# Use ImageNet class decoder
decode_predictions = tf.keras.applications.imagenet_utils.decode_predictions

# Define common bird-related class keywords
BIRD_KEYWORDS = [
    "bird", "parrot", "hen", "cock", "duck", "goose", "flamingo", "ostrich",
    "eagle", "woodpecker", "peacock", "pigeon", "seagull", "quail",
    "swan", "kite", "kingfisher", "hawk", "falcon", "vulture", "rooster", "canary"
]

def is_bird_present(predictions, top_k=5):
    """
    Check if any of the top_k predictions relate to birds.
    """
    for _, class_name, confidence in predictions[:top_k]:
        class_name_lower = class_name.lower()
        if any(keyword in class_name_lower for keyword in BIRD_KEYWORDS):
            return True, class_name, confidence
    return False, predictions[0][1], predictions[0][2]

def classify_image(image_path):
    # Load and preprocess image
    image = Image.open(image_path).convert('RGB').resize((300, 300))
    img_array = np.array(image).astype('float32')
    input_tensor = np.expand_dims(img_array, axis=0)
    input_tensor = tf.keras.applications.efficientnet.preprocess_input(input_tensor)

    # Predict
    predictions = model.predict(input_tensor)
    decoded_preds = decode_predictions(predictions, top=5)[0]

    # Output results
    print("Top 5 predictions:")
    for _, name, score in decoded_preds:
        print(f"{name}: {score:.3f}")

    # Check if bird is detected
    is_bird, class_name, confidence = is_bird_present(decoded_preds)
    print("\nPrediction:", class_name)
    print(f"Confidence: {confidence:.2f}")
    print("✅ Bird detected!" if is_bird else "❌ No bird detected.")

# ==== Replace this with your actual image path ====
image_path = "/Users/chamikamunithunga/Desktop/bird detection /birdenv/imgs/1.jpeg"  # relative to your script location
if os.path.exists(image_path):
    classify_image(image_path)
else:
    print(f"Image not found at {image_path}")
