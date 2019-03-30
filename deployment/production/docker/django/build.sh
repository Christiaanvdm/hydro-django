#!/usr/bin/env bash

set -e

if [ -z "$REPO_NAME" ]; then
	REPO_NAME=kartoza
fi

if [ -z "$IMAGE_NAME" ]; then
	IMAGE_NAME=hydro_django
fi

if [ -z "$TAG_NAME" ]; then
	TAG_NAME=latest
fi

if [ -z "$BUILD_ARGS" ]; then
	BUILD_ARGS="--pull --no-cache"
fi

if [ -z "$HYDRO_TAG" ]; then
	HYDRO_TAG="develop"
fi

# Build Args Environment
echo "Build: $REPO_NAME/$IMAGE_NAME:$TAG_NAME"

echo "HYDRO_TAG: ${HYDRO_TAG}"

docker build -t ${REPO_NAME}/${IMAGE_NAME} \
	--build-arg HYDRO_TAG=${HYDRO_TAG} \
	${BUILD_ARGS} .
docker tag ${REPO_NAME}/${IMAGE_NAME}:latest ${REPO_NAME}/${IMAGE_NAME}:${TAG_NAME}
docker push ${REPO_NAME}/${IMAGE_NAME}:${TAG_NAME}
