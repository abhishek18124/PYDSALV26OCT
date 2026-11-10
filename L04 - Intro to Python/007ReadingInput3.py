# x = int(input())
# y = int(input())
# z = int(input())

# user_input = input()
# print(user_input, type(user_input))

# user_input_as_a_list = user_input.split()
# print(user_input_as_a_list, type(user_input_as_a_list))
# x, y, z = map(int, user_input_as_a_list)
# print(x, y, z)
# print(type(x), type(y), type(z))

x, y, z = map(int, input().split())
print(type(x), type(y), type(z))
print(x, y, z, sep="\n")
