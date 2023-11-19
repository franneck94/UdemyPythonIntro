input_filepath = "C:/Users/Jan/OneDrive/_Coding/UdemyPythonIntro/Chapter4_Intermediate/test.txt"  # noqa: E501
output_filepath = "C:/Users/Jan/OneDrive/_Coding/UdemyPythonIntro/Chapter4_Intermediate/test_out.txt"  # noqa: E501


with open(input_filepath) as file:
    content = file.readlines()


print(content)
content.append("Tom Tomerson\n")


with open(output_filepath, "w") as file:
    file.writelines(content)
