

def searchMatrix(matrix, target):
    
    m, n = len(matrix), len(matrix[0])
    t = m * n
    l, r = 0, t-1
    
    while l <= r:
        
        M = (l+r) // 2
        M_i = M // n
        M_j = M % n
        
        m_val = matrix[M_i][M_j]
        
        if target == m_val: return True
        
        elif target < m_val: r = M -1
        
        else: l = M + 1
        
    return False



test_matrix = [
    [1,  3,  5,  7],
    [10, 11, 16, 20],
    [23, 30, 34, 60]
]


tests = [
    (3, True),
    (13, False),
    (60, True),
    (1, True),
    (0, False)
]


for target, expected in tests:
    result = searchMatrix(test_matrix, target)
    print(f"Target {target:2}: {'PASS' if result == expected else 'FAIL'} (Found: {result})")