import configparser
import psycopg2
import sys

config = configparser.ConfigParser()
config.read('../../sam.conf')

connectstring = f"host={config['db']['host']} dbname={config['db']['name']} user={config['db']['user']} password={config['db']['password']} port={config['db']['port']}" 
print(connectstring)
conn = psycopg2.connect(connectstring)

for line in sys.stdin:
	t,e = line.strip().split(';')
	cur = conn.cursor()
	cur.execute("SELECT * from mai.dict d, mai.mean m where d.id = m.did and d.t = %s", (t,))
	rows = cur.fetchall()
	if cur.rowcount == 0:
		sys.stdout.write(line)
	else:
		#sys.stdout.write(' '.join(rows))
		print(rows)
	cur.close()

conn.close()
