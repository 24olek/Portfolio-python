def editorQuiz():
    file = open("quiz.txt", "w")
    fooQuiz = ""
    print("""Welcome to "Quiz" editor.
To avoid losing content of current "Quiz" data, exit the program.

""")
    input("Press any key to continue. \n")
    file.write(input("Introduce the name of episode: "))
    file.write("\n")
    while fooQuiz != "2":
        fooQuiz = input("""1. Add a question.
2. Exit the editor.\n""")
        if fooQuiz == "1":
            file.write(input("Add category: "))
            file.write("\n")
            file.write(input("Add question: "))
            file.write("\n")
            file.write(input("Add an anwser number 1: "))
            file.write("\n")
            file.write(input("Add an anwser number 2: "))
            file.write("\n")
            file.write(input("Add an anwser number 3: "))
            file.write("\n")
            file.write(input("Indicate number of correct anwser: "))
            file.write("\n")
            file.write(input("Add an explenation of correct anwser: "))
            file.write("\n")
        
    file.close()

bar = ""
while bar != "exit":
    bar = input("""1. "Quiz" editor.
To exit editor, introduce "exit".
If you choose to edit data, every content of past content is lost.\n
""")
    if bar == "exit":
        break
    elif bar == "1":
        editorQuiz()
input()



    


               
    
