##Matt Henry

class Rememberer:
    #def __init__(self):
    #    self.remeberthese = []
    def __init__(self,filename):
        #self.remeberthese = []  - using set to make it unique, sorting at the end
        self.remeberthese = set()
        try:
            f = open(str(filename))
            s = f.read()
            self.parse(s)
        except IOError as e:
            print "I/O error" + e 
            return
        self.lexoSort()
    
    def parse(self,the_file_as_string):
        templist = the_file_as_string.split(' ')
        for e in templist:
            if (self.checkprime(e)):
                self.remeberthese.add(e)
                continue
            if (self.check4to9long(e)):
                print "Should add the next value in the text"
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
    def checkprime(self, datum):
        return False
    
    #First checks if its 3 chars long "len(datum) == 3"
    #Then if all chars are vowels
    def checkthreechar(self, datum):
        #Should we strip the end of line character i.e. eee at end of line returns false
        #datum = datum.rstrip();
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
    #I think we use this to determine if we keep the next value after this one
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
        print "Final list (sorted):", sorted(self.remeberthese)
        print "Final list (unsorted):", self.remeberthese



##TODO Make read from command line argument?
x = Rememberer("./testfile.txt")