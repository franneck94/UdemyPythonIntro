import matplotlib.pyplot as plt


grades_jan = [56, 64, 78, 100]
grades_ben = [86, 94, 98, 90]


plt.plot(range(len(grades_jan)), grades_jan, color="blue")
plt.plot(range(len(grades_ben)), grades_ben, color="red")
plt.xlabel("Courses")
plt.ylabel("Grade (in %)")
plt.legend(["Jan", "Ben"])
plt.title("Jan vs. Ben")
plt.show()


plt.scatter(range(len(grades_jan)), grades_jan, c="blue")
plt.scatter(range(len(grades_ben)), grades_ben, c="red")
plt.xlabel("Courses")
plt.ylabel("Grade (in %)")
plt.legend(["Jan", "Ben"])
plt.title("Jan vs. Ben")
plt.show()
