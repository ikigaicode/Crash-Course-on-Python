# Using the "split" string method from the preceding lesson,
# complete the get_word function to return the {n}th word from
# a passed sentence.
# For example, get_word("This is a lesson about lists", 4)
# should return "lesson", which is the 4th word in this sentence.
# Hint: remember that list indexes start at 0, not 1. 

def student_grade(name, grade):
    return "{nombre} received {grado}% on the exam".format(nombre=name, grado=grade)

print(student_grade("Reed", 80))
print(student_grade("Paige", 92))
print(student_grade("Jesse", 85))
