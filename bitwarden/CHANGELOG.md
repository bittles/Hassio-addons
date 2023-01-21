## v0.19.0.6
- Add ingress proxy param setting

## v0.19.0.5
- Increase verbosity of ingress error log

## v0.19.0.4
- Separate nginx servers for ingress and direct access

## v0.19.0.3
- Fix port mapping

## v0.19.0.2
- Fix typo, give ingress a panel icon

## v0.19.0.1
- Bump base image, use variables for iterface and ingress port to fix ingress

## v0.18.0.6
- Forgot nginx wont make logs if they dont already exist

## v0.18.0.5
- I hate nginx format, fixing logs

## v0.18.0.4
- Add logging see where ingress is failing remotely, probably double reverse proxy

## v0.18.0.3
- Fix nginx upstream servers

## v0.18.0.2
- Fix startup dependency

## v0.18.0.1
- Restructure nginx setup so ingress works remotely

## v0.18.0
- First working version working as addon but no documentation changes, ingress not working correctly remotely