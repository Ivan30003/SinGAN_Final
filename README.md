# SinGAN_Final
## Requirements
At least 9 GB free space (12GB recommended)
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
docker build -t singan_36 .
```
Run it with (both tests will be launched):
```
docker run <container_id>
```
## Watch images
to know the container_id, write:
```
docker ps -a
```
To copy images from container to your machine:
```
docker cp <container_id>: results <path_on_your_machine>
```
