ARG BUILD_FROM="ghcr.io/hassio-addons/base:13.0.1"
# build from source in folder with hass addon base
FROM $BUILD_FROM

RUN apk --no-cache add --virtual .build-dependencies \
  autoconf \
  automake \
  confuse-dev \
  gcc \
  gnutls-dev \
  libc-dev \
  libtool \
  make\
  git

ARG INADYN_VERSION="v2.10.0"
RUN git clone --depth 1 --branch "$INADYN_VERSION" https://github.com/troglobit/inadyn
#WORKDIR /root/source
WORKDIR /inadyn
RUN ./autogen.sh
RUN ./configure --prefix=/usr --sysconfdir=/etc --localstatedir=/usr
RUN make install

WORKDIR /root
RUN apk del --no-cache --purge .build-dependencies &&\
    rm -rf /root/source

RUN apk --no-cache add \
  ca-certificates \
  confuse \
  gnutls

# 2 Modify Image #

# Set S6 wait time
ENV S6_CMD_WAIT_FOR_SERVICES=1 \
    S6_CMD_WAIT_FOR_SERVICES_MAXTIME=0 \
    S6_SERVICES_GRACETIME=0

ARG BUILD_ARCH
ENV LANG='C.UTF-8'\
    TERM='xterm-256color'\
    GOPATH='/opt/go'

# 3 Install apps #

# Add rootfs
COPY rootfs/ /

# Corrects permissions for s6 v3
RUN if [ -d /etc/cont-init.d ]; then chmod -R 755 /etc/cont-init.d; fi && \
    if [ -d /etc/services.d ]; then chmod -R 755 /etc/services.d; fi && \
    if [ -f /entrypoint.sh ]; then chmod 755 /entrypoint.sh; fi

# Modules
ARG MODULES="00-banner.sh 01-custom_script.sh"

WORKDIR /
RUN apk add --no-cache --virtual .build-deps\
    build-base\
    git\
    go &&\
    go env -w GO111MODULE=off &&\
    go get -u github.com/quantumew/mustache-cli &&\
    cp "$GOPATH"/bin/* /usr/bin/ && \
    rm -rf "$GOPATH" /var/cache/apk/* /tmp/src &&\
    apk del --no-cache --purge .build-deps xz build-base go git || true

# Some more build cleanup
RUN rm -rf /root/.cache/go-build /media/* /usr/share/doc /usr/share/man /usr/share/misc /inadyn

# 4 Entrypoint #

WORKDIR /
RUN chmod 777 /entrypoint.sh
ENTRYPOINT [ "/usr/bin/env" ]
CMD [ "/entrypoint.sh" ]
VOLUME [ "/data" ]

# 5 Labels #

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
