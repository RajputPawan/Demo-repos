#!/bin/bash

# Function to start Docker
start_docker() {
  systemctl start docker
  echo "Docker started with pid $(ps -ef|grep -i 'docker'|awk '{print $2}')"
    docker run -d -p 8080:8080 jenkins/jenkins
    docker ps -a |grep -i "jenkins"
}

# Function to check Docker status
status_docker() {
  if systemctl status docker | grep -i inactive; then
    start_docker
  else
    echo "Docker is running"
  fi
}

# Check Docker status
status_docker
