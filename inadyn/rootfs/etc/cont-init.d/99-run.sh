#!/usr/bin/env bashio
# shellcheck shell=bash

#################
# Create config #
#################
mustache-cli /data/options.json /templates/inadyn.mustache >/etc/inadyn.conf

# Check it
/usr/sbin/inadyn --check-config

## If cache folder not exit then make
if [ -f /share/inadyn-cache ]; then
    mkdir /share/inadyn-cache
    chmod +w /share/inadyn-cache
fi

##############
# Launch App #
##############
/usr/sbin/inadyn --foreground --force
