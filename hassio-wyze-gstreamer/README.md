# HASS Addon for Wyze V3 cams with wz_mini_hacks using Gstreamer 1.22 (for arm64 only)
Gstreamer pipelines setup to only work with two cams for now.  Both cams and both resolution stream pipelines will try to launch so if you have less than one camera I wouldn't use this addon yet, and if you have more than two then you only get two for now.  Not sure yet how to make it configurable for number of cams without restructuring the s6 services.

Set cam1 and cam2 parameters from wz_mini_hacks. Then set ip, port and path for output (eg RTSP simple server). ie. rtsp://{rtsp_simple_server_ip}:{rtsp_simple_server_port}/{rtsp_simple_server_pathname}. 

## Addon Options
| Option                   | Description                                                                        |
| ------------------------ | ---------------------------------------------------------------------------------- |
| rtsp_simple_server_ip    | Set to ip address of your receiver (eg RTSP simple server)                         |
| rtsp_simple_server_port  | Port for your rtsp receiver 												        |
| cam1_ip                  | IP address of first camera                                                         |
| cam1_rtsp_port           | RTSP port of first camera                                                          |
| cam1_username            | RTSP username of first camera                                                      |
| cam1_password            | RTSP password of first camera                                                      |
| cam1_rtsp_ss_hi_res_path | This is the name of the path to send the high res stream of camera 1 (see below)   |
| cam1_rtsp_ss_lo_res_path | This is the name of the path to send the low res stream of camera 1 (see below)    |

Path example: rtsp://{rtsp_simple_server_ip}:{rtsp_simple_server_port}/{cam1_rtsp_ss_hi_res_path}
So if your rtsp simple server is at 192.168.1.50 and the rtsp port is 8554, and your path for your high res stream is 'yard_hi_res', gstreamer will output to rtsp://192.168.21.50:8554/yard_hi_res.

Repeat steps for cam2 options.

## Gstreamer pipelines
Opus used for audio codec.  Volume is boosted 1.5x since I didn't really find the default volume loud enough.  The slight 120 and 100 ms latency seemed to make streams nice and stable up to 1000 kb bitrate set in wz_mini.  With FFmpeg I was only able to get stable streams with the bitrate set to 500 kb.  Gstreamer also used less cpu and monitors and restarts itself versus FFmpeg.

### Gsreamer pipeline for hi res stream:
```
gst-launch-1.0 rtspsrc protocols=tcp \
location=rtsp://${CAM2_USERNAME}:${CAM2_PASSWORD}@${CAM2_IP}:${CAM2_RTSP_PORT}/video1_unicast \
latency=120 buffer-mode=3 connection-speed=2000 add-reference-timestamp-meta=true \
name=t t. ! queue ! \
capsfilter caps="application/x-rtp,media=video,height=1920,width=1080" ! \
queue ! rtph264depay ! h264parse ! h264timestamper ! queue ! \
rtspclientsink protocols=tcp latency=0 ntp-time-source=3 \
location=rtsp://${RTSP_SIMPLE_SERVER_IP}:${RTSP_SIMPLE_SERVER_PORT}/${CAM2_RTSP_SS_HI_RES_PATH} \
name=pay t. ! queue ! \
capsfilter caps="application/x-rtp,media=audio,clock-rate=16000,encoding-name=L16" ! \
rtpL16depay ! queue ! audioconvert ! queue ! \
audioresample ! audio/x-raw,channels=1,rate=16000 ! volume volume=1.5 ! \
opusenc bitrate=64000 \
packet-loss-percentage=50 inband-fec=true ! \
queue ! pay. -e
```

### Pipeline for lo res (similar but audio sample rate in wz_mini is lower):
```
gst-launch-1.0 rtspsrc protocols=tcp \
location=rtsp://${CAM2_USERNAME}:${CAM2_PASSWORD}@${CAM2_IP}:${CAM2_RTSP_PORT}/video2_unicast \
latency=100 buffer-mode=3 connection-speed=1000 add-reference-timestamp-meta=true \
name=t t. ! queue ! \
capsfilter caps="application/x-rtp,media=video,height=640,width=360" ! \
queue ! rtph264depay ! h264parse ! h264timestamper ! queue ! \
rtspclientsink protocols=tcp latency=0 ntp-time-source=3 \
location=rtsp://${RTSP_SIMPLE_SERVER_IP}:${RTSP_SIMPLE_SERVER_PORT}/${CAM2_RTSP_SS_LO_RES_PATH} \
name=pay t. ! queue ! \
capsfilter caps="application/x-rtp,media=audio,clock-rate=8000,encoding-name=L16" ! \
rtpL16depay ! queue ! audioconvert ! queue ! \
audioresample ! audio/x-raw,channels=1,rate=8000 ! volume volume=1.5 ! \
opusenc bitrate=64000 \
packet-loss-percentage=50 inband-fec=true ! \
queue ! pay. -e 
```