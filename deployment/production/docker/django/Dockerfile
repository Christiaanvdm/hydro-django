#--------- Generic stuff all our Dockerfiles should start with so we get caching ------------
# Note this base image is based on debian
FROM kartoza/django-base:3.7
MAINTAINER Tim Sutton<tim@kartoza.com>

#RUN  ln -s /bin/true /sbin/initctl

# Pandoc needed to generate rst dumps, uic compressor needed for django-pipeline
RUN apt-get update -y; apt-get -y --force-yes install yui-compressor

ARG HYDRO_TAG=develop
RUN mkdir -p /usr/src; mkdir -p /home/web  && \
	git clone --branch ${HYDRO_TAG} --depth 1 https://github.com/kartoza/hydro.git /usr/src/hydro && \
	rm -rf /home/web/django_project && \
	ln -s /usr/src/hydro/django_project /home/web/django_project

RUN cd /usr/src/hydro/deployment/docker && \
	pip3 install -r REQUIREMENTS.txt && \
	pip3 install uwsgi && \
	rm -rf /uwsgi.conf && \
	ln -s ${PWD}/uwsgi.conf /uwsgi.conf

# Open port 8080 as we will be running our uwsgi socket on that
EXPOSE 8080

WORKDIR /home/web/django_project
CMD ["uwsgi", "--ini", "/uwsgi.conf"]
