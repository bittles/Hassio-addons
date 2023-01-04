![License GPLv3](https://img.shields.io/github/license/bmartin5692/bumper.svg?color=brightgreen)

# Small fork from bmartin's great bumper

This is a small fork because my N79 would send XMPP payloads with errno='' which would then trigger error logging in bumper.  I just put a catch in to only create an error if errno is an actual number. If your debug logs are throwing errors and the errno is '' then this may help you.  

Build with:
```docker build -t bmartin5692/bumper:forked .```
and use the docker-compose.yaml in the example folder, make sure to put the announce IP address in there.

### 1/4/23:
Since I only have an N79 which uses XMPP I added environment variables to enable mqtt or xmpp, selectively, and seems to be working.  Massive amounts of mqtt pinging and attempting communication in the debug logs that aren't there now and make it a lot more readable.


# Bumper 

Bumper is a standalone and self-hosted implementation of the central server used by Ecovacs vacuum robots.  Bumper allows you to have full control of your Ecovacs robots, without the robots or app talking to the Ecovacs servers and transmitting data outside of your home.

![Bumper Diagram](./docs/images/BumperDiagram.png "Bumper Diagram")

**Note:** The current master branch is unstable, and in active development.

## Build Status

| Master Branch | Status                                                                 |
| ------------------- | ---------------------------------------------------------------------- |
| AppVeyor (Win32)    | [![AppVeyor branch](https://img.shields.io/appveyor/ci/bmartin5692/bumper/master?logo=appveyor)](https://ci.appveyor.com/project/bmartin5692/bumper/branch/master) |
| TravisCI (Linux)    | [![Travis (.org) branch](https://img.shields.io/travis/bmartin5692/bumper/master?logo=travis)](https://travis-ci.com/bmartin5692/bumper/branch/master) |
| Docker Hub	      | [![Docker Build](https://img.shields.io/docker/cloud/build/bmartin5692/bumper?logo=docker)](https://hub.docker.com/r/bmartin5692/bumper/branch/master) |
| CodeCov Coverage    | [![Codecov branch](https://img.shields.io/codecov/c/github/bmartin5692/bumper/master?logo=codecov)](https://codecov.io/gh/bmartin5692/bumper/branch/master) |


**Community**:
A Gitter community has been created for Bumper so users can chat and dig into issues outside of Github, join us here:
[![Gitter chat](https://badges.gitter.im/gitterHQ/gitter.png)](https://gitter.im/ecovacs-bumper/community)


***Testing needed***
Bumper needs users to assist with testing in order to ensure compatability as bumper moves forward!  If you've tested Bumper with your bot, please open an issue with details on success or issues.

***Please note**: this software is experimental and not ready for production use. Use at your own risk.* 

## Why?

For fun, mostly :)

But seriously, there are a several reasons for eliminating the central server:

1. Convenience: It works without an internet connection or if Ecovacs servers are down
2. Performance: No need for messages to travel to Ecovacs server and back.
3. Security: We can completely isolate the robot from the public Internet.
 
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

## Documentation and Getting Started

See the documentation on [Read the Docs](https://bumper.readthedocs.io)

---
### Thanks
A big thanks to the original project creator @torbjornaxelsson, without his work this project would have taken much longer to build. 

Bumper wouldn't exist without [Sucks](https://github.com/wpietri/sucks), an open source client for Ecovacs robots. Thanks to @wpietri and contributors!
