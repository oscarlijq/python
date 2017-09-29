#!/usr/bin/python
import psutil,datetime
for proc in psutil.process_iter():
	try:
		pinfo = proc.as_dict(attrs = ['pid','name'])
		p = psutil.Process(pinfo['pid'])
		if p.status() == 'zombie':
			print("zombie process: " + str(pinfo['pid']) + "  " + p.name() + "  " + p.status())
		else:
			print("health process: " + str(pinfo['pid']) + "  " + p.name() + "  " + p.status())
	except psutil.NoSuchProcess:
		pass
