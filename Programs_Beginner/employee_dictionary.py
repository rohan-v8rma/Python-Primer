employees = {"rohan":{"age":16,"salary":1000},"soham":{"age":16, "salary":5000}}
for key in employees:
    new = employees[key]
    print(key.capitalize(),":")
    print("Age:",new["age"])
    print("Salary:",new["salary"])
