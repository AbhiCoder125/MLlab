def normalize(word: str) -> str:
    punc: list[str] = ['.',',','?',';','!','-',':','\'','\"']
    contrc = {
        "n't": {
            "aren't": "are not", "isn't": "is not", "wasn't": "was not",
            "weren't": "were not", "haven't": "have not", "hasn't": "has not",
            "hadn't": "had not", "don't": "do not", "doesn't": "does not",
            "didn't": "did not", "won't": "will not", "wouldn't": "would not",
            "can't": "cannot", "couldn't": "could not", "shouldn't": "should not",
            "mightn't": "might not", "mustn't": "must not", "needn't": "need not",
            "shan't": "shall not"
        },
        
        "'m": {
            "I'm": "I am"
        },
        
        "'re": {
            "you're": "you are",
            "we're": "we are",
            "they're": "they are"
        },
        
        "'s": {
            "he's": "he is",
            "she's": "she is",
            "it's": "it is"
        },
        
        "'ve": {
            "I've": "I have",
            "you've": "you have",
            "we've": "we have",
            "they've": "they have"
        },
        
        "'d": {
            "I'd": "I would",
            "you'd": "you would",
            "he'd": "he would",
            "she'd": "she would",
            "we'd": "we would",
            "they'd": "they would"
        },
        
        "'ll": {
            "I'll": "I will",
            "you'll": "you will",
            "he'll": "he will",
            "she'll": "she will",
            "we'll": "we will",
            "they'll": "they will"
        }
    }
    
    if word.isalpha() is False:
        old_word = word
        new_word = list(filter(lambda chr: chr not in punc, old_word.split()))
        word.replace(old_word,"".join(new_word))
        del old_word
        del new_word
        
        if '`' in word:
            
    elif word.isupper():
        word.lower()
    
    


def main() -> None:
    ...
