# Bumper Addon for Home Assistant
Use my custom Ecovacs component [here](https://github.com/bittles/ha_ecovacs_bumper) to uwth with Home Assistant.  Mainly just adds ability to not verify SSL which is needed as the cert is self-signed.  Built from a fork I made of bumper [here](https://github.com/bittles/bumper-fork), that made some minor changes of bmartni5692's [original bumper](https://github.com/bmartin5692/bumper) that I got working fully with my N79 and decided to try to turn it into a HASS addon for easy management which I got working.

The certs it creates for app usage from a phone as in ssl/bumper_certs and the database for the server is in share/bumper_data.

# Bumper 
Bumper is a standalone and self-hosted implementation of the central server used by Ecovacs vacuum robots.  Bumper allows you to have full control of your Ecovacs robots, without the robots or app talking to the Ecovacs servers and transmitting data outside of your home.

## Addon Options
| Option              | Description                                                                                                    |
| ------------------- | -------------------------------------------------------------------------------------------------------------- |
| announce_ip         | Set to your HASS IP to tell robots where to talk                                                               |
| listen_ip           | Should be fine as 0.0.0.0 but available to change if needed.  IP address the bumper server binds it's ports to |
| time_zone           | Set to your local timezone                                                                                     |
| debug_logs          | Enable debugging                                                                                               |
| disable_xmpp_server | If your robot only communicates via MQTT you might be able to disable this                                     |
| disable_mqtt_server | If your robot only communicates via XMPP you can probably disable this                                         |

Ports need to be left to defaults for robot to find server, explained in the docs below.  Though if MQTT or XMPP is disabled you can clear those ports to free them up.  DNS forwarding needs to be setup on your network explained in the docs below.

## Bumper Documentation and Getting Started
See the documentation on [Read the Docs](https://bumper.readthedocs.io)

## Compatibility
As work to reverse the protocols and provide a self-hosted central server is still in progress, Bumper has had limited testing.  There are a number of EcoVacs models that it hasn't been tested against.  Bumper should be compatible with most wifi-enabled robots that use either the Ecovacs Android/iOS app or the Ecovacs Home Android/iOS app, but has only been reported to work on the below:

| Model           | Protocol Used | Bumper Version Tested | EcoVacs App Tested   |
| --------------- | ------------- | --------------------- | -------------------- |
| Deebot 900/901  | MQTT          | master                | Ecovacs/Ecovacs Home |
| Deebot 600      | MQTT          | master                | Ecovacs Home         |
| Deebot Ozmo 950 | MQTT          | master                | Ecovacs Home         |
| Deebot Ozmo 601 | XMPP          | master                | Ecovacs              |
| Deebot Ozmo 930 | XMPP          | master                | Ecovacs              |
| Deebot M81 Pro  | XMPP          | v0.1.0                | Ecovacs              |