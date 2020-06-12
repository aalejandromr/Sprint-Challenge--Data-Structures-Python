'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
def single_number(arr):
    # Your code here
    # Understand
    # For a given array, find the index that doesn't repeat twice, I can assume there will always be only one and only one index missing its pair, every other number shows up exactly.

    # Plan
    # Traverse the array in every other manner, store prev value in a variable. If prev doesn't match current, return, this is the one missing

    index = 2
    middle = arr[0]
    while index <= len(arr):
        print(f"middle {arr[index - 1]}")
        print(f"current {arr[index]}")
        if middle != arr[index]:
            return arr[index]
        else:
            middle = arr[index - 1]
        index += 2


if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")