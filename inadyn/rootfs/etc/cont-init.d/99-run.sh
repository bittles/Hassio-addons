#!/usr/bin/env bashio
# shellcheck shell=bash

#################
# Create config #
#################
mustache-cli /data/options.json /templates/inadyn.mustache >/etc/inadyn.conf

# Check it
/usr/sbin/inadyn --check-config

## If cache folder not exit then make
mkdir /share/inadyn-cache
chmod a+rw /share/inadyn-cache
rm rf /root/.cache/inadyn
ln -s /share/inadyn-cache /root/.cache/inadyn
chmod a+rw /root/.cache/inadyn

##############
# Launch App #
##############
/usr/sbin/inadyn --foreground --force
