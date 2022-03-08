def calc_average(s1, s2, s3, s4, s5):
    return (s1 + s2 + s3 + s4 + s5) / 5


def determine_grade(score):
    if 90 <= score <= 100: return 'A'
    if 80 <= score <= 89: return 'B'
    if 70 <= score <= 79: return 'C'
    if 60 <= score <= 69: return 'D'
    else:
        return 'F'


def main():
    score1 = int(input('Enter score 1: '))
    score2 = int(input('Enter score 2: '))
    score3 = int(input('Enter score 3: '))
    score4 = int(input('Enter score 4: '))
    score5 = int(input('Enter score 5: '))

    average = calc_average(score1, score2, score3, score4, score5)

    print('Score #1: {}, Grade: {}'.format(score1, determine_grade(score1)))
    print('Score #2: {}, Grade: {}'.format(score2, determine_grade(score2)))
    print('Score #3: {}, Grade: {}'.format(score3, determine_grade(score3)))
    print('Score #4: {}, Grade: {}'.format(score4, determine_grade(score4)))
    print('Score #5: {}, Grade: {}'.format(score5, determine_grade(score5)))
    print('Average Score: {:.1f}'.format(average))
    
while True:
 main()
     

 calculation=input('Enter "yes" if you would like to do another calculation:')
if calculation=='No'or 'no':
    print('Bye')
    exit()
   





