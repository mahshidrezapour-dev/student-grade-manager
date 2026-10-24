# پروژه پنجم
# سیستم مدیریت نمرات


def scores(name=None):
    if name is None:

        name = input("fisrt and land name of student : ")
    score = float(input("score of student : "))
    grade = int(input("student's class grade :"))
    student = {
        "name": name,
        "score": score,
        "grade": grade
    }
    return student


all_students = {}
x = int(input("enter the count of students >>>"))

for i in range(x):
    system = scores()
    all_students[system["name"]] = system
# menue
while True:
    search = input("search here >>>")
    # average
    if search.lower() == "average score":
        total = 0
        for student in all_students:
            total = total + all_students[student]["score"]
        average = total / len(all_students)
        print(average)
    # top score
    elif search.lower() == "top":
        all_scores = []

        for student in all_students:
            all_scores.append(all_students[student]["score"])
        top = max(all_scores)
        for student in all_students:
            if all_students[student]["score"] == top:
                print(all_students[student]["name"])
        print(top)
# lowest score
    elif search.lower() == "lowest":
        all_scores = []
        for student in all_students:
            all_scores.append(all_students[student]["score"])
        lowest = min(all_scores)
        for student in all_students:
            if all_students[student]["score"] == lowest:
                print(all_students[student]["name"])
        print(lowest)

    # update score
    elif search.lower() == "update score":
        name = input("which student's score do you want to update? ")
        if name in all_students:
            all_students[name]["score"] = float(input("enter new score:"))
            print(all_students[name])
        else:
            print("Not Found")

    elif search.lower() == "look up":
        # search
        name = input("who are you searching for? >>>")
        if name in all_students:
            print(all_students[name])
        else:
            print("no student with this name in this school")
# add
    elif search.lower() == "add":
        ask = input("enter the name of new student : ")
        if ask in all_students:
            print("this student already exists in our system")
        else:
            system = scores(ask)
            all_students[system["name"]] = system
# show all
    elif search.lower() == "show all":
        print(all_students)

# exit
    elif search.lower() == "exit":
        break
    else:
        print("Not Found")
