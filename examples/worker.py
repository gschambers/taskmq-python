import sys, os
sys.path.append(os.path.abspath(".."))

from haigha.connection import Connection
from lib.worker import Worker

conn = Connection()
worker = Worker(conn=conn)

def run_test(task):
	print "test message"

worker.bind("run_test", run_test)
worker.work()
