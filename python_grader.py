while True:
    pts = float(input("Total points possible: "))
    gained = float(input("Points gained: "))
    grade = round((gained / pts) * 100, 2)

    if grade >= 89:
        print("A")
        print("Amazing!")
    elif 76 <= grade <= 88.99:
        print("B")
        print("Great!")
    elif 61 <= grade <= 75.99:
        print("C")
        print("Super!")
    elif 51 <= grade <= 60.99:
        print("D")
        print("Good try!")
    elif grade < 51:
        print("F")
        print("...for failure.")
