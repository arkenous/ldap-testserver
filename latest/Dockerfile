## -*- docker-image-name: "trileg/ldap-testserver" -*-
FROM trileg/arch-base:latest
MAINTAINER Kensuke Kosaka <kosaka@trileg.net>

RUN pacman -Syu --noconfirm patch openldap &> /dev/null
COPY patches/slapd.conf.patch /tmp/slapd.conf.patch
RUN patch -u /etc/openldap/slapd.conf < /tmp/slapd.conf.patch && rm -f /tmp/slapd.conf.patch
RUN cp /etc/openldap/DB_CONFIG.example /var/lib/openldap/openldap-data/DB_CONFIG
RUN chown ldap:ldap /var/lib/openldap/openldap-data/DB_CONFIG
RUN rm -rf /etc/openldap/slapd.d/*
RUN /bin/sh -c "/usr/bin/slapd -u ldap -g ldap" && killall slapd
RUN slaptest -f /etc/openldap/slapd.conf -F /etc/openldap/slapd.d/ &> /dev/null
RUN chown -R ldap:ldap /etc/openldap/slapd.d
RUN slapindex &> /dev/null
RUN chown ldap:ldap /var/lib/openldap/openldap-data/*
#RUN /bin/sh -c "/usr/bin/slapd -u ldap -g ldap"

