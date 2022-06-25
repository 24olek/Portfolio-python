#Based on Michael Dawson book

def open_file(file_name, mode):
    try:
        the_file = open(file_name, mode)
    except:
        print("""There is no available data for \"Quiz\". Try to find data
on internet or create in DataEditor.""")
    else:
        return the_file

def read_line(the_file):
    line = the_file.readline()
    line = line.replace("/", "\n")
    return line

def next_block(the_file):
    category = read_line(the_file)
    question = read_line(the_file)
    anwsers = []
    for i in range(3):
        anwsers.append(read_line(the_file))

    correct = read_line(the_file)
    if correct:
        correct = correct[0]

    explanation = read_line(the_file)
    return category, question, anwsers, correct, explanation
    
def welcome(title):
    print("\t\t Welcome to \"Quiz\"!\n")
    print("\t\t", title, "\n ")


def main():
    import pickle
    nickname = input("What is your name?")
    quest_file = open_file("quiz.txt", "r")
    title = read_line(quest_file)
    score = 0
    category, question, anwsers, correct, explanation = next_block(quest_file)
    while category:
        print("Category: ", category)
        print("Next question is: ", question)
        for i in range(3):
            print("\t", i + 1, anwsers[i])
        anwser = input("What is your anwser? \n")
        if anwser == correct:
            print("Correct anwser.")
            score += 1
        else:
            print("Incorrect awser.")
        print(explanation)
        print("Score: ", score, "\n\n")
        category, question, anwsers, correct, explanation = next_block(quest_file)
    quest_file.close()
    print("This was last question.")
    print("Your score: ", score)
    open("scoresquiz.dat", "ab+")
    yourscore  = nickname + str(score)
    print(yourscore)
    
    

main()
    
input("To exit program, press enter")
