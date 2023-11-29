from ldap3 import Server, Connection, ALL

LDAP_URL = '10.40.10.10'

# Check user authentication in the LDAP and return his information


def get_LDAP_user(username, password):
    try:
        server = Server(LDAP_URL, get_info=ALL)
        connection = Connection(
            server=server, user='cn=Sistema,ou=Cuentas De Servicio,ou=Grupo Slots,dc=corp,dc=gruposlots', password='Zaq123edC', auto_bind=True)
        connection.search(
            search_base='ou=Grupo Slots,dc=corp,dc=gruposlots',
            search_filter='(&(objectClass=user)(objectCategory=person)(sAMAccountName=' +
            username.__str__() + '))',
        )

        uid = connection.response[0]['dn']
        autenticado = Connection(
            server=server, user=uid, password=password, auto_bind=True
        )

        print(autenticado)

        if len(connection.response) == 0 or not autenticado.bind():
            return None

        return autenticado
    except Exception as e:
        print(e)
        return None
