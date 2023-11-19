def test(param1, param2="hello", param3="byebye"):
    print("Test function: ", param1, " - ", param2, " - ", param3)


test("hello", param2="byebye", param3="end")


def list_max(input_list):
    max_value = input_list[0]

    for i in range(1, len(input_list)):
        if input_list[i] > max_value:
            max_value = input_list[i]

    return max_value


list1 = [-2, 1, 2, -10, 22, -10]
list1_max = list_max(list1)
print(list1_max)
