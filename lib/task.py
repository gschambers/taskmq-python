from haigha.message import Message
from .encoders.dummy import DummyEncoder

class Task(object):
	"""
	Submits a task request via a RabbitMQ exchange
	"""
	def __init__(self, name=None, data=None, encoder=DummyEncoder):
		self.encoder = encoder
		self.name = name
		self.data = self.encoder.encode(data)

	def to_message(self):
		return Message(self.data)

	def from_message(self, routing_key, message):
		name = routing_key
		data = self.encoder.decode(message.body)
		
		self.name = name
		self.data = data
		