from flask import Flask, render_template
from flaskext.mysql import MySQL


app = Flask(__name__)



mysql = MySQL()
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = ''
app.config['MYSQL_DATABASE_DB'] = 'python_monitoring'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)



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

if __name__ == "__main__":
  app.run(debug=True)