#! /bin/bash
# A simple script to build and run the docker container

# To run the script you will run ./build.sh <command> <dockerfile_name>
# Commands:
# build - build the docker image
# run - run the docker image
# stop - stop the docker image
# remove - remove the docker image
# exec - terminal into the docker container
# logs - show the logs of the docker image

DOCKERFILE_NAME=${2:-rate-tracker}  # Default to 'rate-tracker' if not provided

if [ "$1" == "build" ]; then
    echo "Building docker image using $DOCKERFILE_NAME"
    docker build -t rate-tracker:lastest -f "$DOCKERFILE_NAME" .

    echo "Running docker image on port 8000"
    docker run -d -p 8000:8000 --name "$DOCKERFILE_NAME" "$DOCKERFILE_NAME"
fi

if [ "$1" == "run" ]; then
    echo "Running docker image"
    docker run -d -p 8000:8000 --name "$DOCKERFILE_NAME" "$DOCKERFILE_NAME"
fi

if [ "$1" == "stop" ]; then
    echo "Stopping docker image"
    docker stop rate-tracker
fi

if [ "$1" == "remove" ]; then
    echo "Removing docker image"
    docker rm rate-tracker  
fi

if [ "$1" == "exec" ]; then
    echo "Executing docker image"
    docker exec -it rate-tracker /bin/bash
fi

if [ "$1" == "logs" ]; then
    echo "Showing logs"
    docker logs rate-tracker
fi