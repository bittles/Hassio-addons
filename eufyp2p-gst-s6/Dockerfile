# use restreamio ubuntu gstreamer base
ARG BUILD_ARCH
#FROM restreamio/gstreamer:${BUILD_ARCH}-latest-prod
FROM bittles999/hassio-gstreamer

# Install ffmpeg, tini (for signal handling), and other common tools for the echo source.
RUN \
    apt-get update && \
    apt-get install -y --no-install-recommends \
#        curl \
        ffmpeg \
        gzip \
#        jq \
        psmisc \
        python3-pip \
        tar \
        tini \
        wget

# Grab GO2RTC and ngrok binaries, not sure if ngrok needed.  It's in go2rtc addon
# Versions
ARG BUILD_ARCH
ARG GO2RTC_VERSION="v1.2.0"
ARG NGROK_VERSION="v3-3.1.1"
# Set non-matching defaults to make sure they set right
ARG GO2RTC_ARCH="amd64"
ARG NGROK_ARCH_URL_SUBDIR="3uoGJrwPaSE"

RUN if [ "${BUILD_ARCH}" = "aarch64" ]; then GO2RTC_ARCH="arm64"; fi \
    && if [ "${BUILD_ARCH}" = "amd64" ]; then GO2RTC_ARCH="amd64"; fi \
    && if [ "${BUILD_ARCH}" = "armhf" ]; then GO2RTC_ARCH="arm"; fi \
    && if [ "${BUILD_ARCH}" = "armv7" ]; then GO2RTC_ARCH="arm"; fi \
    && wget https://github.com/AlexxIT/go2rtc/releases/download/${GO2RTC_VERSION}/go2rtc_linux_${GO2RTC_ARCH} \
    && if [ "${GO2RTC_ARCH}" = "arm64" ]; then NGROK_ARCH_URL_SUBDIR="3uoGJrwPaSE"; fi \
    && if [ "${GO2RTC_ARCH}" = "amd64" ]; then NGROK_ARCH_URL_SUBDIR="cr98VkAAe6w"; fi \
    && if [ "${GO2RTC_ARCH}" = "arm" ]; then NGROK_ARCH_URL_SUBDIR="aPXjX6QdzRS"; fi \
    && if [ "${GO2RTC_ARCH}" = "arm" ]; then NGROK_ARCH_URL_SUBDIR="aPXjX6QdzRS"; fi \
    && wget https://bin.equinox.io/a/${NGROK_ARCH_URL_SUBDIR}/ngrok-${NGROK_VERSION}-linux-${GO2RTC_ARCH}.zip \
    && mv ngrok-${NGROK_VERSION}-linux-${GO2RTC_ARCH}.zip ngrok.gz \
    && gzip -d ngrok.gz \
    && mv go2rtc_linux_${GO2RTC_ARCH} /usr/local/bin/go2rtc \
    && mv ngrok /usr/local/bin/

# Hardware Acceleration for Intel CPU for go2rtc (+50MB)
RUN if [ "${BUILD_ARCH}" = "amd64" ]; then apk add --no-cache libva-intel-driver intel-media-driver; fi

COPY root/ /

# Install aiohttp
RUN pip3 install aiohttp
# Set permissions
RUN chmod a+x /etc/s6-overlay/s6-rc.d/go2rtc/* /etc/s6-overlay/s6-rc.d/eufyp2p/* /usr/local/bin/*
WORKDIR /app

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