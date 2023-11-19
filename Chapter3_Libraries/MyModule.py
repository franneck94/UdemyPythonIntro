def list_max(input_list):
    max_value = input_list[0]

    for i in range(1, len(input_list)):
        if input_list[i] > max_value:
            max_value = input_list[i]

    print(max_value)


def list_min(input_list):
    max_value = input_list[0]

    for i in range(1, len(input_list)):
        if input_list[i] < max_value:
            max_value = input_list[i]

    print(max_value)


if __name__ == "__main__":
    print("Hello from MyModule")
