# Birthday Cake Candles Challenge
# https://www.hackerrank.com/challenges/birthday-cake-candle/problem

def birthdayCakeCandles():
    # Cast input type to int
    int(input().strip())

    # Iterate input result and cast each value to integer
    candles = [int(x) for x in input().strip().split(' ')]

    # Print count max value result 
    print(candles.count(max(candles)))

if __name__ == '__main__':
    # Run logic function
    birthdayCakeCandles()