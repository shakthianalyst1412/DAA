import os,psutil,time
process = psutil.Process(os.getpid())
start = time.time()

def insertionSortAlgo(arr):
	for i in range(1, len(mylist)):
		key = mylist[i]
		j = i-1
		while j >=0 and key < mylist[j] :
				mylist[j+1] = mylist[j]
				j -= 1
		mylist[j+1] = key

mylist = [188,106,67,40,133,73,60,226,21,139,24,72,129,168,125,76,219,75,90,171,175,175,180,238,93,245,13,66,64,36,42,14,162,187,68,59,56,194,44,80,80,45,93,239,12,159,228,172,118,3,220,117,151,18,123,99,243,125,50,67,95,50,197,144,162,38,207,221,70,125,158,86,41,85,109,63,150,42,82,193,98,69,16,1,7,167,125,66,21,206,36,241,106,33,153,168,120,104,42,221]
#mylist = input('Enter the values: ').split()
#mylist = [int(x) for x in mylist]
insertionSortAlgo(mylist)
end = time.time()
#timeDiff = (end-start)
#execTime = timeDiff*1000
print ("Sorted Array is:",mylist)
print()
print(f"Runtime of the program is {end - start}")
print("Consumed memory in MB : ",psutil.Process(os.getpid()).memory_info().rss / 1024 ** 2,'MB')
