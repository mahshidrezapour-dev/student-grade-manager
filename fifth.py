# پروژه پنجم
# سیستم مدیریت نمرات


def scores(name=None):
    if name is None:
        name = input("first and last name of student : ").strip()
    else:
        name=name.strip()
    while not name:
        print("name cannot be empty")
        name=input("first and last name of student : ").strip()        
    while True:
        try:
            score = float(input("score of student : "))
            if 0<= score <=20:
                break
            else:
                print("Score must be between 0 and 20")
        except ValueError:
            print("please enter a valid number")
    while True:
        try:
            grade = int(input("student's class grade :"))
            if 10<= grade<=12:
                break
            else:
                print("Grade must be between 10 and 12 ( High school)")
        except ValueError:
            print("please enter a valid number")
    student = {
        "name": name,
        "score": score,
        "grade": grade
    }
    return student


all_students = {}
while True:
    try:
        x = int(input("enter the count of students >>>"))
        if x <0 :
            print("number of students cannot be negative")
        else:
            break
    except ValueError:
        print("please enter a valid integer")
for i in range(x):
    system = scores()
    while any(name.casefold()==system["name"].casefold() for name in all_students):
        #اینجا any() بررسی می‌کنه آیا حتی یک اسم در دیکشنری وجود داره که با اسم جدید، بدون درنظرگرفتن بزرگی و کوچکی حروف، برابر باشه یا نه.
        #متد casefold()  حروف رو برای مقایسه یکسان می‌کنه
        print("this student already exists in our system")
        system=scores()
    all_students[system["name"]] = system

print("Menu = average score , top , lowest , update score , look up , add , show all , exit")
while True:
    search = input("search here  >>> choose from Menu " )
    # average
    if search.lower() == "average score":
        if all_students:
            total = 0
            for student in all_students:
                total = total + all_students[student]["score"]
            average = total / len(all_students)
            print(average)
        else:
            print("no students have been registered")
    # top score
    elif search.lower() == "top":
        if all_students:
            all_scores = []
            for student in all_students:
                all_scores.append(all_students[student]["score"])
            top = max(all_scores)
            for student in all_students:
                if all_students[student]["score"] == top:
                    print(all_students[student]["name"])
            print(top)
        else:
            print("no students have been registered")
# lowest score
    elif search.lower() == "lowest":
        if all_students:
            all_scores = []
            for student in all_students:
                all_scores.append(all_students[student]["score"])
            lowest = min(all_scores)
            for student in all_students:
                if all_students[student]["score"] == lowest:
                    print(all_students[student]["name"])
            print(lowest)
        else:
            print("no students have been registered")

    # update score
    elif search.lower() == "update score":
        name = input("which student's score do you want to update? ").strip()
        student_name=None
        for student in all_students:
            if student.casefold()==name.casefold():
                student_name=student
                break
        if student_name is not None:         
            while True:
                try:
                    new_score=float(input("enter new score : "))
                    if 0<= new_score<=20:
                        all_students[student_name]["score"]=new_score
                        print(all_students[student_name])
                        break
                    else:
                        print("score must be between 0 and 20")
                except ValueError:
                    print("please enter a valid number")                
        else:
            print("Not Found")

    elif search.lower() == "look up":
        # search
        name = input("who are you searching for? >>>").strip()
        found=False
        for student in all_students.values():
            if student["name"].casefold()==name.casefold():
                print(student)
                found=True
                break
        if not found:
            print("no student with this name in this school")
# add
    elif search.lower() == "add":
        ask = input("enter the name of new student : ").strip()
        if any(name.casefold()==ask.casefold() for name in all_students):
            print("this student already exists in our system")
        else:
            system=scores(ask)
        #حلقهٔ دوم برای اینه که اگر کاربر بعد از رد شدن اسم تکراری، اسم دیگری وارد کرد، اون اسم هم بررسی بشه.
            while any(name.casefold()==system["name"].casefold() for name in all_students):  
                print("this student already exists in our system")
                system=scores()
            all_students[system["name"]] = system
# show all
    elif search.lower() == "show all":
        print(all_students)

# exit
    elif search.lower() == "exit":
        break
    else:
        print("Not Found")
