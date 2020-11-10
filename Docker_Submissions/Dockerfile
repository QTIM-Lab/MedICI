FROM pytorch/pytorch:latest

WORKDIR /workspace

# Install packages\libraries
RUN pip install pandas

# wrapper code that can read file names for submission key
COPY read_files.py /workspace
# inference model
COPY sample_deep_learning_model.py /workspace
# dummy data (CIFAR10) images
# COPY data /workspace/data
COPY download_CIFAR_images.py /workspace

#ENTRYPOINT ["python", "read_files.py"]
CMD ["python", "read_files.py"]
