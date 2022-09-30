#!/bin/bash
path_repo=`pwd`
sudo docker build -t api_app .
sudo docker run -p 8000:8000 api_app

