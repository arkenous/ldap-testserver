## -*- docker-image-name: "trileg/ldap-testserver" -*-
FROM trileg/arch-base:latest
MAINTAINER Kensuke Kosaka <k@trileg.net>

RUN pacman -Syu --noconfirm patch openldap &> /dev/null

COPY patches/slapd.conf.patch1 /tmp/slapd.conf.patch
RUN patch -u /etc/openldap/slapd.conf < /tmp/slapd.conf.patch && \
  rm -f /tmp/slapd.conf.patch

COPY files/manager_pass.txt /tmp/manager_pass.txt
RUN sed -i '/^rootpw/d' /etc/openldap/slapd.conf && \
  echo "rootpw $(slappasswd -T /tmp/manager_pass.txt)" >> /etc/openldap/slapd.conf && \
  rm -f /tmp/manager_pass.txt

RUN cp /etc/openldap/DB_CONFIG.example /var/lib/openldap/openldap-data/DB_CONFIG

RUN rm -rf /etc/openldap/slapd.d/* && \
  slapd && \
  sleep 5s && \
  killall slapd && \
  slaptest -f /etc/openldap/slapd.conf -F /etc/openldap/slapd.d/ &> /dev/null && \
  slapindex &> /dev/null

# client
COPY patches/ldap.conf.patch /tmp/ldap.conf.patch
RUN patch -u /etc/openldap/ldap.conf < /tmp/ldap.conf.patch && \
  rm -f /tmp/ldap.conf.patch

# More securing ldap server
COPY patches/slapd.conf.patch2 /tmp/slapd.conf.patch
RUN patch -u /etc/openldap/slapd.conf < /tmp/slapd.conf.patch && \
  rm -f /tmp/slapd.conf.patch

RUN rm -rf /etc/openldap/slapd.d/* && \
  slapd && \
  sleep 5s && \
  killall slapd && \
  slaptest -f /etc/openldap/slapd.conf -F /etc/openldap/slapd.d/ &> /dev/null && \
  slapindex &> /dev/null

# Add base data to OpenLDAP tree
COPY files/base.ldif /tmp/base.ldif
COPY files/manager_pass.txt /tmp/manager_pass.txt
RUN slapd && \
  sleep 5s && \
  ldapadd -D "cn=Manager,dc=trileg,dc=net" -y /tmp/manager_pass.txt -f /tmp/base.ldif &> /dev/null && \
  killall slapd && \
  rm -f /tmp/base.ldif && \
  rm -f /tmp/manager_pass.txt

# Add test users
COPY files/manager_pass.txt /tmp/manager_pass.txt
COPY files/Charlotte_Dunois.ldif /tmp/Charlotte_Dunois.ldif
COPY files/Laura_Bodewig.ldif /tmp/Laura_Bodewig.ldif
COPY files/Houki_Shinonono.ldif /tmp/Houki_Shinonono.ldif
COPY files/Cecilia_Alcott.ldif /tmp/Cecilia_Alcott.ldif
COPY files/Lingyin_Huang.ldif /tmp/Lingyin_Huang.ldif
RUN slapd && \
  sleep 5s && \
  ldapadd -D "cn=Manager,dc=trileg,dc=net" -y /tmp/manager_pass.txt -f /tmp/Charlotte_Dunois.ldif && \
  ldapadd -D "cn=Manager,dc=trileg,dc=net" -y /tmp/manager_pass.txt -f /tmp/Laura_Bodewig.ldif && \
  ldapadd -D "cn=Manager,dc=trileg,dc=net" -y /tmp/manager_pass.txt -f /tmp/Houki_Shinonono.ldif && \
  ldapadd -D "cn=Manager,dc=trileg,dc=net" -y /tmp/manager_pass.txt -f /tmp/Cecilia_Alcott.ldif && \
  ldapadd -D "cn=Manager,dc=trileg,dc=net" -y /tmp/manager_pass.txt -f /tmp/Lingyin_Huang.ldif && \
  rm -f /tmp/manager_pass.txt && \
  rm -f /tmp/Charlotte_Dunois.ldif && \
  rm -f /tmp/Laura_Bodewig.ldif && \
  rm -f /tmp/Houki_Shinonono.ldif && \
  rm -f /tmp/Cecilia_Alcott.ldif && \
  rm -f /tmp/Lingyin_Huang.ldif && \
  killall slapd

CMD ["/usr/sbin/slapd", "-d", "Config,Stats"]
