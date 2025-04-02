student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86, 55, 91, 64, 89]
print(range(1, 10))

'''
COMPLETE THIS CHALLENGE WITHOUT USING max()
You are given a list of exam scores, and you have to print out the highest score from the List. You will need to use what you have learnt about Lists, For Loops and Conditionals to print out the highest score in the list of student_scores. For example, if the scores were:

8 65 89 86 55 91 64 89
Your code should print

91
'''

scores = [8,65,89,86,55,91,64,89]
high_score = 0
for score in scores:
    if score > high_score:
        high_score = score


print(high_score)