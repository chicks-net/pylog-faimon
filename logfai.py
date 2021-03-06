#!/usr/bin/env python
"""python logging module for writing to FAI Project's faimond"""

import logging
import socket
import os

class FaimonHandler(logging.Handler):
	"""
	Log to FAImond across the network

	This is not based on SocketHandler because the other side doesn't want our pickles.
	"""

	DEFAULT_FAI_MONITOR_PORT = 4711


	def __init__(self, address=('localhost', DEFAULT_FAI_MONITOR_PORT)):
		"""
		Initialize a handler.
		"""
		#print 'FaimonHandler.__init__(address=' + str(address) + ')'

		self.hostname = address[0]
		self.port = address[1]
		super(FaimonHandler, self).__init__()

#	def close (self):
#		"""
#		Closes the socket.
#		"""
#		if self.unixsocket:
#			self.socket.close()
#		logging.Handler.close(self)

	def emit(self, record):
		"""
		Emit a record.

		Format the record and send it to the specified addressees.
		"""
		# format
		msg = self.format(record) + "\n"

		# send
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		sock.connect((self.hostname, self.port))
		sock.sendall(msg)
		sock.shutdown(socket.SHUT_WR)

		# dispose socket results
		while 1:
			data = sock.recv(1024)
			if data == "":
				break
			#print "Received:", repr(data)
		#print "Connection closed."
		sock.close()

if __name__ == '__main__':
	logger = logging.getLogger('faimon_test')
	logger.setLevel(logging.DEBUG)

	# STDOUT logging
	log_stdout = logging.StreamHandler()
	formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
	log_stdout.setFormatter(formatter)
	logger.addHandler(log_stdout)

	# FAIMON logging
	log_faimon = FaimonHandler(address=(os.environ['monserver'], 4711))
	fai_formatter = logging.Formatter('FAIMON: %(name)s - %(levelname)s - %(message)s')
	log_faimon.setFormatter(fai_formatter)
	logger.addHandler(log_faimon)

	logger.info('started')

	logger.warning('done')
