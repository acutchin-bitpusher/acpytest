# acpytest

Python/Flask app for testing infrastructure

* Displays environment variables

* Connects to DB instance

## LOCAL DEV WITH PYTHON-VIRTUALENV

1. install prerequisites

       brew install python3 pyenv

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

* build Docker image and push to DockerHub

       docker build -f Dockerfile -t acutchinbitpusher/actest . && docker push acutchinbitpusher/actest

