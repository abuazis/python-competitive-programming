# Time Conversion Challenge
# https://www.hackerrank.com/challenges/time-conversion/problem

def timeConversion():
    # Catch input time value
    time = input().strip()

    # Assign time element with splitting by ':' 
    # and cast time element into int
    h, m, s = map(int, time[:-2].split(':'))

    # Catch AM/PM type
    p = time[-2:]

    # Convert hour format based on 'p' variable
    h = h % 12 + (p.upper() == 'PM') * 12

    # Print new time format with binding
    print(('%02d:%02d:%02d') % (h, m, s))

if __name__ == '__main__':
    # Run logic function
    timeConversion()