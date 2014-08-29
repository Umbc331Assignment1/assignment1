##Matt Henry
import re
charref = re.compile("[aeiouy]+",re.I)
areletters = re.compile("[a-z]+",re.I)
arenotletters = re.compile("\W+")
charinverse = re.compile("[bcdfghjklmnpqrstvwxz]+",re.I)
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
	#TODO: then if they are letters
	#then if theres any non-vowels "charinverse.search(datum)"
	def checkthreechar(self, datum):
		if (len(datum) == 3) and not charinverse.search(datum):
			print "Debug: Hit three char for: " , datum
			return True
		return False

	#Should be finished
	def checkLE(self, datum):
		if ((datum[0] == 'l' or datum[0] == 'L') and (datum[-1] == 'e' or datum[-1] == 'E'):
			print "Debug: Hit checkLE for: ", datum
			return True
		return False

	#Not sure this is even needed
	#instructions say only check if the prime critria is reached
	#so the item would be already included?
	def check4to9long(self, datum):
		pass
###############################################
	##Checker helper



###########################################
	def lexoSort(self):
		#sorts self.remeberthese
		print self.remeberthese



##TODO Make read from command line argument?
#x = Rememberer("testfile.txt")


###reg expresion crap
#if ( not charinverse.search("eta")):
#	print "yes"

if arenotletters.search("1234"):
	print "has non letters"


