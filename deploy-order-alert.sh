#!/bin/bash

set -e

DOCKER_IMAGE_TAG=$1


cd bybit-order-alert

echo "Shutting Down Previous Containers."

sudo docker-compose -f docker-compose-bybit-order-alert.yaml down

cd ..

echo "Deleting previous directory"

rm -rf bybit-order-alert

echo "Cloning Repo"

git clone https://github.com/HaynesX/bybit-order-alert.git

cd bybit-order-alert

echo "Checkout new version"

git checkout tags/$DOCKER_IMAGE_TAG

echo "Starting Docker Container for Image $DOCKER_IMAGE_TAG"

sudo TAG=$DOCKER_IMAGE_TAG docker-compose -f docker-compose-bybit-order-alert.yaml up -d


