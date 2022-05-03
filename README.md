# SinGAN_Final
## Requirements
Ubuntu 20.04

## Preparing
Firstly, clone repository:
```
git clone https://github.com/Ivan30003/SinGAN_Final
```
Set directory:
```
cd /SinGAN_Final
```

## Docker
Build docker image:
```
docker build -t SinGAN_36
```
Run it with (both tests will be launched):
```
docker run <container_id>
```
## Watch images
To copy images from container to your machine:
```
docker cp <container_id>: results <path_on_your_machine>
```

