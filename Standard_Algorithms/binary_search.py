def binary_search (A, left, right, target):
  if right > left:  
    mid = left+(right - left) //2
    if A[mid] == target:
      return mid
    elif A[mid] > target:
      return binary_search(A, left, mid, target)
    else:
      return binary_search(A, mid+1, right, target)
    

a = [1,2,3,4,5,6,7,8,9,10]

for i in range(1,11):
  print (binary_search(a, 0, 10, i))