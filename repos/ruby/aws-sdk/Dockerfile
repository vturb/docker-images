FROM --platform=amd64 ruby:alpine

# add annotation
LABEL org.opencontainers.image.source=https://github.com/vturb/docker-images/tree/master/repos/ruby/aws-sdk

USER root

RUN /usr/sbin/adduser -D -H -u 1000 ruby ruby

RUN apk update && apk add --no-cache  \
    bash \
    git \
    curl \
    libpng-dev \
    oniguruma-dev\
    libxml2-dev \
    zip \
    unzip; \
    gem install -N bundler -v 2.4.22; \
    gem install -N nokogiri -v 1.16; \
    gem install -N aws-sdk -v 3.2; \
    mkdir /app; \
    chown -R ruby:ruby /app

WORKDIR /app
USER ruby

