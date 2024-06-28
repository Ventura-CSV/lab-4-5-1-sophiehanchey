import random


def main():
    total = 0
    numbers = []
    i = 0
    
    while i<5:
        new_num = random.randint(0,100)
        
        numbers.append(new_num)
        total += new_num
        
        i += 1
        

    print(f'The random values are {numbers}')
    print(f'The total is {total}')

    ########################################
    # Do not delete the return statement
    ########################################
    return numbers, total


if __name__ == '__main__':
    main()
