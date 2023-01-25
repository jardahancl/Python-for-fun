from copy import deepcopy


def start_with_0(my_input):
    i = my_input.index(0)
    ordered = my_input[i:] + my_input[:i]
    return ordered


# def translate_index_to_last(circle, ind):
#     result = []
#     for j in range(ind+1, len(circle)):
#         result.append(circle[j])
#     for j in range(ind+1):
#         result.append(circle[j])
#     return result
# 
# 
# def move_last(circle, move_by):
#     result = []
#     for j in range(move_by):
#         result.append(circle[j])
#     result.append(circle[-1])
#     for j in range(move_by, len(circle)-1):
#         result.append(circle[j])
#     return result


def move(numbers_input, n):
    ind = numbers_input.index(n)
    move_by = n % (modulo - 1)
    # translate such that the number to move is the last
    translated_numbers = numbers_input[ind + 1:] + numbers_input[:ind + 1]
    # translated_numbers = translate_index_to_last(numbers_input, ind)
    # actual movement
    result = translated_numbers[:move_by] + [n] + translated_numbers[move_by:-1]
    # result = move_last(translated_numbers, move_by)
    return result
    # return start_with_0(result)


with open('resources/20.txt') as file:
    lines = file.read().splitlines()
numbers_original = [int(x) for x in lines]
modulo = len(numbers_original)

# part 1
numbers = deepcopy(numbers_original)
for number in numbers_original:
    numbers = move(numbers, number)
print(numbers)
numbers = start_with_0(numbers)
result_1 = numbers[1000 % modulo] + numbers[2000 % modulo] + numbers[3000 % modulo]
print(f'20a - sum of numbers on 1000th, 2000th and 3000th position after 0 is {result_1}')

# part 2 - as original
decryption_key = 811_589_153
numbers_decrypted_original = [x * decryption_key for x in numbers_original]
numbers = deepcopy(numbers_decrypted_original)
for _ in range(10):
    for number in numbers_decrypted_original:
        numbers = move(numbers, number)
    # index_0 = numbers.index(0)
    # numbers = numbers[index_0:] + numbers[:index_0]
    # print(numbers)
numbers = start_with_0(numbers)
result_2 = numbers[1000 % modulo] + numbers[2000 % modulo] + numbers[3000 % modulo]
print(f'20b - using decryption key {decryption_key}, the sum is now {result_2}')

# # part 2 simplified
# decryption_key = 811_589_153
# decryption_key_module = decryption_key % (modulo - 1)
# numbers = [x * decryption_key_module for x in numbers_original]
# print(numbers)
# for _ in range(10):
#     for number in numbers_original:
#         numbers = move(numbers, number * decryption_key_module)
#     print(numbers)
# index = numbers.index(0)
# result_2_pre = numbers[(index + 1000) % modulo] + numbers[(index + 2000) % modulo] + numbers[(index + 3000) % modulo]
# result_2 = (result_2_pre // decryption_key_module) * decryption_key
# print(f'20b - using decryption key {decryption_key}, the sum is now {result_2}')
# # 6738624737359 too high
# # 6738624737359








