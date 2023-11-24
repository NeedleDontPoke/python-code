input_str = input()
input_list = input_str.split(' ', 1)
k = int(input_list[0])
s = input_list[1]
if 0 < k <= len(s):
    substring = s[:k]
    print(substring)
else:
    print("0<k<=len(s)")
