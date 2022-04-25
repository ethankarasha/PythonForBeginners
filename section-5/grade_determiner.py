grade = int(input("Please input the student's grade. "))


if grade >= 90:
    print("The student will receive an A")
else:
    if grade >= 80:
        print("The student will receive a B")
    else:
        if grade >= 70:
            print("The student will receive a C")
        else:
            if grade >= 60:
                print("The student will receive a D")
            else:
                print ("The student will receive an F")