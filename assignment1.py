##Matt Henry

class Rememberer:
	#def __init__(self):
	#	self.remeberthese = []
	def __init__(self,filename):
		self.remeberthese = []
		try:
			f = open(str(filename))
			s = f.read()
			self.parse(s)
		except Exception:
			print "Failed to open"	
			return
		self.lexoSort()
	
	def parse(self,the_file_as_string):
		templist = the_file_as_string.split(' ')
		for e in templist:
			if (self.checkprime(e)):
				self.remeberthese.append(e)
				continue
				#if (check4to9long(e)):
				#	pass
			if (self.checkthreechar(e)):
				self.remeberthese.append(e)
				continue
			if(self.checkLE(e)):
				self.remeberthese.append(e)
				continue
#############################################
	##Checkers
	##########TODO	
	#So check-ers should return booleans
	def checkprime(self, datum):
		return True

	def checkthreechar(self, datum):
		return True
	def checkLE(self, datum):
		return True

	#Not sure this is even needed
	#instructions say only check if the prime critria is reached
	#so the item would be already included?
	def check4to9long(self, datum):
		pass


###########################################
	def lexoSort(self):
		#sorts self.remeberthese
		print self.remeberthese



##TODO Make read from command line argument?
x = Rememberer("testfile.txt")
