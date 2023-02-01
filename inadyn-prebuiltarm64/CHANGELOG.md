## 2.10.0.2
- Fix startup checks if /share/inadyn-cache exists and symbolic linking with inadyn's cache

## 2.10.0.1
- Build addon from hassio-addon base
- Remove redunancies resulting from that
- Build inadyn from source (need to put this in Dockerfile to grab specific version instead of saving here)
- Remove some leftover build dependencies, cleanup and minimize image/backup size
- Store dns caches in /share/inadyn-cache to persist across addon uninstalls and able to move to other installs to cut down on dns provider polling