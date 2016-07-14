from app import app
from app import common
from flask.ext.mysql import MySQL
from MySQLdb.cursors import DictCursor

mysql = MySQL(autocommit=True, cursorclass=DictCursor)

# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = common.load('mysql_user')
app.config['MYSQL_DATABASE_PASSWORD'] = common.load('mysql_password')
app.config['MYSQL_DATABASE_DB'] = 'clasificador'
app.config['MYSQL_DATABASE_HOST'] = common.load('mysql_host')
app.config['MYSQL_DATABASE_PORT'] = int(common.load('mysql_port'))

mysql.init_app(app)

conn = mysql.connect()
