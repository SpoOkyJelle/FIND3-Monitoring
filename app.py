from flask import Flask, render_template
from flaskext.mysql import MySQL

import socket, math
import psutil

app = Flask(__name__)



mysql = MySQL()
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = ''
app.config['MYSQL_DATABASE_DB'] = 'python_monitoring'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)


def convert_size(size_bytes):
  if size_bytes == 0:
      return "0B"
  size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
  i = int(math.floor(math.log(size_bytes, 1024)))
  p = math.pow(1024, i)
  s = round(size_bytes / p, 2)
  
  return "%s %s" % (s, size_name[i])

@app.route("/")
def home():
  conn = mysql.connect()
  cursor = conn.cursor()

  cursor.execute("SELECT * FROM `raspberries`")
  data = cursor.fetchall()
  
  return render_template('dashboard.html', data=data)

@app.route("/database")
def database():
  conn = mysql.connect()  
  cursor = conn.cursor()

  cursor.execute("SELECT * FROM `raspberries`")
  data = cursor.fetchall()
  
  return render_template('database.html', data=data)

@app.route("/settings")
def settings():
  ipaddress = socket.gethostbyname(socket.gethostname())
  
  network_stats = psutil.net_io_counters(pernic=True)['Ethernet']
  bytes_sent = getattr(network_stats, 'bytes_sent')
  bytes_recv = getattr(network_stats, 'bytes_recv')
  
  
  return render_template('settings.html', ip=ipaddress, byte_sent=convert_size(bytes_sent), byte_recv=convert_size(bytes_recv))

if __name__ == "__main__":
  app.run(debug=True)