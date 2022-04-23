# SinGAN_Final
## Requirements
Your will need console (this repository was tested in git bash console) with python (and pip) available in it. (Python > Python2 is needed)

## Preparing
Firstly, clone repository:
```
git clone https://github.com/Ivan30003/SinGAN_Final
```
Set directory to repository directory (or print directory manually):
```
cd ./SinGAN/
```
## Installing dependecies
This code was tested and checked with pytorch version 1.8.1. \
Install requirements (manually is also possible):
```
python -m pip install -r requirements.txt
```
## Testing
To launch smoke test run (it checks code workability):
```
python generation/test_main.py
```
If console write: "Torch not complied with CUDA enabled" Then add --device cpu \
If previous test is OK, launch test, which compare FIRST result image with checking ones, they must be the same (enter the path to first generated image):
```
python generation/test_result_image.py --result-image-path <your-path>
```
## Evaluating
To launch evaluating and generate more images run. \
Just specify --num-step, which is a number of pictures generated
(to make it faster, just 15-30 seconds, don't enter --num-steps > 100):
```
python generation/main.py --root images/balloons.png --evaluation --model-to-load results/g_multivanilla.pt --amps-to-load results/amps.pt --num-steps <enter num of images to generate> --batch-size 1
```
If console write: "Torch not complied with CUDA enabled" Then add --device cpu
