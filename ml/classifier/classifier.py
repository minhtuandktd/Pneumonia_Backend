import os
import torch
import numpy as np
import cv2

absolute_path = os.path.dirname(__file__)
device = torch.device("cpu")

class Classifier:
    def __init__(self):
        self.model = torch.load(os.path.join(absolute_path, "weights/Pneumonia_transfered_on_EfficentB0.pt"), map_location=torch.device('cpu'))
        self.model = self.model.to(device)
        self.model.eval()

    def preprocessing(self, img):
        img = cv2.resize(img, (224, 224))
        if img.shape[2] == 1:
            img = np.dstack([img, img, img])
        else:
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        img = img.astype(np.float32)/255.
        img =np.array(img)
        img = img.transpose(2,0,1)
        img = np.expand_dims(img, axis=0)
        img = torch.from_numpy(img)
        img = img.to(device)

        return img

    def predict(self, img):
        predict = self.model(img)
        predict = np.argmax(predict.cpu().detach().numpy(), axis=-1)

        return predict

    def postprocessing(self, pred):
        if pred == 0:
            return {"prediction": "Normal"}
        if pred == 1:
            return {"prediction": "Pneumonia"}
        
    def compute_prediction(self, img):
        try:
            img = self.preprocessing(img)
            pred = self.predict(img)
            prediction = self.postprocessing(pred)
        except Exception as e:
            return {"status": "Error", "message": str(e)}
        
        return prediction