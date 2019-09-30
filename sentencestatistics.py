def main():
    sentence = input("Please enter a sentence: ")
    a = len(sentence)
    print("Number of characters:", a)
    s = len(sentence.split())
    print("Number of words:", s)
    average = a / s
    print("Average word length:", average)
    
    
main()
