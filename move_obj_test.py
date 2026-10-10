def move_zero(arr):
    
    no_zero = [num for num in arr if num != 0]

    zero = len(arr) - len(no_zero)

    return no_zero+[0]*zero


print(move_zero([0, 1, 0, 2, 0, 3, 0, 4, 0, 5]))