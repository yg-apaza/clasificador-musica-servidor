from app import app
from flask.ext.mysql import MySQL
import os

mysql = MySQL()

# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = os.environ.get('MYSQL_USER', '')
app.config['MYSQL_DATABASE_PASSWORD'] = os.environ.get('MYSQL_PASSWORD', '')
app.config['MYSQL_DATABASE_DB'] = 'clasificador'
app.config['MYSQL_DATABASE_HOST'] = os.environ.get('OPENSHIFT_MYSQL_DB_HOST',
                                                   '')
app.config['MYSQL_DATABASE_PORT'] = int(os.environ.get(
                                                    'OPENSHIFT_MYSQL_DB_PORT',
                                                    ''))

print "---------------------------------here--------------------------------"
print os.environ.get('MYSQL_PASSWORD', '')

mysql.init_app(app)

conn = mysql.connect()
