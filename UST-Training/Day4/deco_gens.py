def mainDude(func):
    def wrapper(num, dp):
        return func(num, dp)
    return wrapper

@mainDude
def fibonnaci(num, dp):
    if num <= 1: return num
    if dp[num] != None: return dp[num]
    dp[num]=  fibonnaci(num-1, dp) + fibonnaci(num-2, dp)
    return dp[num]

times = 10
dp = [None] * (times + 1)
num = fibonnaci(times, dp)
print(num)


