#!/bin/bash

############################
# variables
############################
AZURE_LOGIN=false
AZURE_ACR_NAME=''

DOCKER_REGISTRY=''
DOCKER_REGISTRY_USERNAME=''
DOCKER_REGISTRY_CREDENTIALS_LOCATION=''

LOCAL_IMAGE=''
LOCAL_TAG=''
REMOTE_IMAGE=''
REMOTE_TAG=''

if [ "$AZURE_LOGIN" = true ]
then
    ### Logging In with Azure
    echo ''
    echo -e '[SCRIPT] Logging on Docker Registry' $AZURE_ACR_NAME
    _LOGIN_RESULT=$(az acr login -n $AZURE_ACR_NAME)
else
    ### Logging In with Docker
    echo ''
    echo -e '[SCRIPT] Logging on Docker Registry' $DOCKER_REGISTRY
    _LOGIN_RESULT=$(cat $DOCKER_REGISTRY_CREDENTIALS_LOCATION | docker login $DOCKER_REGISTRY -u ${DOCKER_REGISTRY_USERNAME} --password-stdin)
fi


if [ "$_LOGIN_RESULT" == 'Login Succeeded' ]
then
    echo -e '\033[0;32m[SCRIPT]\033[0m Login Succeeded' 


    ### Tagging Image for Pushing
    echo ''
    echo -e '[SCRIPT] Tagging Image' ${LOCAL_IMAGE}:${LOCAL_TAG}
    docker tag ${LOCAL_IMAGE}:${LOCAL_TAG} ${REMOTE_IMAGE}:${REMOTE_TAG}
    echo -e '\033[0;32m[SCRIPT]\033[0m Image tagged' $REMOTE_IMAGE:$REMOTE_TAG


    ### Pushing Tagged Image
    echo ''
    echo -e '[SCRIPT] Pushing image to Docker Registry'
    _PUSH_RESULT=$(docker push $REMOTE_IMAGE:$REMOTE_TAG -q)

    if [ "$_PUSH_RESULT" = $REMOTE_IMAGE:$REMOTE_TAG ]
    then
        echo -e '\033[0;32m[SCRIPT]\033[0m Image pushed to' $REMOTE_IMAGE:$REMOTE_TAG
    else
        echo -e '\033[0;31m[SCRIPT]\033[0m Pushed Failed (?) for' $REMOTE_IMAGE:$REMOTE_TAG 

    fi
else 
    echo -e '\033[0;31m[SCRIPT]\033[0m Login Failed'
fi