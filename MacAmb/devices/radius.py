# connect to our router via SSH using module Netmiko

import datetime
import re
from netmiko import ConnectHandler
from MacAmb.models import Mac

router_mikrotik = {
    'device_type': 'mikrotik_routeros',
    'host':   '10.11.20.238',
    'port': 22,
    'username': 'MACapp',
    'use_keys': True,
    'key_file': 'MacAmb/devices/keys/private.ppk',
}

patron_mac = re.compile(
    r'\b(?:[0-9A-Fa-f]{2}[:-]){5}[0-9A-Fa-f]{2}\b')
patron_name = re.compile(r';;;(.*?)\n', re.DOTALL)


def modificarEliminar(comando):
    net_connect = ConnectHandler(**router_mikrotik)
    net_connect.send_config_set(comando, cmd_verify=False)
    net_connect.save_config()
    net_connect.disconnect()


def listar(comando):
    net_connect = ConnectHandler(**router_mikrotik)
    output = net_connect.send_command(comando, cmd_verify=False)
    net_connect.disconnect()
    return output


def sincronizar():

    comando = '/user-manager user print without-paging'
    output = listar(comando)

    macs = patron_mac.findall(output)
    name = patron_name.findall(output)
    macBd = Mac.objects.all()
    arrayMac = []

    if (len(macBd) != len(macs)):
        for i in range(len(macs)):
            if (len(macBd) == 0 or macBd[i]not in macs):
                if (len(macs) != len(name)):
                    mac = Mac.objects.create(mac=macs[i])
                    Mac.objects.filter(id=mac.id).update(
                        comentario='luciano.echevarne', fecha_creacion=datetime.datetime.now())
                else:
                    mac = Mac.objects.create(mac=macs[i], nombre=name[i])
                    Mac.objects.filter(id=mac.id).update(
                        comentario='luciano.echevarne', fecha_creacion=datetime.datetime.now())
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
