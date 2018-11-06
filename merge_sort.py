from random import  randint as random
from time import time as timer

"UTILITY FUNCTION : "
def wrap(f):
    t1 = timer()
    
"Rishabh code here"
def merge(a, b):
    if a and b:
        if a[0] > b[0]:
            a, b = b, a
        return [a[0]] + merge(a[1:], b)
    return a + b

def merge_sort(array):
    if len(array) <= 1 : return array
    half = len(array) // 2
    left = merge_sort(array[:half])
    right = merge_sort(array[half:])
    return merge(left, right)
"Rishabhs code end here"

"Masters code here"
def MERGE_SORT(A):
    start = []
    end = []
    while len(A) > 1:
        a = min(A)
        b = max(A)
        start.append(a)
        end.append(b)
        A.remove(a)
        A.remove(b)
    if A: start.append(A[0])
    end.reverse()
    return (start + end)
"Master code end here"


a = [random(1, 10000) for i in range(1000)]

"I was lazy enough to not add wrapper!!"
t1 = timer()
MERGE_SORT(a)
t2 = timer()
dt_bhushan = t2-t1

t3 = timer()
merge_sort(a)
t4 = timer()
dt_rishabh = t4-t3

if dt_bhushan < dt_rishabh : 
    print("Bhushan's' code won, fraction :", dt_rishabh/dt_bhushan)
else:
    print("Rishabh's' code won, fraction :", 1/(dt_rishabh/dt_bhushan))
