input_filename = r"C:\Users\new\Documents\Visual Studio 2010\Projects\Olympiads\Olympiads\biginteger_test.txt"
output_filename = r"C:\Users\new\Documents\Visual Studio 2010\Projects\Olympiads\Olympiads\biginteger_right_ans.txt"

if (input() != "1"):
    file = open(input_filename, mode = 'w')
    for i in range(100, 101):
        num1 = (761 ** 17000)
        num2 = (789 ** 17000)
        print(len(str(num1)), len(str(num2)))
        file.write(str(num1) + " " + str(num2) + "\n")
    print("Done!")
    file.close()
else:
    file = open(input_filename)
    result = open(output_filename, mode = 'w')
    for line in file:
        a, b = tuple(map(int, line.split()))
        #print(a, b)
        result.write(str(a * b) + "\n")
    print("Done!")

    file.close()
    result.close()
