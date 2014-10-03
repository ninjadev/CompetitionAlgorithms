from sys import stdin

# strip() removes newline from the string

# parse one integer on the first line
n = int(stdin.readline().strip())

# parse a sequence of ints separated by space on the 2nd line
string_array = stdin.readline().strip().split(' ')
int_array = map(int, string_array)

# parse a string on the 3rd line
s = stdin.readline().strip()

# parse a float on the 4th line
f = float(stdin.readline().strip())

print '1st line contains number:', n
print '2nd line contains list of numbers (separated by space):', ' '.join(map(str, int_array))
print '3rd line contains string:', s
print '4th line contains float:', f
