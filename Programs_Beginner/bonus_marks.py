def marks_input():
    while True:
        marks = float(input("What are your marks? --> "))
        if (marks > 100) or (marks <= 0):
            print("Enter appropriate Mark.\n")
        else:
            return marks
def class_type_input():
    class_type = "no"
    while class_type.upper() not in ['L', 'T']:
        class_type = str(input("\nTheory or Lab? \nEnter \'T\' for Theory and \'L\' for Lab >> "))
    return class_type.upper()        

while True:
    marks = marks_input()
    class_type = class_type_input()
    print("Your marks are ")
    if marks >= 80:
        if class_type == "T": marks *= 1.08
        elif class_type == "L": marks *= 1.06
    elif 80 > marks >= 60:
        if class_type == "T": marks *= 1.06
        elif class_type == "L": marks *= 1.04
    elif 60 > marks >= 40:
        if class_type == "T": marks *= 1.04
        elif class_type == "L": marks *= 1.02
    elif marks < 40:
        pass
    option = ''
    if marks > 100:
        marks = 100
    print(marks)
    while option not in ["Y","N"]:
        option = input("Do you want to continue? (Y/N) ").upper()
    if option == "N":
        break
    
        
