#!/bin/bash

############################
# variables
############################
BUILD_AND_RUN=true
REPLACE_ANCESTOR=false

APP_LOCATION=''

IMAGE_NAME=''
IMAGE_TAG=''

PORT_LOCAL=''
PORT_CONTAINER=''
CONTAINER_NAME=''


### Building
echo ''
echo -e '[SCRIPT] Starting Image Building' ${IMAGE_NAME}:${IMAGE_TAG}
docker build -t $IMAGE_NAME:$IMAGE_TAG $APP_LOCATION -q

echo -e '\033[0;32m[SCRIPT]\033[0m Finished Building' ${IMAGE_NAME}:${IMAGE_TAG}


if [ "$BUILD_AND_RUN" = true ] 
then

    ### If CONTAINER_NAME is defined
    if [ -n "$CONTAINER_NAME" ]
    then
        ### Finding pre-existing containers with the same container name
        _CONTAINER_ID=$(docker ps -aq --filter name=${CONTAINER_NAME} --filter ancestor=${IMAGE_NAME}:${IMAGE_TAG})


        ### Replacing pre-existing containers
        echo ''
        echo -e '[SCRIPT] Finding pre-existing containers to replace'
        if [ -n "$_CONTAINER_ID" ]
        then
            docker stop $_CONTAINER_ID && docker rm $_CONTAINER_ID
            echo -e '\033[0;32m[SCRIPT]\033[0m Deleted and removed existing container' ${IMAGE_NAME}:${IMAGE_TAG}
        else
            echo -e '\033[0;32m[SCRIPT]\033[0m No pre-exisisting containers. Proceeding' ${IMAGE_NAME}:${IMAGE_TAG}
        fi

        ### Running image
        echo ''
        echo -e '[SCRIPT] Starting to run container' ${IMAGE_NAME}:${IMAGE_TAG}
        docker run -p :$PORT_LOCAL:$PORT_CONTAINER -d --name $CONTAINER_NAME $IMAGE_NAME:$IMAGE_TAG
        echo -e '\033[0;32m[SCRIPT]\033[0m Container' $CONTAINER_NAME 'now running.'
    elif [ "$REPLACE_ANCESTOR" = true ]
    then
        ### Finding pre-existing containers with the same ancestor
        _CONTAINER_ID=$(docker ps -aq --filter ancestor=${IMAGE_NAME}:${IMAGE_TAG})

        ### Replacing pre-existing containers
        echo ''
        echo -e '[SCRIPT] Finding pre-existing containers to replace'
        if [ -n "$_CONTAINER_ID" ]
        then
            docker stop $_CONTAINER_ID && docker rm $_CONTAINER_ID
            echo -e '\033[0;32m[SCRIPT]\033[0m Deleted and removed existing container' ${IMAGE_NAME}:${IMAGE_TAG}
        else
            echo -e '\033[0;32m[SCRIPT]\033[0m No pre-exisisting containers. Proceeding' ${IMAGE_NAME}:${IMAGE_TAG}
        fi

        ### Running image
        echo ''
        echo -e '[SCRIPT] Starting to run container' ${IMAGE_NAME}:${IMAGE_TAG}
        _CONTAINER_ID=$(docker run -p :$PORT_LOCAL:$PORT_CONTAINER -d $IMAGE_NAME:$IMAGE_TAG)
        _CONTAINER_NAME=$(docker ps -a --format "{{.Names}}" --filter id=$_CONTAINER_ID)
        _RESULT=$(docker inspect -f {{.State.Running}} $_CONTAINER_ID)

        if [ "$_RESULT" = true ]
        then
            echo -e '\033[0;32m[SCRIPT]\033[0m Container' $_CONTAINER_NAME 'now running.'
        else
            echo -e '\033[0;31m[SCRIPT]\033[0m Container' $_CONTAINER_NAME 'failed to run.'
        fi
    else
        ### Running image without a container name
        echo ''
        echo -e '[SCRIPT] Starting to run container' ${IMAGE_NAME}:${IMAGE_TAG}
        _CONTAINER_ID=$(docker run -p :$PORT_LOCAL:$PORT_CONTAINER -d $IMAGE_NAME:$IMAGE_TAG)
        _CONTAINER_NAME=$(docker ps -a --format "{{.Names}}" --filter id=$_CONTAINER_ID)
        _RESULT=$(docker inspect -f {{.State.Running}} $_CONTAINER_ID)

        if [ "$_RESULT" = true ]
        then
            echo -e '\033[0;32m[SCRIPT]\033[0m Container' $_CONTAINER_NAME 'now running.'
        else
            echo -e '\033[0;31m[SCRIPT]\033[0m Container' $_CONTAINER_NAME 'failed to run.'
        fi
    fi

fi