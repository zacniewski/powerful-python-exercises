# https://www.codewars.com/kata/5877e7d568909e5ff90017e6/train/python


def find_all(sum_dig, digs):
    output = []
    solutions = []
    number_of_possible_numbers = 0
    current_sum = 0

    for number in range(10**(digs-1), 10**digs):
        temp = number
        while temp > 0:
            last_before = temp % 10
            temp = temp // 10
            last_after = temp % 10
            if last_after <= last_before:
                current_sum += last_before
                if current_sum > sum_dig:
                    break
            else:
                current_sum = 0
                break

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
    print(find_all(35, 6))
