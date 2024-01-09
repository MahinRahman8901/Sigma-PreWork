def minmax(arr): 
  newarray = []
  max_number = arr[0]
  min_number = arr[0]
  for i in arr:
      if i > max_number:
        max_number = i
  newarray.append(max_number)
  for i in arr:
    if i < min_number:
      min_number = i
  newarray.append(min_number)
  return newarray


arr = [20, 50, 12, 6, 14, 8]

print(minmax(arr))
