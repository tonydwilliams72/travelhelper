#FROM ubuntu:16.04
FROM resin/raspberrypi3-alpine-python

#RUN apt-get update && apt-get install -y \
#    python-pip
RUN mkdir /srv/travelhelper
COPY . /srv/travelhelpder
RUN pip install --upgrade pip
RUN pip install -r /srv/travelhelpder/requirements.txt

ENTRYPOINT ["python"]
CMD ["/srv/travelhelpder/run.py"]
