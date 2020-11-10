# MedICI Docker Submission Template

## Dockerfile
* This is a sample Dockerfile to show how you could built this submission image.
* It is based on pytorch but tensorflow is acceptable and so is any deep learning package or library.

```bash
FROM pytorch/pytorch:latest

WORKDIR /workspace

# wrapper code that can read file names for submission key
COPY read_files.py /workspace
# inference model
COPY sample_deep_learning_model.py /workspace
# dummy data (CIFAR10) images
COPY data /workspace/data

# Install packages\libraries
RUN pip install pandas

#ENTRYPOINT ["python", "read_files.py"]
CMD ["python", "read_files.py"]
```

* The command "COPY data /workspace/data" is for my pytorch code (sample_deep_learning_model.py). You will not have internet on our system, so since the tutorial deep learning algorithm needs the CIFAR10 dataset, I had to load it in ahead of time. You shouldn't have this problem as your input data will be mounted to /mnt/in, so you will have access to it during run time.

## read_files.py
This is actually the main python file that gets executed. The following things happen in here:  
1. import sample_deep_learning_model - which is a pytorch tutorial. This should be replaced by your algorithm.  
2. IN and OUT are defined as /mnt/in and /mnt/out. There is some flexibility here on whether you use IN and OUT variables specifically. The important thing is to make sure you read in files from /mnt/in and output your classification to /mnt/out. These will be mounts specified using the "-v" flag.  
3. sample_deep_learning_model.py is the file that hold the algorithm. You don't need a separate file, but I separate it out to organize things. Technically you can use one single file for everything or multiple files (more than 2 even).
4. "directory_of_files" is what I mount to /mnt/in inside the container and is a folder where fake files are located so you can test this template out on them. It has the Pathology and Radiology folder with all their subfolders and files (for training set). These are blank files with custom extensions but have no real data. I use them in "read_files.py" to create my csv output key column "CPM_RadPath_2020_ID".

> Note: use ```docker build -t <tag name> .``` to create image using this directory's Dockerfile

The run command will be:
```
docker run \
  --net none \
  --rm \
  --gpus all \
  --name=participant_docker_submission_taskid_<auto generated id> \
  --stop-timeout=5000 \
  --security-opt=no-new-privileges \
  -v <path>/directory_of_files:/mnt/in:ro \
  -v <path>:/mnt/out \
  cpmcomps/miccai-2020:training_phase_dl_submission

```
> Note: <path> will be set by competition organizers. Same for <auto generated id>

