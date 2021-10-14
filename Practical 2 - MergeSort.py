import os,psutil,time
process = psutil.Process(os.getpid())
start = time.time()

def mergeSortAlgo(myList):
    if len(myList) > 1:
        mid = len(myList) // 2
        left = myList[:mid]
        right = myList[mid:]
        mergeSortAlgo(left)
        mergeSortAlgo(right)
        i = 0
        j = 0
        k = 0        
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
              myList[k] = left[i]
              i += 1
            else:
                myList[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            myList[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            myList[k]=right[j]
            j += 1
            k += 1
myList = [188,106,67,40,133,73,60,226,21,139,24,72,129,168,125,76,219,75,90,171,175,175,180,238,93,245,13,66,64,36,42,14,162,187,68,59,56,194,44,80,80,45,93,239,12,159,228,172,118,3,220,117,151,18,123,99,243,125,50,67,95,50,197,144,162,38,207,221,70,125,158,86,41,85,109,63,150,42,82,193,98,69,16,1,7,167,125,66,21,206,36,241,106,33,153,168,120,104,42,221]
#myList = input('Enter the values: ').split()
#myList = [int(x) for x in myList]
mergeSortAlgo(myList)
end = time.time()
timeDiff = (end-start)
execTime = timeDiff*1000
print("Sorted Array is:",myList)
print()
print(f"Runtime of the program is {end - start}")
print("Consumed memory in MB : ",psutil.Process(os.getpid()).memory_info().rss / 1024 ** 2,'MB')
