# connect to our router via SSH using module Netmiko

import json
import re
from netmiko import ConnectHandler

from MacAmb.models import Mac

router_mikrotik = {
    'device_type': 'mikrotik_routeros',
    'host':   '10.120.10.62',
    'username': 'lenovo',
    'password': 'Dgjl0864',
    'port': 22          # optional, defaults to 22
    # 'secret': 'secret',     # optional, defaults to ''
}

""" 'use_keys': True,
    'key_file': '/Users/mankomalsingh/.ssh/id_rsa', """

patron_mac = re.compile(
    r'"([0-9A-Fa-f]{2}:[0-9A-Fa-f]{2}:[0-9A-Fa-f]{2}:[0-9A-Fa-f]{2}:[0-9A-Fa-f]{2}:[0-9A-Fa-f]{2})\"')
patron_name = re.compile(r';;;(.*?)\n', re.DOTALL)


def conectar(comando):
    net_connect = ConnectHandler(**router_mikrotik)
    output = net_connect.send_command(comando)
    return output


def listarMacs():

    comando = '/user-manager user print'
    output = conectar(comando)

    macs = patron_mac.findall(output)
    name = patron_name.findall(output)
    arrayMac = []

    for i in range(len(macs)):
        if (len(macs) != len(name)):
            mac = Mac.objects.create(mac=macs[i])
        else:
            mac = Mac.objects.create(mac=macs[i], nombre=name[i])
        arrayMac.append(mac)

    return arrayMac


def agregarMac(mac, nombre, comentario):
    mac = Mac.objects.create(mac=mac, nombre=nombre, comentario=comentario)
    comando = '/user-manager user add name=' + \
        mac.mac.__str__() + ' comment=' + mac.nombre
    conectar(comando)
    return mac
