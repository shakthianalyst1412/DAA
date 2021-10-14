import heapq
from collections import defaultdict

def huffmanAlgorithm(fq):
	hp = [[weight, [sym, '']] for sym, weight in fq.items()]
	heapq.heapify(hp)
	while len(hp) > 1:
		lo = heapq.heappop(hp)
		hi = heapq.heappop(hp)
		for pair in lo[1:]:
			pair[1] = '0' + pair[1]
		for pair in hi[1:]:
			pair[1] = '1' + pair[1]
		heapq.heappush(hp, [lo[0] + hi[0]] + lo[1:] + hi[1:])
	return sorted(heapq.heappop(hp)[1:], key=lambda p: (len(p[-1]), p))

str1=[]
str1=input("Take input from the User: ")
fq = defaultdict(int)
for sym in str1:
	fq[sym] += 1

huff = huffmanAlgorithm(fq)
print ("Symbol".ljust(10) + "Weight".ljust(10) + "Huffman Code")
for p in huff:
	print (p[0].ljust(10) + str(fq[p[0]]).ljust(10) + p[1])

#Time complexity: O(nlogn) where n is the number of unique characters. 
#If there are n nodes, extractMin() is called 2*(n – 1) times. extractMin() takes O(logn) time as it calles minHeapify().
#So, overall complexity is O(nlogn).