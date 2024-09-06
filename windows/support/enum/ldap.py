from ldap3 import Server, Connection, ALL

# Konfigurasi server LDAP
ldap_server = 'ldap://support.htb'  # atau gunakan ldaps:// untuk koneksi SSL
ldap_user = 'ldap@support.htb'
ldap_password = 'nvEfEK16^1aM4$e7AclUf8x$tRWxPWO1%lmz'
base_dn = 'dc=support,dc=htb'

# Membuat koneksi ke server LDAP
server = Server(ldap_server, get_info=ALL)
conn = Connection(server, user=ldap_user, password=ldap_password, auto_bind=True)

# Melakukan pencarian LDAP
conn.search(base_dn, '(objectClass=*)', attributes=['*'])

# Menampilkan hasil pencarian
for entry in conn.entries:
    print(entry)

# Menutup koneksi
conn.unbind()
