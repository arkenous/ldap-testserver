# ldap-testserver
[![Build Status](https://travis-ci.org/trileg/ldap-testserver.svg?branch=master)](https://travis-ci.org/trileg/ldap-testserver)
[![AMA](https://img.shields.io/badge/ask%20me-anything-0e7fc0.svg)](https://github.com/trileg/ama)

Docker image to build LDAP test server.

## Please change Manager password by below command
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
docker run -p 50389:389 -d --name container-ldap-testserver ldap-testserver
```
Host 50389 port <-> Container 389 port

#### Systemd service script sample
```
[Unit]
Description=LDAP authentication test service
Requires=docker.service
After=docker.service

[Service]
Type=simple
ExecStartPre=/usr/bin/docker stop container-ldap-testserver
ExecStartPre=/usr/bin/docker rm container-ldap-testserver
ExecStart=/usr/bin/docker run --name container-ldap-testserver -p 50389:389 ldap-testserver
ExecStop=/usr/bin/docker stop container-ldap-testserver

[Install]
WantedBy=multi-user.target
```

### DN
- Base DN: `dc=trileg,dc=net`
- User DN: `uid=charlotte,ou=People,dc=trileg,dc=net`

### User list
- uid=`charlotte`, password=`dunois`
- uid=`laura`, password=`bodewig`
- uid=`houki`, password=`shinonono`
- uid=`cecilia`, password=`alcott`
- uid=`lingyin`, password=`huang`
