FROM ubuntu:latest
MAINTAINER Porphyrio

ENV potential /usr/local/potential


# Set bitbucket read-only access
RUN mkdir /root/.ssh
ADD script/bitbucket_key_id_rsa  /root/.ssh/bitbucket_key_id_rsa
ADD script/config /root/.ssh/config

RUN apk update \
    && apk upgrade \
    && apt-get install openssh \
    && chmod 600 /root/.ssh/bitbucket_key_id_rsa \
    && chmod 600 /root/.ssh/config \
    && ssh-keyscan -t rsa bitbucket.org >> /root/.ssh/known_hosts


# Install reporter and dependencies
RUN apt-get add curl \
    && apt-get install python \
    && apt-get install libffi-dev \
    && apt-get install libpq-dev \
    && apt-get install python-dev \
    && apt-get install musl-dev \
    && apt-get install build-base\
    && ln -s /usr/include/locale.h /usr/include/xlocale.h \
    && apt-get install git \
    && curl -sS https://bootstrap.pypa.io/get-pip.py | python \
    && pip install git+ssh://git@github.com:Vinnie1986/iotpotential.git@implement_rds_service#egg=potential001 \
    && apk del musl-dev python-dev gcc git curl \
    && rm -rf /var/cache/apk/*


# Create the user
RUN adduser -S -s /bin/bash -h ${potential} potential

# Set the install script and configuration
ADD script/entrypoint.sh ${potential}/entrypoint.sh

RUN \
    chown -R reporter: ${potential} \
    && chmod +x ${PHY_REPORTER_HOME}/entrypoint.sh

# EXPOSE 5000

USER potential

WORKDIR ${PHY_REPORTER_HOME}
CMD ["./entrypoint.sh"]


