#!/usr/bin/env bashio
# shellcheck shell=bash

#################
# Create config #
#################
mustache-cli /data/options.json /templates/inadyn.mustache >/etc/inadyn.conf

# If cache folder not exist then make it
if [ ! -d /share/inadyn-cache ]; then
    mkdir /share/inadyn-cache
fi

# Check it
/usr/sbin/inadyn --check-config

# If inadyn cache dir exists, check if it's not a symbolic link, if it's not a link then remove the folder and create a link
# test -d is true if it's a dir or a link to a dir, so further needs to test if it's symbolic link
if [ -d /root/.cache/inadyn ]; then
    if [ ! -L /root/.cache/inadyn ]; then
        rm -rf /root/.cache/inadyn
        ln -s /share/inadyn-cache /root/.cache/inadyn
    fi
# If inadyn cache is false with test -d then it's false with test -L
else
    ln -s /share/inadyn-cache /root/.cache/inadyn
fi


##############
# Launch App #
##############
/usr/sbin/inadyn --foreground --force
