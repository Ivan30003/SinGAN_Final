FROM ubuntu:20.04

RUN apt-get update
RUN apt-get install ffmpeg libsm6 libxext6  -y
RUN apt-get install -y python3
RUN apt-get install -y python3-pip

COPY . .

RUN pip3 install --no-cache-dir -r requirements.txt

CMD ["python3","generation/test_main.py","--device", "cpu"]
# CMD ["python3","generation/test_result_image.py"]
# CMD ["python3","generation/main.py"]