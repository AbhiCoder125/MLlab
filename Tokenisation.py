class Tokenization:
    stop_words : list[str] = [
            "a", "an", "the","i", "me", "my", "mine", "myself",
            "you", "your", "yours", "yourself", "yourselves",
            "he", "him", "his", "himself",
            "she", "her", "hers", "herself",
            "it", "its", "itself",
            "we", "us", "our", "ours", "ourselves",
            "they", "them", "their", "theirs", "themselves",
            "this", "that", "these", "those",
            "who", "whom", "whose", "which", "what","am", "is", "are", "was", "were",
            "be", "been", "being",
            "do", "does", "did",
            "have", "has", "had","can", "could", "may", "might",
            "shall", "should", "will", "would", "must","in", "on", "at", "by", "for", "with", "about",
            "against", "between", "into", "through",
            "during", "before", "after", "above", "below",
            "to", "from", "up", "down", "out", "off", "over", "under","and", "or", "but", "nor", "so", "yet",
            "because", "although", "though", "while",
            "if", "unless", "until", "since",
            "this", "that", "these", "those",
            "each", "every", "either", "neither",
            "some", "any", "no", "such","all", "both", "few", "many", "much",
            "several", "some", "any", "enough", "more", "most", "less", "least",
            "up", "down", "in", "out", "on", "off", "over", "under", "away",
            "not", "no", "nor", "never"
    ]
    
    sentence: str
    tokenList: list[str]
    charTokenList: list[list[str]]
    
    def __init__(self, sntnce: str) -> None:
        self.sentence = sntnce
        
    def word_Tokenization(self) -> None:
        self.tokenList = self.sentence.rstrip('.').split()
        
    def char_Tokenization(self) -> None:
        self.charTokenList = list(map(lambda x: list(x), self.tokenList))
    
    def remove_StopWords(self) -> None:
        newTokenList: list[str] = list(filter(lambda x: x.lower() not in self.stop_words,self.tokenList))
        self.tokenList = newTokenList
    
if __name__ == "__main__":
    sentence = input("Enter a sentence:")
    
    tkn: Tokenization = Tokenization(sentence)
    tkn.word_Tokenization()
    print(tkn.tokenList)
    tkn.char_Tokenization()
    print(tkn.charTokenList)
    tkn.remove_StopWords()
    print(tkn.tokenList)
