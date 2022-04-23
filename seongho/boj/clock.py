# 2082 백준
# H1,H2 hour inputs
# M1,M2 minute inputs
H1 = []
H2 = []
M1 = []
M2 = []
for i in range(5):
    h1, h2, m1, m2 = input().split()
    H1.append(h1)
    H2.append(h2)
    M1.append(m1)
    M2.append(m2)

# num0-num9 arrays in an array called numbers
line1 = "###  ..#  ###  ###  #.#  ###  ###  ###  ###  ###"
line2 = "#.#  ..#  ..#  ..#  #.#  #..  #..  ..#  #.#  #.#"
line3 = "#.#  ..#  ###  ###  ###  ###  ###  ..#  ###  ###"
line4 = "#.#  ..#  #..  ..#  ..#  ..#  #.#  ..#  #.#  ..#"
line5 = "###  ..#  ###  ###  ..#  ###  ###  ..#  ###  ###"
setting = [line1, line2, line3, line4, line5]
num0 = []
num1 = []
num2 = []
num3 = []
num4 = []
num5 = []
num6 = []
num7 = []
num8 = []
num9 = []
for i in setting:
    Num0, Num1, Num2, Num3, Num4, Num5, Num6, Num7, Num8, Num9 = i.split()
    num0.append(Num0)
    num1.append(Num1)
    num2.append(Num2)
    num3.append(Num3)
    num4.append(Num4)
    num5.append(Num5)
    num6.append(Num6)
    num7.append(Num7)
    num8.append(Num8)
    num9.append(Num9)

numbers = [num0, num1, num2, num3, num4, num5, num6, num7, num8, num9]

# compare one number with one clock letter, line by line
# only when number is "." and clock is "#", the clock cannot fit into the number.


def compare_letters(num, clock):
    for j in range(5):
        for i in range(3):
            if num[j][i] == "." and clock[j][i] == "#":
                return False
    else:
        return True

# search from number 0-9, and returns the first number that fits as string


def find_num(numbers, x):
    for i in range(10):
        if compare_letters(numbers[i], x):
            return str(i)


# following answer format (e.g. 23:35);
ans = []
ans.append(find_num(numbers, H1))
ans.append(find_num(numbers, H2))
ans.append(":")
ans.append(find_num(numbers, M1))
ans.append(find_num(numbers, M2))
answer = "".join(ans)
print(answer)
