items = [1, 2, 3, 4, 5, 6 , 7, 8, 9, 10]

def binary_search(alist, item):
  first = 0
  last = len(alist)-1
  found = False

  while first <= last and not found:

    midpoint = (first + last)//2
    
    if alist[midpoint] == item:
      found = True
    else:
      if item < alist[midpoint]:
        last = midpoint-1
      else:
        first = midpoint+1
    
    return found

print(binary_search(items, 19))