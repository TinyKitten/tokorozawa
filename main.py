# coding:utf-8
import random
import sys
from urllib.parse import urlparse

import mysql.connector

url = urlparse('mysql://root@localhost:3306/stationapi')

conn = mysql.connector.connect(
    host=url.hostname or 'localhost',
    port=url.port or 3306,
    user=url.username or 'root',
    password=url.password or 'password',
    database=url.path[1:],
    auth_plugin='mysql_native_password'
)

if conn.is_connected() == False:
    print("Database connection failed! Please check the credential!")
    sys.exit()

# トンキン都
PREF_ID = 13

stations_select_query = "SELECT station_g_cd, station_name FROM stations WHERE pref_cd = {} GROUP BY station_g_cd, station_name".format(
    PREF_ID)

cursor = conn.cursor()
try:
    cursor.execute(stations_select_query)
    stations = cursor.fetchall()
    index = random.randrange(cursor.rowcount)
    print(stations[index][1])

except Exception as e:
    conn.rollback()
    raise e
finally:
    cursor.close()

conn.close()
