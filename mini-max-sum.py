# Mini Max Sum Challenge
# https://www.hackerrank.com/challenges/mini-max-sum/problem

def miniMaxSum():
    # Iterate input result and cast each value to integer
    nums = [int(x) for x in input().strip().split(' ')]

    # Subtract sum nums result with max element
    # Subtract sum nums result with min element
    print(sum(nums) - max(nums), sum(nums) - min(nums))

if __name__ == '__main__':
    # Run logic function
    miniMaxSum()