FROM ubuntu:16.04

RUN apt-get update && apt-get install -y \
    python-pip
RUN mkdir /srv/travelhelper
RUN date
COPY . /srv/travelhelpder
RUN pip install --upgrade pip
RUN pip install -r /srv/travelhelpder/requirements.txt

ENTRYPOINT ["python"]
CMD ["/srv/travelhelpder/run.py"]
