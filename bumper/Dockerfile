# FROM alpine as builder
#ARG FROM_ARCH=arm64v8

# ARG FROM_ARCH=$BUILD_ARCH
ARG BUILD_FROM
FROM $BUILD_FROM as builder

# Download QEMU 
ADD https://github.com/balena-io/qemu/releases/download/v3.0.0%2Bresin/qemu-3.0.0+resin-arm.tar.gz .
RUN tar zxvf qemu-3.0.0+resin-arm.tar.gz --strip-components 1
ADD https://github.com/balena-io/qemu/releases/download/v3.0.0%2Bresin/qemu-3.0.0+resin-aarch64.tar.gz .
RUN tar zxvf qemu-3.0.0+resin-aarch64.tar.gz --strip-components 1

FROM builder as base

# Add QEMU
# Add QEMU
COPY --from=builder qemu-arm-static /usr/bin
COPY --from=builder qemu-aarch64-static /usr/bin

FROM base as builderfinal

# add build utils (gcc, others)
RUN apk add build-base

FROM base

COPY requirements.txt /requirements.txt

RUN apk add --no-cache nginx nginx-mod-stream openssl curl ca-certificates

# install required python packages
RUN pip3 install -r requirements.txt

COPY nginx.conf /etc/nginx/nginx.conf

WORKDIR /bumper

# Copy only required folders instead of all
COPY create_certs/ /create_certs/
COPY bumper/ bumper/
RUN chmod a+x /create_certs/* /create_certs/src/*

COPY data/ /share/bumper-data
COPY certs/ /ssl/bumper-certs

COPY run.sh /
RUN chmod a+x /run.sh

CMD [ "/run.sh" ]