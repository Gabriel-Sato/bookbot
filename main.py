with open("books/frankenstein.txt") as f:
    file_contents = f.read()
def main():
  #  printbook()
  #  countWords()
    countChar()

def printbook():  
    print(file_contents)
    
def countWords():
    words = file_contents.split() 
    print(len(words))
def countChar():
    import string
    alphabet = list(string.ascii_lowercase)
    lowerCase = file_contents.lower()
    teste = "teste abcde"
    print(alphabet)
main()