import getpass
import socket
import os

from CommandsList import *

class bcolors:
	HEADER = '\033[95m'
	OKBLUE = '\033[94m'
	OKGREEN = '\033[92m'
	WARNING = '\033[93m'
	FAIL = '\033[91m'
	ENDC = '\033[0m'
	BOLD = '\033[1m'
	UNDERLINE = '\033[4m'

class PyTermUI(object):
	"""docstring for PyTermUI"""
	def __init__(self):
		pass
		
	def preText(self):
		userName = getpass.getuser()
		computerName = socket.gethostname()
		currentDir = os.path.dirname(os.path.abspath(__file__))
		return "\r(PyTerm)" + userName +"@" + computerName +":" + currentDir.replace("/home/" + userName, "~") + "$"

	def check(self,commandList):
		isFirst = True
		for text in commandList:
			if isFirst:
				print self.preText(),

			if commands.find(text):
				print bcolors.BOLD + bcolors.OKGREEN + text + bcolors.ENDC,
			else:
				if isFirst:
					print bcolors.BOLD + bcolors.FAIL + text + bcolors.ENDC,
				else:
					print text,

			isFirst = False


pyTermUI = PyTermUI()