from .connection import BaseConnection
from .encoders.dummy import DummyEncoder
from .task import Task

class Client(BaseConnection):
	"""
	Creates a client for publishing tasks to
	to a RabbitMQ exchange
	"""
	encoder = DummyEncoder

	def submit_task(self, task):
		exchange = self.kwargs.get("exchange", "amq.direct")
		routing_key = task.name
		message = task.to_message()

		self.channel.basic.publish(message, exchange, routing_key)
