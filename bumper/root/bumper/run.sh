#!/usr/bin/with-contenv bashio
set -e

# Create main config
BUMPER_ANNOUNCE_IP=$(bashio::config 'announce_ip')
TZ=$(bashio::config 'time_zone')
BUMPER_LISTEN=$(bashio::config 'announce_ip')
BUMPER_DEBUG=$(bashio::config 'debug_logs')
ENABLE_XMPP=true
ENABLE_MQTT=true

argline="--listen ${BUMPER_LISTEN} --announce ${BUMPER_ANNOUNCE_IP}"

if [ "${BUMPER_DEBUG}" = true ]
then
    argline+=" --debug"
fi

if [ "$(bashio::config 'disable_xmpp_server')" = true ]
then
    argline+=" --disable-xmpp"
	ENABLE_XMPP=false
fi

if [ "$(bashio::config 'disable_mqtt_server')" = true ]
then
    argline+=" --disable-mqtt"
	ENABLE_MQTT=false
fi

echo "Announce IP is ${BUMPER_ANNOUNCE_IP}"
echo "Listen IP is ${BUMPER_LISTEN}"
echo "Debug is ${BUMPER_DEBUG}"
echo "XMPP Server active is ${ENABLE_XMPP}"
echo "MQTT Server active is ${ENABLE_MQTT}"
echo "python command ran is:"
echo "python3 -m bumper ${argline}"

python3 -m bumper ${argline}