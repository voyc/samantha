import configparser
import psycopg2
import sys

config = configparser.ConfigParser()
config.read('../../config.ini')

conn = psycopg2.connect(f"dbname={config['db']['name']} user={config['db']['user']} password={config['db']['password']} port={config['db']['port']}") 

for line in sys.stdin:
	t,e = line.strip().split(';')
	cur = conn.cursor()
	cur.execute("SELECT * from mai.dict d, mai.mean m where d.id = m.did and d.t = %s", (t,))
	rows = cur.fetchall()
	if cur.rowcount == 0:
		sys.stdout.write(line)
	cur.close()

conn.close()
