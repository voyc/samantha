import configparser
import psycopg2
import json
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

def sortFreq(key):
	return freqtbl[key]['freq']

def sortLvl(key):
	return freqtbl[key]['lvl']

# open db
config = configparser.ConfigParser()
config.read('../../config.ini')
conn = psycopg2.connect(f"dbname={config['db']['name']} user={config['db']['user']} password={config['db']['password']} port={config['db']['port']}") 

# build freq table
freqtbl = {}
cur = conn.cursor()
id = 1
#cur.execute("SELECT words from mai.story where id = %s", (id,))
cur.execute("SELECT words from mai.story")
rows = cur.fetchall()
for row in rows:
	words = json.loads(row[0])
	for word in words:
		t = word['t']
		if len(t) > 0 and t != ' ':
			for loc in word['loc']:
				n = loc['n']
				if t in freqtbl:
					freqtbl[t] += 1
				else:
					freqtbl[t] = 1
				#if n > 0:
				#	print(f"{t} : {n} : {freqtbl[t]}")
cur.close()
conn.close()

# find low and high freq
lowfreq = 1
highfreq = 1
for key in freqtbl:
	freq = freqtbl[key]
	if freq < lowfreq:
		lowfreq = freq
	if freq > highfreq:
		highfreq = freq
#print(f'lowfreq:{lowfreq}, highfreq:{highfreq}')

# calc level for each word
for key in freqtbl:
	freq = freqtbl[key]
	level = 100 - int(((freq/(highfreq-lowfreq))*99))
	level = max(level,1)
	level = min(level,100)
	freqtbl[key] = {'freq':freq, 'lvl':level}

# print freq table
sorted = sorted(freqtbl, key=sortLvl, reverse=False)
#for key in sorted:
#	print(f'{key} : {freqtbl[key]}')
print(f'total words: {len(freqtbl)}')

# plot results
x = np.array([])
y = np.array([])
for key in sorted:
	x = np.append(x, freqtbl[key]['freq'])
	y = np.append(y, freqtbl[key]['lvl'])
plt.plot(y)
plt.savefig('plot.png')
