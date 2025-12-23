#!/usr/bin/python3

def print_times_table(n):
    for i in range(1, 11):
        print(f"{n} * {i} = {n * i}")

def print_range_table(n, start, end):
    for i in range(start, end + 1):
        print(f"{n} * {i} = {n * i}")

def sum_times_table(n):
    sum = 0

    for i in range(1, 11):
        num_multiplied = n * i
        sum += num_multiplied

    return sum

def print_grid(size):
    print(size * "*")

    for i in range(1, size):
        print(size * "*")

def print_triangle(height):
    for i in range(1, height + 1):
        print(i)
        for i in range(1, height + 1, 3):
            print(i * "*")
        


# # UNIT TEST FOR: print_times_table()
# test = print_times_table(5)
# test = print_times_table(11)
# test = print_times_table(20)

# # UNIT TEST FOR: print_range_table()
# test = print_range_table(5)
# test = print_range_table(11)
# test = print_range_table(20)

# UNIT TEST FOR: print_grid()
test = print_grid(2)
test = print_grid(5)
test = print_grid(11)

# # UNIT TEST FOR: print_triangle()
# test = print_triangle(2)
# test = print_triangle(5)
# test = print_triangle(11)

