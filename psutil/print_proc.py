#!/usr/bin/python
import psutil,datetime
#p = psutil.cpu_times()
#p = psutil.cpu_count()
#p = psutil.cpu_stats()
#p = datetime.datetime.fromtimestamp(psutil.boot_time()).strftime("%Y-%m-%d %H:%M:%S")
#p = psutil.pids()
for proc in psutil.process_iter():
	try:
		pinfo = proc.as_dict(attrs = ['pid','name'])
		print(pinfo)
	except psutil.NoSuchProcess:
		pass
#	else:
#		print(pinfo)
