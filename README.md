# ldap-testserver
[![Build Status](https://travis-ci.org/trileg/ldap-testserver.svg?branch=master)](https://travis-ci.org/trileg/ldap-testserver)
[![Docker Stars](https://img.shields.io/docker/stars/trileg/ldap-testserver.svg?maxAge=3600)](https://hub.docker.com/r/trileg/ldap-testserver/)
[![Docker Pulls](https://img.shields.io/docker/pulls/trileg/ldap-testserver.svg?maxAge=3600)](https://hub.docker.com/r/trileg/ldap-testserver/)
[![AMA](https://img.shields.io/badge/ask%20me-anything-0e7fc0.svg)](https://github.com/trileg/ama)
[![GitHub release](https://img.shields.io/github/release/trileg/ldap-testserver.svg?maxAge=86400)](https://github.com/trileg/ldap-testserver/releases/latest)
[![license](https://img.shields.io/github/license/trileg/ldap-testserver.svg?maxAge=2592000)](LICENSE)

Docker image to build LDAP test server.

### Please modify domain name before building
- latest/Dockerfile
- latest/files/base.ldif
- latest/patches/ldap.conf.patch
- latest/patches/slapd.conf.patch1
- latest/patches/slapd.conf.patch2

### Please change Manager password by below command
```
echo -n 'your preferred password' > latest/files/manager_pass.txt
chmod 600 latest/files/manager_pass.txt
```

-----

## How to use this?
Build docker image using Dockerfile
```
docker build -t ldap-testserver latest/
```

Run docker container from builded image
```
docker run -p 50389:389 -d ldap-testserver
```
Host 50389 port <-> Container 389 port

####Systemd service script sample

<script src="https://gist.github.com/trileg/ce8106d8cd7a2b11d2dddf948c6798fd.js"></script>

### DN
- Base DN: `dc=trileg,dc=net`
- User DN: `uid=charlotte,ou=People,dc=trileg,dc=net`

### User list
- uid=`charlotte`, password=`dunois`
- uid=`laura`, password=`bodewig`
- uid=`houki`, password=`shinonono`
- uid=`cecilia`, password=`alcott`
- uid=`lingyin`, password=`huang`
