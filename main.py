with open("books/frankenstein.txt") as f:
    file_contents = f.read()
def main():
    introduction()
  #  printbook()
    countWords()
    countChar()
def introduction():
    intro = f"Fun facts about {f.name}"
    print(intro)
def printbook():  
    print(file_contents)
    
def countWords():
    words = file_contents.split() 
    print(f'This book have {len(words)} words')
def countChar():
    import string
    alphabet = list(string.ascii_lowercase)
    lowerCase = file_contents.lower()
    for x in alphabet:
        print(f'The character {x} appeared {lowerCase.count(x)} times')    
main()