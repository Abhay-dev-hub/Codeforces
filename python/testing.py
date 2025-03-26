list1 = list(map(int,input().split()))
ind = 0
max_element = list1[0]
 
for i in range (1,len(list1)): 
  if list1[i] > max_element: 
    max_element = list1[i]
    ind = i

print("Index of the maximum element in the list is: ",ind)

