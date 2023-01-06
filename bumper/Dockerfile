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

# Copy only required folders instead of all
COPY root/ /

RUN apk add --no-cache nginx nginx-mod-stream openssl curl ca-certificates

# install required python packages
RUN pip3 install -r requirements.txt

WORKDIR /bumper

RUN chmod a+x /create_certs/* /create_certs/src/*
RUN chmod a+x /bumper/run.sh

CMD [ "./run.sh" ]