
def circleOfChainedWords(words:list()):
    
    for i in range(len(words)-1):
        currentWord=words[i];
        nextWord=words[i+1];
        if currentWord[-1]!=nextWord[0]:
            return False;
    firstWord=words[0];
    endWord=words[-1];
    if firstWord[0]==endWord[-1]:
        return True;
    return False;

def makeCircleWords(word:list()):
    pass;
if __name__=="__main__":
    print(circleOfChainedWords(['apple', 'eggs',\
        'snack', 'karat', 'tuna']));
