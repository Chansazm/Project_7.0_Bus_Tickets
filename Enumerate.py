lessons = ["Why Python Programming", "Data Types and Operators",
           "Control Flow", "Functions", "Scripting"]


def my_enumerate(iterable, start=0):
    # Implement your generator function here

    for i, lesson in my_enumerate(lessons, 1):
        print("Lesson {}: {}".format(i, lesson))
        if lessons == 10:
            break


my_enumerate(lessons)
