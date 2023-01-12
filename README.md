# Bumper Addon for Home Assistant
Use my custom Ecovacs component [here](https://github.com/bittles/ha_ecovacs_bumper) to use with Home Assistant.  Mainly just adds ability to not verify SSL which is needed as the cert is self-signed.  Built from a fork I made of bumper [here](https://github.com/bittles/bumper-fork), that made some minor changes of bmartnin5692's [original bumper](https://github.com/bmartin5692/bumper) that I got working fully with my N79 and decided to try to turn it into a HASS addon for easy management which I got working.

The certs it creates for app usage from a phone are in ssl/bumper_certs and the database for the server is in share/bumper_data.

## Bumper 
Bumper is a standalone and self-hosted implementation of the central server used by Ecovacs vacuum robots.  Bumper allows you to have full control of your Ecovacs robots, without the robots or app talking to the Ecovacs servers and transmitting data outside of your home.

# Inadyn Addon for Home Assistant
Just a fork from alexbelgium's addon [here](https://github.com/alexbelgium/hassio-addons/tree/master/inadyn).  Really was just trying to get image and backup size down which I did.  Based off one of 13.0.1 of the hassio addon base, cleaned up the Dockerfile some, and wanted to store cache files which are now accessible in addon data folder but want to move them to share or something so they persist through uninstalls and easy transfers.