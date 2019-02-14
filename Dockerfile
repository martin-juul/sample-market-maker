FROM python:3.7.2-alpine3.9

LABEL org.label-schema.name = "bitmex-market-maker"
LABEL org.label-schema.description = "Market making bot for BitMEX API"
LABEL org.label-schema.vcs-url = "https://github.com/martin-juul/sample-market-maker"
LABEL org.label-schema.vendor = "Martin Juul <code@juul.xyz>"
LABEL org.label-schema.schema-version = "1.0"

ADD . /usr/local/marketmaker

WORKDIR /usr/local/marketmaker

RUN set -xe \
    && pip3 install --no-cache-dir -r requirements.txt

CMD ["python", "/usr/local/marketmaker/marketmaker"]