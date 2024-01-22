question = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ")
question_change = question.lower().replace(" ", "")
if question_change == "42" or question_change == "forty-two" or question == "forty two" or question == "FoRty TwO":
    print("yes")
else:
    print("no")