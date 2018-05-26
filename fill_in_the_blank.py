def for_incorrect_answer():
    # For an incorrect answer itwill work and print your answer is incorrect.
    print "Your answer is incorrect!"


def my_python_project(game_level):
# the main roll of this function is to check the answer from the user and the answer given by the admin is correct if yess then loop go again for second question
# It also helps in getting the ans value by replacing space[i] with given_answers[i]
# If ans is right it will print ans is right if not then invalid ans.
# also replacing the value in the qusetion with the answer value if it is true.
    line = game_level[0]
    space = game_level[1]
    given_answers = game_level[2]
    count_length = len(space)
    for count in range(count_length):
        print line
        ans = ""
        while ans != given_answers[count]:
            ans = ques("What is your ans: " + space[count] + ": ")
# it helps in checking answer
            if ans != given_answers[count]:
                for_incorrect_answer()                               
        line = line.replace(space[count], given_answers[count])
        print "You are right! The Answer is:" + given_answers[count] + "' !\n"
    print line
    
easy = ["What is full form of HTML ___1___\n" +
        "What is full form of css ___2___ \n" +
        " What is full form of js ___3___\n" +
        " What is python called____4___\n",
        ["___1___", "___2___", "___3___", "____4___"],
        ["hypertext markup language", "cascading style sheets", "javascript", "programing language"]]

medium = ["For what purpose css is used ___1___\n " +
         "what purpose is html used:___2___\n" +
         " What you would prefer css or html for design :___3___\n" +
         " What is p tag used for : ___4____\n",
         ["___1___","___2___","___3___","___4____"],
         ["design", "framing", "css", "paragraph"]]


hard = ["What is h1 tag use for : ___1___\n " +
         "What is use of marque tag : __2__\n" +
         " Which tag is used for next line :___3___\n" +
         " What tag is use for highlighting any word ___4____\n",
         ["___1___","__2__","___3___","___4____"],
         ["heading", "moving sentence", "br tag", "Strong tag"]]


def chosse_level(level):
# It helps in checking that it is matching or not. == means check that it is equal or not if yes thn return statement will work if not then it moves to next statement.
    if level == "easy":
        return easy
    
    elif level == "medium":
        return medium
    
    elif level == "hard":
        return hard
    
    else:
        return 0





def ques(ques1):
# This function is for proper working of the my_python_project(game_level).
    return raw_input(ques1)



game_level = 0

while game_level == 0:
    level = raw_input("Select a level Easy , Medium or Hard: ")
    game_level = chosse_level(str.lower(level))

#Calling this function to start this according to the level chossen
my_python_project(game_level)
