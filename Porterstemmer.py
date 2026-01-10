class Porter_Stemmer:
    stem_word: str = ""
    word: str
    m: int
    Suffixes: dict[str, str] = {     
        "sses":"ss","ies":"i","ss":"ss","s":"", # 1a
        "eed":"ee","ed":"","ing":"","y":"i", # 1b
        "ational":"ate","tional":"tion","izer":"ize","fulness":"ful", #2
        "icate":"ic","ness":"","ful":"", #3
        "ance":"","ence":"","ment":"","able":"","ible":"","ion":"", #4
        "e":"", "ll":"l", #5
    }
    
    def __init__(self, word: str) -> None:
        self.word = word.lower()
        self.stemming()
    
    def isreplacable(self,suffix: str) -> bool:
        do_replce: bool

        if self.word.endswith(suffix):
            self.measure()
            if suffix in ["ance","ence","ment","able","ible","ion","e","ll"]: # 4 and 5
                do_replce = True if self.m > 1 else False
            elif suffix in ["eed"]: #1b
                do_replce = True if self.m > 0 else False
            elif suffix in ["ed","ing"]: #1b
                VCSeq: str = self.getCVSeq(self.word[:self.word.find(suffix)])
                do_replce = True if VCSeq and VCSeq[-1] == 'v' else False
            else: # 1a,2,3
                do_replce = True if self.m > 0 else False
        else:
            do_replce = False
        return do_replce
    
    def stemming(self) -> None:
        for suffix, replacement in self.Suffixes.items():
            if self.isreplacable(suffix):
                self.stem_word: str = self.word[:self.word.find(suffix)] + replacement
                break
        
    def getCVSeq(self, word: str = "") -> str:
        if word == "":
            word = self.word
        return ''.join(['v' if letter in "aeiou" else 'c' for letter in word])
        
    def measure(self) -> None:
        self.m = self.getCVSeq().count('vc')
	
if __name__ == "__main__":
    words = ["caresses", "ponies", "ties", "caress", "cats",
    "feed", "agreed", "plastered", "bled", "motoring",
    "sing", "conflated", "troubled", "sized", "hopping",
    "tanned", "falling", "hissing", "fizzed", "failing",
    "filing", "happy", "sky", "relational", "conditional",
    "rational", "valenci", "hesitanci", "digitizer"
    ]

    for word in words:
        stem: Porter_Stemmer = Porter_Stemmer(word)
        print(f"The stem word for {stem.word} is {stem.stem_word}")
    
