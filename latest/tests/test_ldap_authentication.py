#!/usr/bin/env python
# -*- coding: utf-8 -*-

from ldap3 import Server, Connection, SIMPLE, SYNC, ALL
from nose.tools import eq_
import traceback


def test_ldap_authentication():
  eq_(True, ldap_auth())


def ldap_auth():
  user_dict = {'charlotte':'dunois', 'laura':'bodewig',
               'houki':'shinonono', 'cecilia':'alcott', 'lingyin':'huang'}
  server = 'localhost'
  port = 50389
  base_dn = 'ou=People,dc=k3n,dc=link'

  for k, v in user_dict.items():
    user_dn = 'uid='+k+','+base_dn
    s = Server(server, port=port, get_info=ALL)
    try:
      Connection(s, user=user_dn, password=v, auto_bind=True,
        authentication=SIMPLE, check_names=True)
    except:
      traceback.print_exc()
      return False

  return True

