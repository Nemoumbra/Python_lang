from fractions import Fraction
input_filename = r"rational_test.txt"
output_filename = r"rational_right_ans.txt"

if (input() != "1"):
    file = open(input_filename, mode = 'w')
    for i in range(100, 101):
        num1 = (25 ** 17)
        den1 = (79 ** 8)
        print(len(str(num1)), len(str(den1)))
        file.write(str(num1) + "/" + str(den1) + " ")
        num2 = (7 ** 15)
        den2 = (11 ** 9)
        print(len(str(num2)), len(str(den2)))
        file.write(str(num2) + "/" + str(den2) + "\n")
    print("Done!")
    file.close()
else:
    file = open(input_filename)
    result = open(output_filename, mode = 'w')
    for line in file:
        a, b = tuple([Fraction(s) for s in line.split()])
        #print(a, b)
        result.write(str(a + b) + "\n")
    print("Done!")

    file.close()
    result.close()
