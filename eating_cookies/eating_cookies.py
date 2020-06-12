'''
Input: an integer
Returns: an integer
'''
def eating_cookies(n):
    # Your code here
    # Understand
    # Write a function that returns how many ways the monster cookie can eat all the cookies, the monster has 3 options: 1, 2 or 3 at the time. The monster can combine options or just choose one.
    # Plan
    # Mmm, so I know recursion will be the way to go, because we are looking for permutations. now, how can we possibly interchange options? our base case will be checking if the option cookie monster chose is greater than the left overs. for instance, if we are only missing 1 cookie and the monster decides to choose eating 3 at the time, then this is not permitted since we can't have negatives. I'm thinking having a touple per option, and calcultating how many times cookie monster can choose that option and go from option 1 (This obviously, most likely, will be the first case where she eats 1 at the time), then go to option and check if this is possible, and then go down? and last choose the middle one and go to the right and then go the option 1 and repeat the same process.

    # Execute
    # For now just calculate how many times monster cookie can choose each option
    options = [[1, 0], [2, 0], [3, 0]]

    for index in range(len(options)):
        options[index][1] = n // options[index][0]

    print(options)
    # Reflect

if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 5

    print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")
