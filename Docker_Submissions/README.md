# MedICI Docker Submission Template

## Dockerfile
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

* This is the Dockerfile to show how you could build this submission image.
* It is based on pytorch but tensorflow is acceptable and so is any deep learning package or library.

> The command "COPY data /workspace/data" is for my pytorch code (sample_deep_learning_model.py). You will not have internet on our system, so since the tutorial deep learning algorithm needs the CIFAR10 dataset, I had to load it in ahead of time. You shouldn't have this problem as your input data will be mounted to /mnt/in, so you will have access to it during run time.

## read_files.py
```python
import os, pandas as pd, random, sys

# Sample Deep Learning Run
import sample_deep_learning_model

# for use with docker mounts
IN = '/mnt/in'
OUT = '/mnt/out'


if __name__ == "__main__":
    files_dir = os.path.join(IN,'Pathology')
    print(files_dir)
    files = [file[0:-5] for file in os.listdir(files_dir) if file.find('.tiff') != -1]
    classes = ['A','O','G']
    submission_csv = pd.DataFrame({"CPM_RadPath_2020_ID":files, "class":[random.choice(classes) for file in files]})
    
    # Deep Learning Model
    sample_deep_learning_model.run()
    # Deep Learning Model

    submission_csv.to_csv(os.path.join(OUT,"random.csv"), index=None)
```

This is actually the main python file that gets executed. The following things happen in here:  
1. ```import sample_deep_learning_model``` - which is a pytorch tutorial. This should be replaced by your algorithm.  
2. IN and OUT are defined as /mnt/in and /mnt/out. There is some flexibility here on whether you use the IN and OUT variables specifically. The important thing is to make sure you read in files from /mnt/in and output your classification to /mnt/out. These will be mounts specified using the "-v" flag.  
3. sample_deep_learning_model.py is the file that hold the algorithm. You don't need a separate file, but I separate it out to organize things. Technically you can use one single file for everything or multiple files (more than 2 even).
4. "directory_of_files" is what I mount to /mnt/in inside the container and is a folder where fake files are located so you can test this template out on them. It has Pathology and Radiology folders with all their subfolders and files (for training set). These are blank files with custom extensions but have no real data. I use them in "read_files.py" to create my csv output key column "CPM_RadPath_2020_ID". This is an example set of data from the miccai 2020 (challenge)[https://miccai.westus2.cloudapp.azure.com/].

> Note: use ```docker build -t <tag name> .``` to create image using this directory's Dockerfile

When run on our system, the command will be:
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
  cpmchallenges/miccai-2020:training_phase_dl_submission

```
> Note: <path> will be set by competition organizers. Same for <auto generated id>

## Demo - part 1

[1] Clone repo
```bash
$ git clone https://github.com/QTIM-Lab/MedICI.git
$ cd MedICI/Docker_Submissions; mkdir out;
```

[2] Build local image
```
$ docker build -t cpmchallenges/miccai-2020:training_phase_dl_submission .
```

[3] Download CIFAR images inside ./Docker_Submissions/directory_of_files

> You will have to use your own local paths. I recommend mounting the cloned "directory_of_files". It will make a more seamless demo.

```bash
PATH_TO_MedICI=/home/bbearce/Documents/MedICI/;
```

```
$ docker run \
  --rm \
  -v $PATH_TO_MedICI/Docker_Submissions/directory_of_files/:/mnt/in \
  cpmchallenges/miccai-2020:training_phase_dl_submission \
  python download_CIFAR_images.py
```

[4] Run the image and don't forget to add a location for "/mnt/out":
> ```-v /home/bbearce/Documents/MedICI/Docker_Submissions/out/:/mnt/out \```

You can run it normally:
```bash
$ docker run \
  --rm \
  -v $PATH_TO_MedICI/Docker_Submissions/directory_of_files/:/mnt/in \
  -v $PATH_TO_MedICI/Docker_Submissions/out/:/mnt/out \
  cpmchallenges/miccai-2020:training_phase_dl_submission
```

or interactively:
```bash
$ docker run \
  -it \
  --rm \
  -v $PATH_TO_MedICI/Docker_Submissions/directory_of_files/:/mnt/in \
  -v $PATH_TO_MedICI/Docker_Submissions/out/:/mnt/out \
  cpmchallenges/miccai-2020:training_phase_dl_submission \
  bash
```

and then:
```bash
$ python read_files.py
```

## Demo - part 2

To submit to CodaLab there is only a couple changes required.

[1] Dockerfile
Un comment this code: ```# COPY ./directory_of_files/data /workspace/data```

[2] read_files.py

Comment out the local ```sample_deep_learning_model``` and uncomment the CodaLab one so that it looks as follows:

```python
    # Deep Learning Model - local
    # sample_deep_learning_model.run(IN+"/data", OUT)
    # Deep Learning Model - local

    # Deep Learning Model - CodaLab submission
    sample_deep_learning_model.run("/workspace/data", OUT)
    # Deep Learning Model - CodaLab submission
```

[3] Rebuild the image

```bash
$ docker build -t cpmchallenges/miccai-2020:training_phase_dl_submission .
```

[4] Test run to make sure it still works:
```bash
$ docker run \
  --rm \
  -v $PATH_TO_MedICI/Docker_Submissions/directory_of_files/:/mnt/in \
  -v $PATH_TO_MedICI/Docker_Submissions/out/:/mnt/out \
  cpmchallenges/miccai-2020:training_phase_dl_submission
```

[5] Push to a repo:

```bash
$ docker push cpmchallenges/miccai-2020:training_phase_dl_submission
```













