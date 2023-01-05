#!/usr/bin/with-contenv bashio
set -e

# Create main config
BUMPER_ANNOUNCE_IP=$(bashio::config 'announce_ip')
TZ=$(bashio::config 'time_zone')
BUMPER_LISTEN=$(bashio::config 'announce_ip')
BUMPER_DEBUG=$(bashio::config 'debug_logs')
ENABLE_XMPP=$(bashio::config 'enable_xmpp_server')
ENABLE_MQTT=$(bashio::config 'enable_mqtt_server')

python3 -m bumper --listen $BUMPER_LISTEN --announce $BUMPER_ANNOUNCE_IP --debug $BUMPER_DEBUG --enable_xmpp $ENABLE_XMPP --enable_mqtt $ENABLE_MQTT