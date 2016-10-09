#!/bin/bash

SHA1=$1

REGION="eu-west-1"
APP="travelhelper"
DOCKER_IMAGE="145949126156.dkr.ecr.eu-west-1.amazonaws.com/travel-helper"
TAG=$SHA1
S3_BUCKET="amit-code"
S3_DIR=$APP

# Update Dockerrun Template
sed  "s|<DOCKER_IMAGE>|$DOCKER_IMAGE|g ; s|<TAG>|$SHA1|g" Dockerrun.aws.json.template > Dockerrun.aws.json

# Printing Template
cat Dockerrun.aws.json

# Copy Template to S3
aws s3 cp Dockerrun.aws.json s3://$S3_BUCKET/$S3_DIR/Dockerrun.aws.json

# Create New EB Version
aws elasticbeanstalk create-application-version --region=$REGION \
                                                --application-name $APP \
                                                --version-label $SHA1 \
                                                --source-bundle S3Bucket=$S3_BUCKET,S3Key=$S3_DIR/Dockerrun.aws.json
# Deploy New EB Version
aws elasticbeanstalk update-environment --region=$REGION \
					--environment-name $APP \
				        --version-label $SHA1
