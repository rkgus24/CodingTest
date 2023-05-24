don = int(input())
count = 0

for i in [50000, 10000, 5000, 1000, 500, 100, 50, 10]:
	if don // i != 0:
		count += don // i
		don %= i
print(count)
