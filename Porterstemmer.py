class Porter_Stemmer:
    m: int
    rm_Suffxs = {     
        1 : {"sses":"ss","ies":"i","ss":"ss","s":""},
        2 : {"eed":"ee","ed":"","ing":""},
        3 : {"y":"i"},
        4 : {"ational":"ate","tional":"tion","izer":"ize","fulness":"ful"},
        5 : {"icate":"ic","ness":"","ful":""},
        6 : {"ance":"","ence":"","ment":"","able":"","ible":"","ion":""},
        7 : {"e":"", "ll":"l"}
    }
    
    
    def __init__(self, word: str) -> None:
        self.word: str = word.lower()
        self.measure()
        
    def getCVSeq(self) -> str:
        return ''.join(['v' if letter in "aeiou" else 'c' for letter in word])
        
    def measure(self) -> None:
	    self.m = self.getCVSeq().count('vc')
	    
    def replce_Sfx(self, i: int):
        do_replce: bool
        
        if i == 6 or i == 7:
            if self.m > 1:
                do_replce = True
        elif i == 2:
            if self.word.find("eed") != -1 and self.m > 0:
                do_replce = True
            else:
                for sfx in self.rm_Suffxs[i]:
                ind = self.word.find(sfx)
                if ind != -1 :
                    new_word = "".join([self.word.split()[:ind], self.rm_Suffxs[i][sfx]])
                VCSeq
            
    
        for sfx in self.rm_Suffxs[i]:
            ind = self.word.find(sfx)
            if ind != -1 and do_replce:
                new_word = "".join([self.word.split()[:ind], self.rm_Suffxs[i][sfx]])

	def stemming(self) -> None:
	    if self.m > 0 or self.m >= 1 :
	        for i in rm_Suffxs:
	            
                    
	                    
	
if __name__ == "__main__":
    print(measure(input('Enter a word:')))
