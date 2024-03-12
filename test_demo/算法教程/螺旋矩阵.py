"""
@ Title:
@ Author: Cathy
@ Time: 2024/3/6 16:15
"""
# 不会做。。。

def spiralOrder(matrix):
    if not matrix or not matrix[0]:
        return []

    rows, columns = len(matrix), len(matrix[0])
    order = []
    left, right, top, bottom = 0, columns-1, 0, rows-1
    while left <= right and top <= bottom:
        for column in range(left, right+1):
            order.append(matrix[top][column])
        for row in range(top+1, bottom+1):
            order.append(matrix[row][right])
        if left < right and top < bottom:
            pass




if __name__ == '__main__':
    matrix = [[1,2,3],[4,5,6],[7,8,9]]
    spiralOrder(matrix)