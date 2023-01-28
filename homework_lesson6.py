elem_count = input("Enter the number of elements: ")
arr = []
for x in range(1, int(elem_count)+1):
	elem = input(f"Enter element {x}: ")
	arr.append(elem)
    
new_arr = []
for el in arr:
	if len(el) <= 3:
		new_arr.append(el)

print(f"new array: {new_arr}")
    