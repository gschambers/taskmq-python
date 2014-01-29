import sys, os
sys.path.append(os.path.abspath(".."))

from haigha.connection import Connection
from lib.client import Client
from lib.task import Task

conn = Connection()
client = Client(conn=conn)

task = Task("run_test", "test message")
client.submit_task(task)
