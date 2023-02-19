## 0.6
- switch to hassio-debian base and s6overlay. image size down from ~2.8gb to 900mb
- config option importing next

## 0.5
- bump go2rtc to 1.2.0
- change snapshot interval from 10 to 30 min

## 0.4
- go2rtc to 1.1.2

## 0.3
- Change interval snapshot to rtsp instead of grabbing from websocket
- Use gstreamer to capture snapshot
- Set default snapshot to 10 min
- Bump go2rtc to 1.1.0
- Some dockfile optimizations and general cleanup

## 0.2
- Snapshot on an interval works, set to 5 minutes
- Custom interval steps created with options, not working currently

## 0.1
- First working version working as addon with gstreamer pipeline, no documentation
