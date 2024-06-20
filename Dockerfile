
# Dockerfile to build custom image for the e2e pipeline. this is built locally and pused to ECR in DFD Dev account. This si ECR is public

# Use cimg/python:3.9 as the base image
FROM cimg/python:3.9

# Set working directory
WORKDIR /app

# Install OpenJDK-11
RUN sudo apt-get update && \
    sudo apt-get install -y openjdk-11-jre

# Install pytest
RUN pip install pytest

# Download and install Allure Commandline
RUN wget https://repo.maven.apache.org/maven2/io/qameta/allure/allure-commandline/2.17.2/allure-commandline-2.17.2.tgz -P /tmp/ && \
    sudo tar -zxvf /tmp/allure-commandline-2.17.2.tgz -C /opt/ && \
    sudo ln -s /opt/allure-2.17.2/bin/allure /usr/bin/allure

# Verify installations
RUN java -version && allure --version
