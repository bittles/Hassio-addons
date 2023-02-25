# 0.33
- Fix config

# 0.3
- Add configurable options for 2 cams
- Issues:
    - Currently have to fill out options for both cams, need to add checks if option is blank
    - Only two cams configurable atm, need to come up with loops to make it expandable

# 0.2
- Add gstreamer 1.22 new features:
	- Add add-reference-timestamp-meta=true property to rtspsrc
	- Add h264timestamper to pipeline
- Make both hi and lo pipelines the same, respectively, for each camera (no actual effect but just for parity)

# 0.1
- Initial
