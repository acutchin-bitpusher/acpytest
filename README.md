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


##  DOCKER

* build Docker image with version tag in `version.py`

  * on M1 Mac ([requires special 'buildx' invocation](https://blog.jaimyn.dev/how-to-build-multi-architecture-docker-images-on-an-m1-mac/))

            TAG=`cat version.py | cut -f2 -d= | tr -d \'`; docker buildx build --platform linux/amd64 -t acutchinbitpusher/actest:$TAG .

  * on Linux

            TAG=`cat version.py | cut -f2 -d= | tr -d \'`; docker build -f Dockerfile -t acutchinbitpusher/actest:$TAG .

* push to DockerHub

        TAG=`cat version.py | cut -f2 -d= | tr -d \'`; docker push acutchinbitpusher/actest:$TAG


##  Build for EC2 and push to DockerHub

        DH_ACCT='acutchinbitpusher'; REPO='acpytest'; TAG=`cat version.py | cut -f2 -d= | tr -d \'`; docker buildx build --platform linux/amd64 -t $DH_ACCT/$REPO:$TAG . && docker push $DH_ACCT/$REPO:$TAG

