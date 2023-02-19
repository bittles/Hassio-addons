Based on [oischinger's eufyp2pstream addon](https://github.com/oischinger/eufyp2pstream).
# Goal and Progress:

## Goal
More stable experience in Homekit than Homebridge Eufy Security plugin.  Video skips frames, audio becomes unsynced.

More flexbility in RTSP url generation and manipulation for Eufy Doorbell using P2P stream.

Gstreamer pipeline.

If koush exposes two-way audio in Homekit in RTSP or FFmpeg cams I'll probably put talkback back in.

Working on transitioning to alpine with s6 startups on hassio addon base with amd64, armhf, and arm64 compatibility.  Having issues building gstreamer.

## Progress
As of version 0.2 gst-launch-1.0 pipelines can be built and used in the go2rtc config.  Camera name must be left as default 'camera1' for now.  TCP port 63336 is used for video, 63337 for audio, 63338 is just for talkback (I think).  Config file is stored in /config/eufyp2p/go2rtc.yaml.  Default config works for my Eufy 2k Battery Doorbell, encoding has to be set to Low (Medium looks like it may work).

Options for custom snapshot interval don't currently work.  FFmpeg subprocess creates snapshot every 5 minutes in /config/www/eufyp2p/camera1.jpg which can be pulled from Home Assistant with http://<hass.ip>:<hass.port>/local/eufyp2p/camera1.jpg snapshot url.  On-demand snapshot generation just didn't really provide a stable experience.

## Other Codec/Homekit Info
Low/medium encoding uses h264 for video and high uses h265.  Low quality is 640x480, high is 1600x1200.  Have mine set to low quality, low encoding for now to try to start streams faster.

My stream is fed to Scrypted RTSP cam, ondemand without Rebroadcast prebuffer.  Startup in Homekit seems to be affected more by where stream gets started in relation to keyframes (keyframe interval is 4 seconds).  If it gets started just before a keyframe it'll start in ~4-6 seconds.  If it starts just after a keyframe it'll start in 8-11 seconds.  Seems to be a by-product of no prebuffer.  

Swapped doorbell transformer from 16 V 10 VAC to 16 V 24 VAC and prebuffering stream in Scrypted isn't draining battery, but it's only been one day.  Prebuffering might break Eufy Security Addon push notifs though.  Motion not coming in now.  Need to dig into it some.

Below is info from oischinger's repo:

# EufyP2PStream

A small project that provides a Video/Audio Stream from Eufy cameras that don't directly support RTSP.

It uses [go2RTC](https://github.com/AlexxIT/go2rtc) to provide the live stream.

# Howto install

## Prerequisites
Install and configure the [Eufy Security Addon](https://github.com/fuatakgun/eufy_security_addon) first. See the instructions [here](https://github.com/fuatakgun/eufy_security).

## Install this addon
Copy this directory to `/addons/eufyp2pstream` on your Home Assistant host and [install the addon](https://my.home-assistant.io/redirect/supervisor_addon/?addon=local_eufyp2pstream).

Open the [Addon's WebUI](https://my.home-assistant.io/redirect/supervisor_ingress/?addon=local_eufyp2pstream) and enjoy a camera stream with audio via WEBRTC.

## Setting up a camera in Home Assistance

Go to devices and [setup a new generic camera](https://my.home-assistant.io/redirect/config_flow_start/?domain=generic) with the following parameters (replace `IP_ADDR` with your Home Assistant IP address):

- Static Image URL: `http://IP_ADDR:8787`
- Stream source: `rtsp://IP_ADDR:8541/camera1`

⚠️ I don't recommend using the Home Assistance camera integration at the moment since it seems to keep the Livestream ALWAYS active.

# References
This project is inspired by:

- [eufy_security Home Assistant Custom Component](https://github.com/fuatakgun/eufy_security)
- [go2RTC](https://github.com/AlexxIT/go2rtc)
- [Video Decoding in ioBroker.eusec](https://github.com/bropat/ioBroker.eusec/blob/0a15e1d125f4fd00144af66d57d8d738140ea619/src/lib/eufy-security/video.ts#L14-L65
)

# TODO

## Static Image:

A static image of the current stream can be obtained by heading to `http://IP_ADDR:8787`

## Talkback

To play an audio file start the P2P stream via the WebRTC URL and spin up an ffmpeg process like this:

`ffmpeg  -re -stream_loop -1 -i test.mp3 -vn -sn -dn -c:a aac  -b:a 20k -ar 16k -ac 2 -f adts tcp://127.0.0.1:63338`
