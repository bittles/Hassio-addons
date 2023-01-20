# FROM alpine as builder
#ARG FROM_ARCH=arm64v8

# ARG FROM_ARCH=$BUILD_ARCH
ARG BUILD_FROM
FROM $BUILD_FROM

# Download QEMU 
#ADD https://github.com/balena-io/qemu/releases/download/v3.0.0%2Bresin/qemu-3.0.0+resin-arm.tar.gz .
#RUN tar zxvf qemu-3.0.0+resin-arm.tar.gz --strip-components 1
#ADD https://github.com/balena-io/qemu/releases/download/v3.0.0%2Bresin/qemu-3.0.0+resin-aarch64.tar.gz .
#RUN tar zxvf qemu-3.0.0+resin-aarch64.tar.gz --strip-components 1

#FROM builder as base

# Add QEMU
# Add QEMU
#COPY qemu-arm-static /usr/bin
#COPY qemu-aarch64-static /usr/bin

#FROM base as builderfinal

# add build utils (gcc, others)
#RUN apk add build-base

#FROM base

# Copy only required folders instead of all
COPY root/ /

RUN apk add --no-cache nginx nginx-mod-stream openssl ca-certificates

# install required python packages
RUN pip3 install -r requirements.txt

RUN chmod a+x /create_certs/* /create_certs/src/*
RUN chmod a+x /etc/s6-overlay/s6-rc.d/bumper/* /etc/s6-overlay/s6-rc.d/nginx/* /etc/cont-init.d/*

WORKDIR /bumper

## add labels

ARG BUILD_ARCH
ARG BUILD_DATE
ARG BUILD_DESCRIPTION
ARG BUILD_NAME
ARG BUILD_REF
ARG BUILD_REPOSITORY
ARG BUILD_VERSION
LABEL \
    io.hass.name="${BUILD_NAME}" \
    io.hass.description="${BUILD_DESCRIPTION}" \
    io.hass.arch="${BUILD_ARCH}" \
    io.hass.type="addon" \
    io.hass.version=${BUILD_VERSION} \
    maintainer="bittles (https://github.com/bittles)" \
    org.opencontainers.image.title="${BUILD_NAME}" \
    org.opencontainers.image.description="${BUILD_DESCRIPTION}" \
    org.opencontainers.image.vendor="Home Assistant Add-ons" \
    org.opencontainers.image.authors="bittles (https://github.com/bittles)" \
    org.opencontainers.image.licenses="MIT" \
    org.opencontainers.image.url="https://github.com/bittles" \
    org.opencontainers.image.source="https://github.com/${BUILD_REPOSITORY}" \
    org.opencontainers.image.documentation="https://github.com/${BUILD_REPOSITORY}/blob/main/README.md" \
    org.opencontainers.image.created=${BUILD_DATE} \
    org.opencontainers.image.revision=${BUILD_REF} \
    org.opencontainers.image.version=${BUILD_VERSION}