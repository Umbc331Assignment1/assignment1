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
		return False
	
	#First checks if its 3 chars long "len(datum) == 3"
	#Then if all chars are vowels
	def checkthreechar(self, datum):
		if ((len(datum) == 3) and (self.isvowel(datum))):
			print "Debug: Hit three char for: " , datum
			return True
		return False

	#Checks First and last Char's for being L and E respectivly 
	#Should be finished
	def checkLE(self, datum):
		if ((datum[0] == 'l' or datum[0] == 'L') and (datum[-1] == 'e' or datum[-1] == 'E')):
			print "Debug: Hit checkLE for: ", datum
			return True
		return False

	#Not sure this is even needed
	#instructions say only check if the prime critria is reached
	#so the item would be already included?
	def check4to9long(self, datum):
		return True
###############################################
	##Checker helper
	def isvowel(self, s):
		s = str(s) #just incase its a number
		letters = ['a','e','i','o','u','y']
		for e in s:
			if e not in letters:
				return False
		return True


###########################################
	def lexoSort(self):
		#sorts self.remeberthese
		print "Final list (unsorted):", self.remeberthese



##TODO Make read from command line argument?
x = Rememberer("testfile.txt")

