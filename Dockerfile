FROM alpine

RUN apk add --update \
    python \
    python-dev \
    gcc \
    linux-headers \
    g++ \
    py-pip

RUN mkdir /srv/travelhelper

COPY . /srv/travelhelpder
RUN pip install --upgrade pip
RUN pip install -r /srv/travelhelpder/requirements.txt

ENTRYPOINT ["python"]
CMD ["/srv/travelhelpder/run.py"]
