def partition(low, high, A):
  i = low
  pivot = A[high]

  for j in range(low, high):
    if A[j] < pivot:
      A[i], A[j] = A[j], A[i]
      i+=1 

  A[i], A[high] = A[high], A[i] 

  return i
def quick_sort(low, high, A):
  if low < high:
    pi = partition (low, high, A)
    quick_sort (low, pi-1, A)
    quick_sort (pi+1, high, A)

def main():    
  A = [5,4,3,2,1]
  quick_sort(0, len(A)-1, A)
  print (A)


main()