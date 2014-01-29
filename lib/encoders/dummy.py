class DummyEncoder(object):
	"""
	No-op data encoder
	"""

	@classmethod
	def encode(cls, input):
		return input

	@classmethod
	def decode(cls, input):
		return input
