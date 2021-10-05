# Docker Scripts
The goal of these scripts are to reduce errors or help with cases of the `butter-fingers` when typing commands.

### `build.sh` - Builds (and run if needed) images
script variables and usage
```javascript
BUILD_AND_RUN=true                      // docker runs an image if true
REPLACE_ANCESTOR=false                  // replace containers built with the same image
APP_LOCATION=''                         // location of the app and Dockerfile
IMAGE_NAME=''                           // name of the container image
IMAGE_TAG=''                            // tag of the container image
PORT_LOCAL=''                           // local port to map image to
PORT_CONTAINER=''                       // container port exposed by the app
CONTAINER_NAME=''                       // container name
```


### `push.sh` - Push apps to a Container Registry
script variables and usage
```javascript
AZURE_LOGIN=false                       // vendor specific boolean to login on Azure
AZURE_USE_AZ_CLI=false                  // boolean check to use AZ CLI
AZURE_ACR_NAME=''                       // docker registry name


DOCKER_REGISTRY=''                      // docker registry e.g. iad.ocir.io, <acrLoginServer>.azurecr.io
DOCKER_REGISTRY_USERNAME=''             // docker registry username
DOCKER_REGISTRY_CREDENTIALS_LOCATION='' // docker login credentials file location to pipe
LOCAL_IMAGE=''                          // local image name
LOCAL_TAG=''                            // local image tag
REMOTE_IMAGE=''                         // remote image name
REMOTE_TAG=''                           // remote tag
```
example for __Oracle Cloud__
```javascript
DOCKER_REGISTRY='iad.ocir.io'
DOCKER_REGISTRY_USERNAME='namespace/oracleidentitycloudservice/username'
DOCKER_REGISTRY_CREDENTIALS_LOCATION='./pwd.txt'
LOCAL_IMAGE='frontend'
LOCAL_TAG='latest'
REMOTE_IMAGE='iad.ocir.io/tenancy/frontend'
REMOTE_TAG='latest'
```

example for __Azure Cloud__
example for __Oracle Cloud__
```javascript
AZURE_LOGIN=true
AZURE_USE_AZ_CLI=true
AZURE_ACR_NAME='registryname'

DOCKER_REGISTRY='registryname.azurecr.io'
DOCKER_REGISTRY_USERNAME=''
DOCKER_REGISTRY_CREDENTIALS_LOCATION=''
LOCAL_IMAGE='frontend'
LOCAL_TAG='latest'
REMOTE_IMAGE='registryname.azurecr.io/frontend'
REMOTE_TAG='latest'
```