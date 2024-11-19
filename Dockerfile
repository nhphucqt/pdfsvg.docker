FROM ubuntu:22.04

WORKDIR /home
LABEL maintainer="nhphucqt"
LABEL version="1.0"
LABEL description="This is custom Docker Image for PDF SVG extraction"

# Install the application dependencies
COPY src .
RUN apt update -y && apt upgrade -y
RUN apt install default-jdk -y
RUN apt install poppler-utils -y