import time


def sum_of_2(n):
    start = time.time()
    the_sum = 0
    for i in range(1, n+1):
        the_sum = the_sum + i
    
    end = time.time()

    return the_sum, end-start


def sum_of_3(n):
    start = time.time()
    the_sum = (n * (n+1))/2
    end = time.time()
    return the_sum, end-start


def main():
    for i in range(5):
        print("Sum is %d required %10.7f seconds" % sum_of_2(100000000))

    for x in range(5):
        print("Sum is %d required %10.7f seconds" % sum_of_3(100000000))





main()





