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


def modificarEliminar(comando):
    net_connect = ConnectHandler(**router_mikrotik)
    net_connect.send_config_set(comando, cmd_verify=False)
    net_connect.save_config()


def listar(comando):
    net_connect = ConnectHandler(**router_mikrotik)
    output = net_connect.send_command(comando, cmd_verify=False)
    return output


def listarMacs():

    comando = '/user-manager user print'
    output = listar(comando)

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


def agregarMac(mac, nombre):
    comando = '/user-manager user add name=' + \
        mac.__str__() + ' comment="' + nombre+'"'
    print(comando.__str__())
    listar(comando.__str__())
    return mac


def modificarMac(macVieja, mac, nombre):
    comando = '/user-manager user set [find where name=' + \
        macVieja.__str__() + '] comment="' + nombre+'"' + ' name=' + mac.__str__()
    modificarEliminar(comando.__str__())
    return mac


def borrarMac(mac):
    comando = '/user-manager user remove [find where name=' + \
        mac.__str__() + ']'
    print(comando.__str__())
    modificarEliminar(comando.__str__())
    return mac
