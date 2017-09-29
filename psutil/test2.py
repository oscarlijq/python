#!/usr/bin/python
import psutil
def on_terminate(proc):
	print("process {} terminated with exit code {}".format(proc, proc.returncode))
procs = psutil.Process().children()
for p in procs:
	p.terminate()
	print(p.terminate())
