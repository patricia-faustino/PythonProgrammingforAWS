# This function calculates the average of a list of numbers

def calculate_average(numbers):
    # Ensure the list is not empty
    if len(numbers) == 0:
        return 0

    # Calculate the sum of the numbers in the list
    sum = 0
    for number in numbers:
        sum += number

    # Calculate the average and return the value
    average = sum / len(numbers)

    return average


if __name__ == '__main__':
    numbers_list = [1, 23, 67, 58, 99]

    numbers_average = calculate_average(numbers_list)
    print(f"Average of the numbers in the list: {numbers_average}.")
