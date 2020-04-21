import random

my_randoms = list()
for i in range(10):
    my_randoms.append(random.randrange(1, 6))

numbers_1_to_10 = range(1, 11)

for number in numbers_1_to_10:
    the_numbers_match = False

if __name__ == '__main__':
    print(f'{number} is in the random list')