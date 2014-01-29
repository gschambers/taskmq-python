from haigha.connection import Connection

class BaseConnection(object):
	"""
	Establish or reuse connection to RabbitMQ server
	"""
	def __init__(self, **kwargs):
		properties = {
			"host": "localhost",
			"port": 5672,
			"user": "guest",
			"password": "guest",
			"vhost": "/",
			"heartbeat": None,
			"debug": False
		}

		self.kwargs = kwargs

		for key, value in kwargs.iteritems():
			if properties.has_key(key):
				properties[key] = value

		# Connection can be shared between multiple clients/workers
		conn = self.kwargs.get("conn", None)

		if conn is None:
			conn = Connection(**properties)

		self._conn = conn
		self.channel = conn.channel()
	
	def consume(self):
		self._conn.read_frames()
