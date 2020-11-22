#!/usr/bin/env python3
# countthread.py

import threading
import time

class Eyes:
	def startThreads(self):
		t = threading.Thread(target=self.sleep5)
		t.start()
		t = threading.Thread(target=self.sleep3)
		t.start()

	def sleep5(self):
		while True:
			time.sleep(5)
			print('sleep5')

	def sleep3(self):
		while True:
			time.sleep(3)
			print('sleep3')

eyes = Eyes()
eyes.startThreads()
