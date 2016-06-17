# ldap-testserver
[![Build Status](https://travis-ci.org/trileg/ldap-testserver.svg?branch=master)](https://travis-ci.org/trileg/ldap-testserver)
[![Docker Stars](https://img.shields.io/docker/stars/trileg/ldap-testserver.svg?maxAge=3600)](https://hub.docker.com/r/trileg/ldap-testserver/)
[![Docker Pulls](https://img.shields.io/docker/pulls/trileg/ldap-testserver.svg?maxAge=3600)](https://hub.docker.com/r/trileg/ldap-testserver/)
[![AMA](https://img.shields.io/badge/ask%20me-anything-0e7fc0.svg)](https://github.com/trileg/ama)
[![GitHub release](https://img.shields.io/github/release/trileg/ldap-testserver.svg?maxAge=86400)](https://github.com/trileg/ldap-testserver/releases/latest)
[![license](https://img.shields.io/github/license/trileg/ldap-testserver.svg?maxAge=2592000)](LICENSE)

Docker image to build LDAP test server.

# Please modify patches before building
- slapd.conf.patch1: suffix and rootdn
- ldap.conf.patch: BASE

# Please change Manager password by below command
`echo -n 'your preferred password' > latest/files/manager_pass.txt`
