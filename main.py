import sys

from attendance import Attendance

if __name__ == "__main__":
    max_miss_allowed = 4
    try:
        total_classes = int(sys.argv[1])
        print("Total Number of Classes are {}".format(total_classes))
    except IndexError:
        print("'total classes' argument is required")
    except Exception as e:
        print(e)
    else:
        attendance = Attendance(total_classes, max_miss_allowed)
        answer_1 = attendance.calculate_ways_to_attend_classes()
        answer_2 = attendance.calculate_ways_to_miss_grad_day()
        print(f'{answer_2}/{answer_1}')
