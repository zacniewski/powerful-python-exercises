# https://www.codewars.com/kata/5877e7d568909e5ff90017e6/train/python

def find_all(sum_dig, digs):
    """
    We want to generate all the numbers of three digits where:
    the sum of their digits is equal to 10.
    their digits are in increasing order (the numbers may have two or more equal contiguous digits)

    The numbers that fulfill the two above constraints are: 118, 127, 136, 145, 226, 235, 244, 334
    Make a function that receives two arguments:
    the sum of digits value
    the desired number of digits for the numbers

    The function should output an array with three values: [1,2,3]
    1 - the total number of possible numbers
    2 - the minimum number
    3 - the maximum number

    """
    output = []
    solutions = []
    number_of_possible_numbers = 0
    current_sum = 0

    for number in range(10**(digs-1), 10**digs):
        for index in range(len(str(number)) - 1):
            if str(number)[index] <= str(number)[index+1]:
                current_sum += int(str(number)[index])
                if current_sum > sum_dig:
                    break
            else:
                current_sum = 0
                break
        current_sum += int(str(number)[-1])

        if current_sum == sum_dig:
            solutions.append(number)
            number_of_possible_numbers += 1
        current_sum = 0

    if number_of_possible_numbers:
        output.append(number_of_possible_numbers)
    if len(solutions) > 0:
        output.append(solutions[0])
        output.append(solutions[-1])
    return output


if __name__ == '__main__':
    print(find_all(23, 4))
