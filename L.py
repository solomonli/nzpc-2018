from heapq import merge

def get_ints():
	return map(int, input().split())

n, sx, sy = get_ints()
B = list(get_ints())
B.sort()

def spots(b):
	run = 1
	while True:
		h = b + run * (-sy) // sx
		# if h < B[0]:
		# 	break
		yield -h
		run += 1


def possible(cnt):
	assert(cnt <= len(B))
	rev = reversed(B)
	its = [spots(next(rev)) for _ in range(cnt)]
	x = 0
	heights = merge(*its)
	for b in rev:
		h = -next(heights)
		if h < b:
			return False
	return True

def bs():
	a = 1
	b = len(B)
	while a != b:
		mid = a + (b - a)//2
		if possible(mid):
			b = mid
		else:
			a = mid + 1
	ans = len(B) - a
	return ans

#print(bs())
def brute():
	for cnt in range(1,len(B)+1):
		if possible(cnt):
			return len(B)-cnt
			break

#print(brute())
print(bs())