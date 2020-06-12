'''
Input: a List of integers
Returns: a List of integers
'''
def moving_zeroes(arr):
    # Your code here
    # Understand
    # Given an array, move all the zeroes to the end of the given array, and return mutated array, order does not matter.

    # Plan
    # Traverse the array, when you encounter a 0 value, remove it from the array, have a counter of 0s removed, and append them to the original array

    # Execute
    zeroes_found = 0
    temp_arr = []
    for index in range(len(arr)):
        if arr[index] == 0:
            # arr.pop(index)
            zeroes_found += 1
        else:
            temp_arr.append(arr[index])
    arr = temp_arr
    if zeroes_found > 0:
        return arr + [0] * zeroes_found
    return arr

    # Reflect
    # I feel like I'm using unnecesary variables
if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")