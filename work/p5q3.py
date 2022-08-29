def calc_average(total):
    return total / 2

def grade(score):
    if score >= 70 and score <= 100:
        return 'A'
    elif score >= 60 and score <= 69:
        return 'B'
    elif score >= 50 and score <= 59:
        return 'C'
    else:
        return 'F'

def valid(score):
    if score < 0 or score > 100:
        return False
    else:
        return True

def main():
    score1 = eval(input("Enter 1st score : "))
    while valid(score1) == False:
        print("Invalid score")
        score1 = eval(input("Enter 1st score : "))
    score2 = eval(input("Enter 2nd score : "))
    while valid(score2) == False:
        print("Invalid score")
        score2 = eval(input("Enter 2nd score : "))
    print("Grade for score 1 is ",grade(score1))
    print("Grade for score 2 is ",grade(score2))
    print("Average is",calc_average(score1 + score2))

main()

