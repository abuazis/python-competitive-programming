# Apple and Orange Challenge
# https://www.hackerrank.com/challenges/apple-and-orange/problem

def countApplesAndOranges(s, t, a, b, apples, oranges):
    # Print the number of apples that fall on Sam's house
    print(
        # Check if apple element distance is >= than 
        # starting point and <= than ending point Sam's house
        sum([1 for x in apples if (x + a) >= s and (x + a) <= t])
    )

    # Print the number of oranges that fall on Sam's house
    print(
        # Check if apple element distance is >= than 
        # starting point and <= than ending point Sam's house
        sum([1 for x in oranges if (x + b) >= s and (x + b) <= t])
    )

if __name__ == '__main__':
    # Catch first multiple input
    first_multiple_input = input().rstrip().split()

    # Assign starting point of Sam's house location
    s = int(first_multiple_input[0])

    # Assign ending location of Sam's house location
    t = int(first_multiple_input[1])

    # Catch second multiple input
    second_multiple_input = input().rstrip().split()

    # Assign location of the Apple tree
    a = int(second_multiple_input[0])

    # Assign location of the Orange tree
    b = int(second_multiple_input[1])

    # Catch third multiple input
    third_multiple_input = input().rstrip().split()

    # Assign space-separated integers denoting the respective 
    # distances that each apple falls from point 'a'
    m = int(third_multiple_input[0])

    # Assign space-separated integers denoting the respective 
    # distances that each orange falls from point 
    n = int(third_multiple_input[1])

    # Catch input of distances at which each apple falls 
    # from the tree
    apples = list(map(int, input().rstrip().split()))

    # Catch input of distances at which each orange falls 
    # from the tree
    oranges = list(map(int, input().rstrip().split()))

    # Run logic funtion
    countApplesAndOranges(s, t, a, b, apples, oranges)