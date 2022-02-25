from numpy import *
dim = '2x2' # dim = input('Enter the dimension: ')
rows = dim[0]
cols = dim[-1]
arr1 = []
arr2 = []

for r in range(1, (int(rows)+1)):
	for c in range(1, (int(cols)+1)):
		ele = input(f'Enter the element of ({r}+{c}): ')
		if r == 2:
			arr2.append(int(ele))
		else:
			arr1.append(int(ele))

arr3 = []
arr3.insert(0,arr1)
arr3.insert(1,arr2)
arr3 = array(arr3)
print(f'The matrix looks like: \n{arr3}')
det = (arr3[0,0] * arr3[1,1]) - (arr3[0,1]* arr3[1,0])

arr4 = arr3.copy()
arr4[0,0], arr4[1,1] = arr4[1,1], arr4[0,0] # inversing the first and the 4th element

arr4[0,1] = arr4[0,1] * (-1) # multipling the 2nd and the 3rd element of the matrix with -1
arr4[1,0] = arr4[1,0] * (-1)

print("The adjoint of the matrix is:\n",arr4)
print("The determine of the array is:",det)

inverse = (1/det)*(arr4)
print("the inverse of the matrix is:\n", inverse)
