sentence = str.title(input("Enter a Sentence: "))

if "Nice" in sentence:
    new_sentence = str.replace(sentence,"Nice","Good")
    print("The new Sentence is: %s" %(new_sentence))

else:
    pass
