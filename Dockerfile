FROM python:3.9.13

ENV PYTHONUNBUFFERED=1

WORKDIR /code

COPY requirements.txt . 
COPY . .

# install dependencies
RUN apt-get update 
RUN apt install -y libgl1-mesa-glx
# RUN apt-get install ffmpeg libsm6 libxext6  -y
# RUN pip install --no-index --find-links . tensorflow
# RUN pip install tensorflow --extra-index-url https://storage.googleapis.com/tensorflow/windows/cpu/tensorflow_cpu-2.12.0-cp39-cp39-win_amd64.whl
# RUN pip install --default-timeout=100 future
RUN pip install -r requirements.txt


# tell the port number container should expose
EXPOSE 8000

# run command
CMD ["python", "manage.py", "runserver","0.0.0.0:8000"]