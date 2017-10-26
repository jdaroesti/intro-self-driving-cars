import sys


def my_generator(total_values):
    for i in range(total_values):
        yield i


if __name__ == '__main__':
    total_values = int(sys.argv[1])

    for i in my_generator(total_values):
        print(i)
