import json

class JSONEncoder(object):
	"""
	Serializes string to/from JSON
	"""

	@classmethod
	def encode(cls, input):
		return json.dumps(input)

	@classmethod
	def decode(cls, input):
		return json.loads(input)
