import datetime

#This is the my mystery function that will give a score to each string
def mystery_score(mystring):

    # z is the highest character we want - 
    totalScore = ord("z")
    charsum = 1
    for ch in mystring:
        charsum += ord(ch)

    return charsum/totalScore

if __name__ == "__main__":
    string= raw_input("What is the string you want to score? ")
    print "Your score for '" + string + "' is "+ str(mystery_score(string))
    
