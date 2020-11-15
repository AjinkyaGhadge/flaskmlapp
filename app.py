import io
import json
from PIL import Image
from flask import Flask, jsonify, request
from torchvision import models
import torchvision.transforms as transforms
import os


app = Flask(__name__)
imagenet_class_index = json.load(open('imagenet_class_index.json'))
model = models.densenet121(pretrained=True)
model.eval()
port = int(os.environ.get("PORT", 5000))


def predict_image(input):
    input_transformed = transforms.Compose([transforms.Resize(255),transforms.CenterCrop(224),transforms.ToTensor(),transforms.Normalize([0.485, 0.456, 0.406],[0.229, 0.224, 0.225])])
    image = Image.open(io.BytesIO(input))
    t = input_transformed(image).unsqueeze(0)
    results = model.forward(t)
    _, label = results.max(1)
    res_idx = str(label.item())
    return imagenet_class_index[res_idx]


@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        file = request.files['file']
        input_file = file.read()
        _, class_name = predict_image(input=input_file)
        return jsonify({'class_name': class_name})


if __name__ == '__main__':
    app.run(host='0.0.0.0',port = port,debug=True)
