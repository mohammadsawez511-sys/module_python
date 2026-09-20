def student_data(n):
    students = []

    for i in range(n):
        name = input("Enter the student name = ")
        students.append(name)

    return students



def calculate_trip_expenses(n):
    total = []

    for i in range(n):
        person, price = map(int, input("Enter person and price = ").split())
        total.append(person * price)

    return total



def greeting():
    print("THE BEKAR COLLEGE")