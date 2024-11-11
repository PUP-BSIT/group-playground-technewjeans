#Technewjeans Quiz

print ("(James Michael) Question No. 1: Which of the following is the correct name of my orange tabby cat?\n")
choice_A = "A) Galaxy Annihilator"
choice_B = "B) All Knowing Sentient Being"
choice_C = "C) Loafy the Gato"
choice_D = "D) Piping the Orange\n"
score = 0
int_score = int(score)
print (choice_A) 
print (choice_B) 
print (choice_C) 
print (choice_D)

answer = input("Input your choice: ")

if answer == "C" or answer == "c":
    print ("\nMeowCorrect! Loafy the Gato is the name of my cat")
    print (f"Current Score: {int_score + 1}")
    int_score = 1
else:
    print ("\nIncorrect! The correct answer is C")


print ("\n(James Michael) Question No. 2: When did the Polytechnic University of the Philippines was founded?\n")
choice_A = "A) August 6, 1945"
choice_B = "B) October 19, 1904"
choice_C = "C) September 2, 1945"
choice_D = "D) October 21, 1600\n"

print (choice_A) 
print (choice_B) 
print (choice_C) 
print (choice_D)

answer = input("Input your choice: ")

if answer == "B" or answer == "b":
    
    print ("\nCorrect! PUP was founded in 1904 with the name of Manila Business School (MBS)")
    print (f"Current Score:  {int_score + 1}")
    int_score = 2
else:
    print ("\nIncorrect! The correct answer is B")