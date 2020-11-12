FROM pytorch/pytorch:latest

WORKDIR /workspace

# Install packages\libraries
RUN pip install pandas
RUN apt-get update -y
RUN apt-get install vim -y

# wrapper code that can read file names for submission key
COPY read_files.py /workspace
# inference model
COPY sample_deep_learning_model.py /workspace
# utility to get sample CIFAR data
COPY download_CIFAR_images.py /workspace

# To submit this demo we need to load the CIFAR data inside the image
# first since we won't have access to internet.
# This won't be necessary in your real image because the only data you need 
# will be supplied at /mnt/in.

COPY ./directory_of_files/data /workspace/data

#ENTRYPOINT ["python", "read_files.py"]
CMD ["python", "read_files.py"]
