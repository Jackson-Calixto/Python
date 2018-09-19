class Process(object):
	"""Inheritance"""
	def __init__(self):
		print('init Process')

	def process_function(self):
		return "process_function"

class Client(Process):
	"""Inherited class"""
	def __init__(self):
		print('init Client')

	def process_function(self):
		return "client_function"

class Server(Process):
	"""docstring for Server"""
	def __init__(self):
		print('init Server')

	def process_function(self):
		result = super(Server, self).process_function()
		return result + ", server_function"
		
class BackgroundProcess(Process):
	pass
		
p = Process()
c = Client()
s = Server()
b = BackgroundProcess()

processes = [p, c, s]
print()
for m in processes:
	print(m.process_function())