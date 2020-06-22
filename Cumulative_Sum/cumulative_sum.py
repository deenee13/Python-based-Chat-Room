import sys


def cumulative_sum(num):
    empty_list = []
    length = len(num)
    temp = 0
    print("length of the list:", length)
    for i in range(0, length):
        temp = temp + num[i]
        empty_list.append(temp)
        # print(i)
    return(empty_list)


# Program2
num = [10, 2, 3]
new_list = cumulative_sum(num)
print('List with Cumulative Sum', new_list)
# cumulative_sum_user_input()
