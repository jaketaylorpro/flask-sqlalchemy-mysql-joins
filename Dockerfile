# This Dockerfile can be used in pycharm to set up a remote interpreter.
# in this dir run `docker build . -t python_ricult_dev`
# go to project interpreter settings, select add, choose Docker, enter the docker tag 'python_ricult_dev:latest' and command 'python2'
# in run configurations you'll need to add the mysql server as an external host. this can be done in the 'docker container settings' field
# if this reads files from disk, we may need to set up some path mapping.
FROM buildpack-deps:stretch
# install python and requirements' dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
		tk-dev \
		apt-utils \
		net-tools \
		python2.7-dev \
		python-setuptools \
		python-pip \
		libgeos-dev \
		libmemcached-dev \
		zlib1g-dev \
	&& rm -rf /var/lib/apt/lists/*
# install requirements
ADD requirements.txt .
RUN pip install -r requirements.txt
# for intellij
WORKDIR /opt/project
EXPOSE 80/tcp