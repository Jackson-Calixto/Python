from datetime import datetime

class LogLine(object):
	def __init__(self, line):		
		log_parts = line.split(' ', 6)
		self.isodate = datetime.strptime(log_parts[0] + ' ' + log_parts[1] + ' ' + log_parts[2] + ' ' + log_parts[3], '%b %d %H:%M:%S %Y').isoformat()
		self.name = log_parts[4]
		self.process = log_parts[5]
		self.description = log_parts[6]

	def __str__(self):
		return f"LogLine: {self.isodate} {self.name} {self.process} {self.description}"

with open('sys.log') as f:
	for line in f:
		log_line = LogLine(line)
		print(log_line)