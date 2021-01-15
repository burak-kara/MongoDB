import cassandra as cc
#
# from cassandra.cluster import Cluster
# from cassandra.auth import PlainTextAuthProvider

cloud_config = {
    'secure_connect_bundle': 'D:\\projects\\CS550\PROJECT\\MongoDB\\secure-connect-cs550.zip'
}
auth_provider = cc.auth.PlainTextAuthProvider('burak', 'burakkara')
cluster = cc.cluster.Cluster(cloud=cloud_config, auth_provider=auth_provider)
session = cluster.connect()

row = session.execute("select release_version from system.local").one()
if row:
    print(row[0])
else:
    print("An error occurred.")
