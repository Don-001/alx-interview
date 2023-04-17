#!/usr/bin/python3


def pascals_triangle(n):
    triangle = [[1]]
    for i in range(n-1):
        row = []
        row.append(triangle[i][0])
        for j in range(len(triangle[i])-1):
            row.append(triangle[i][j] + triangle[i][j+1])
        row.append(triangle[i][-1])
        triangle.append(row)
    return triangle