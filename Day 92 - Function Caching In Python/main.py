import functools
import time
@functools.lru_cache(maxsize=None)
def fx(n):
    time.sleep(5)
    return n*5


print(fx(20))             # Run After 5 Second
print("done for 20")
print(fx(2))
print("done for 2")
print(fx(6))
print("done for 6")

print(fx(20))             # Run instent beacause value of 20 is already saved in lru_cache
print("done for 20")
print(fx(2))
print("done for 2")
print(fx(6))
print("done for 6")

print(fx(8))              # Run After 5 Second Because 8 Is Not Saved In lru_cache
print("done for 8")