from rest_framework.views import APIView
from django.core.files.storage import FileSystemStorage
from rest_framework.response import Response
from django.conf import settings

import cv2
from ml.classifier.classifier import Classifier

class CustomFileSystemStorage(FileSystemStorage):
    def get_available_name(self, name, max_length=None):
        self.delete(name)
        return name
    
class call_model(APIView):

    def get(self, request):
        return Response("Hello World!")

    def post(sefl, request):
        fss = CustomFileSystemStorage()
        image = request.FILES["image"]
        print("Name", image.file)
        _image = fss.save(image.name, image)
        path = str(settings.MEDIA_ROOT) + "/" + image.name
        # Read the image
        img=cv2.imread(path)
        classifier = Classifier()
        prediction = classifier.compute_prediction(img)

        return Response(prediction)

