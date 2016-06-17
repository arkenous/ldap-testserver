## -*- docker-image-name: "trileg/ldap-testserver" -*-
FROM trileg/arch-base:latest
MAINTAINER Kensuke Kosaka <kosaka@trileg.net>

RUN pacman -Syu --noconfirm patch openldap &> /dev/null

COPY patches/slapd.conf.patch1 /tmp/slapd.conf.patch
RUN patch -u /etc/openldap/slapd.conf < /tmp/slapd.conf.patch && \
  rm -f /tmp/slapd.conf.patch

COPY files/manager_pass.txt /tmp/manager_pass.txt
RUN sed -i '/^rootpw/d' /etc/openldap/slapd.conf && \
  echo "rootpw $(slappasswd -T /tmp/manager_pass.txt)" >> /etc/openldap/slapd.conf && \
  rm -f /tmp/manager_pass.txt

RUN cp /etc/openldap/DB_CONFIG.example /var/lib/openldap/openldap-data/DB_CONFIG
RUN chown ldap:ldap /var/lib/openldap/openldap-data/DB_CONFIG

RUN rm -rf /etc/openldap/slapd.d/* && \
  slapd -u ldap -g ldap && \
  killall slapd && \
  slaptest -f /etc/openldap/slapd.conf -F /etc/openldap/slapd.d/ &> /dev/null && \
  slapindex &> /dev/null && \
  chown -R ldap:ldap /etc/openldap/slapd.d && \
  chown ldap:ldap /var/lib/openldap/openldap-data/*

# client
COPY patches/ldap.conf.patch /tmp/ldap.conf.patch
RUN patch -u /etc/openldap/ldap.conf < /tmp/ldap.conf.patch && \
  rm -f /tmp/ldap.conf.patch

# More securing ldap server
COPY patches/slapd.conf.patch2 /tmp/slapd.conf.patch
RUN patch -u /etc/openldap/slapd.conf < /tmp/slapd.conf.patch && \
  rm -f /tmp/slapd.conf.patch

RUN rm -rf /etc/openldap/slapd.d/* && \
  slapd -u ldap -g ldap && \
  killall slapd && \
  slaptest -f /etc/openldap/slapd.conf -F /etc/openldap/slapd.d/ &> /dev/null && \
  slapindex &> /dev/null && \
  chown -R ldap:ldap /etc/openldap/slapd.d && \
  chown ldap:ldap /var/lib/openldap/openldap-data/*

# Add base data to OpenLDAP tree
COPY files/base.ldif /tmp/base.ldif
COPY files/manager_pass.txt /tmp/manager_pass.txt
RUN slapd && \
  sleep 5s && \
  ldapadd -D "cn=Manager,dc=trileg,dc=net" -y /tmp/manager_pass.txt -f /tmp/base.ldif &> /dev/null && \
  rm -f /tmp/base.ldif && \
  rm -f /tmp/manager_pass.txt

