##CSMC 331
##Mr. Echlin
##Project 1
##Group Members: Matt Henry, Ryan Fischbach, Nick Harman

import traceback
import sys

class Rememberer:
	def __init__(self,filename):
		#self.remeberthese = []
		self.remeberthese = set()
		try:
			f = open(str(filename))
			s = f.read()
			self.parse(s)
		except Exception:
			print "Failed to open"
			traceback.print_exc()
			return
		self.lexoSort()
	
	def parse(self,the_file_as_string):
		templist = the_file_as_string.split(' ')
		saveNext = False
		for e in templist:
			if ( saveNext ):
				self.remeberthese.add(e)
			saveNext = self.check4to9long(e)
			if (self.checkprime(e)):
				self.remeberthese.add(e)
				continue
			if (self.checkthreechar(e)):
				self.remeberthese.add(e)
				continue
			if(self.checkLE(e)):
				self.remeberthese.add(e)
				continue
#############################################
	##Checkers
	##########TODO	
	#So check-ers should return booleans
	#Check if string is a number, then checks if it's a prime
	def checkprime(self, datum):
		if(self.isNumber(datum) and ((int(datum) < 10000) and (int(datum) > 1))):
        		i = int(datum)
        		for x in range(i):
            			if(x > 1):
                			if((i % x) == 0):
                    				return False
			return True
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
		try:
			intDatum = int(datum)
		except Exception:
			return False
		if ( len(datum) >= 4 and len(datum) <= 9 ):
			print "Debug: Hit num len for: ", datum
			return True
		return False
###############################################
	##Checker helper
	def isNumber(self, datum):
	    for i in datum:
        	try:
            		int(i)
        	except ValueError:
            		return False
    	    return True

	
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
		#print "Final list (unsorted):", self.remeberthese
		print "Final list (sorted):", sorted(self.remeberthese)



#Takes last argument on command line as filename
filename  = sys.argv[-1]
x = Rememberer(filename)
