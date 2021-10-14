ARG  CODE_VERSION=latest
FROM ubuntu:${CODE_VERSION}

# Update ubuntu
RUN apt-get update -y 

# Download python and pip
RUN apt-get install -y python3.8 python3-pip && \
    pip install numpy==1.19 && \
    pip install scanpy==1.8.1

# Create location to mount local dir
ENV MOUNT_PATH=/usr/mount
RUN mkdir ${MOUNT_PATH}

# Copy 10x matrix to image
COPY ./import_data.py ./

# Execute python script by default
ENTRYPOINT [ "/usr/bin/python3", "./import_data.py"]
