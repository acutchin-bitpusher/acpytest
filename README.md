# acpytest

Python/Flask app for testing infrastructure

* Displays environment variables

* Connects to DB instance

* Stress functions based on: https://github.com/mattixtech/stress

## LOCAL DEV WITH PYTHON-VIRTUALENV

1. install prerequisites

       brew install python3 pyenv pyenv-virtualenv virtualenv

1. create virtualenv

       virtualenv venv

1. activate virutalenv

       . venv/bin/activate

1. verify virtual python version

       python --version

1. install pip packages to virutalenv

       pip install -r ./requirements.txt

1. run app

       python3 ./main.py


##  BUILD DOCKER CONTAINER IMAGE

* NOTE:  Relies on version tag in `version.py`

* on M1 Mac ([requires special 'buildx' invocation](https://blog.jaimyn.dev/how-to-build-multi-architecture-docker-images-on-an-m1-mac/))

        TAG=`cat version.py | cut -f2 -d= | tr -d \'`; docker buildx build --platform linux/amd64 -t acutchinbitpusher/actest:$TAG .

* on Linux

        TAG=`cat version.py | cut -f2 -d= | tr -d \'`; docker build -f Dockerfile -t acutchinbitpusher/actest:$TAG .


## RUN THE CONTAINER IMAGE LOCALLY

1. set shell environment variables for convenience

		export CONTAINER='<container_name>'

1. build the container according to the Dockerfile

        docker build -t $CONTAINER $PWD

1. run the container on port 8080

        docker run -d -p 8080:80 -t $CONTAINER

1. observe the new image and running container

        docker ps -a; echo; docker images

1. curl the container:8080 to test

        curl http://localhost:8080

1. stop/delete the image

    	docker stop $CONTAINER && docker rm $CONTAINER

1. repeatedly stop/delete/rebuild the container and test curl:

    1. first time

            docker stop $CONTAINER && docker rm $CONTAINER && docker build -t $CONTAINER . && docker run -d -p 8080:80 --name $CONTAINER $CONTAINER && echo "sleeping 5..." && sleep 5 && curl http://localhost:8080/index.html && echo && echo && docker logs $CONTAINER

    2. repeatedly thereafter

            docker stop $CONTAINER && docker rm $CONTAINER && docker build -t $CONTAINER . && docker run -d -p 8080:80 --name $CONTAINER $CONTAINER && echo "sleeping 5..." && sleep 5 && curl http://localhost:8080/index.html && echo && echo && docker logs $CONTAINER


## Push to Registry

* DockerHub

        TAG=`cat version.py | cut -f2 -d= | tr -d \'`; docker push acutchinbitpusher/actest:$TAG

* AWS ECR

   1. Set shell environment variables for convenience

            export CONTAINER='<container_name>'; export ECR_ACCOUNT_ID='<ecr_account_id>'; export ECR_REGION='<ecr_region>'; export TAG=`cat version.py | cut -f2 -d= | tr -d \'`; export ECR_URL="$ECR_ACCOUNT_ID.dkr.ecr.$ECR_REGION.amazonaws.com"

   1. Rebuild the image for EC2/ECS hardware platform, if necessary

	    	docker build --platform linux/amd64 -t $CONTAINER $PWD

   1. Import AWS creds to shell environment

	        awsume `<aws_account_name>`

   1. Log in to ECR

            aws --region $ECR_REGION ecr get-login-password | docker login --username AWS --password-stdin $ECR_URL

	   * you should see "Login Succeeded"

   1. tag the container with the ECR info

            docker tag $CONTAINER $ECR_URL/$CONTAINER:latest

   1. push image to ECR

            docker push $ECR_URL/$CONTAINER


##  LOAD NEW IMAGE

* BITPUSHER CHEF/DOCKER EC2 INSTANCES

        chef-client

* ECS

        aws --region $AWS_DEFAULT_REGION ecs update-s ervice --cluster <ecs_cluster_name> --service <ecs_service_name> --force-new-deployment

