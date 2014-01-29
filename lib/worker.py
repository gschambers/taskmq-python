from haigha.message import Message
from .connection import BaseConnection
from .task import Task

class Worker(BaseConnection):
	"""
	Creates a worker (consumer) for receiving
	tasks from a RabbitMQ queue
	"""
	bindings = {}

	def __init__(self, *args, **kwargs):
		super(Worker, self).__init__(*args, **kwargs)
		
		self.queue = self.kwargs.get("queue", "tasks")
		self.exchange = self.kwargs.get("exchange", "amq.direct")

		self.channel.exchange.declare(self.exchange, "direct", durable=True)
		self.channel.queue.declare(self.queue, durable=True, auto_delete=False)
		self.channel.basic.qos(prefetch_count=1)

	def _handle_message(self, message):
		delivery_info = message.delivery_info
		task_name = delivery_info["routing_key"]

		task = Task()
		task.from_message(task_name, message)

		if self.bindings.has_key(task_name):
			for func in self.bindings[task_name]:
				func(task)

		self.channel.basic.ack(delivery_info["delivery_tag"])

	def bind(self, task_name, func):
		self.channel.queue.bind(self.queue, self.exchange, task_name)

		if not self.bindings.has_key(task_name):
			self.bindings[task_name] = []

		self.bindings[task_name].append(func)

	def work(self):
		self.channel.basic.consume(self.queue, self._handle_message, no_ack=False)

		while not self.channel.closed:
			self.consume()
