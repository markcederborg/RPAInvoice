import xmlrpc.client

url = 'https://virksomhedx.odoo.com'
db = 'virksomhedx'
username = 'mikkel4060@gmail.com'
password = 'fb16700a4ba9a32ff71c75afbb79c9fc368e99f8'


common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(url))
uid = common.authenticate(db, username, password, {})
print(common.version())
