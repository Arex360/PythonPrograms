import sys
I = []
class Selection:
  A = []
  def Entry(self):
    r = int(input("Enter the range: "))
    for i in range(r):
      a = int(input("Enter Number"+str(i+1)+ " "))
      I.append(a)
  def SelectionSort(self, arr):
    A = arr
    for i in range(len(A)):
      min_Value = i
      for j in range(i+1, len(A)):
        if A[min_Value] > A[j]:
          min_Value = j
        A[i], A[min_Value] = A[min_Value], A[i]
    for i in A:
      print(i)
z = Selection()
z.Entry()
z.SelectionSort(I)
