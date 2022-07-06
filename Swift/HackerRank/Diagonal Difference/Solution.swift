//
//  Solution.swift
//  Diagonal Difference
//
//  Created by 송태환 on 2022/01/26.
//

import Foundation

/// [Checkout the problem](https://www.hackerrank.com/challenges/diagonal-difference/problem)
func diagonalDifference(arr: [[Int]]) -> Int {
    var leftSum = 0
    var rightSum = 0
    let last = arr.count - 1
    
    for (i, row) in arr.enumerated() {
        leftSum += row[i]
        rightSum += row[last - i]
    }
    
    let result = leftSum - rightSum
    return result >= 0 ? result : ~result + 1
}

func refactor(arr: [[Int]]) -> Int {
    let last = arr.count - 1
    var result = 0
    
    for (i, row) in arr.enumerated() {
        result += row[i]
        result -= row[last-i]
    }
    
    
    return result >= 0 ? result : ~result + 1
}

func refactor2(arr: [[Int]]) -> Int {
    let result = arr.enumerated().reduce(0) {
        let left = $1.element[$1.offset]
        let right = $1.element[arr.count - 1 - $1.offset]
        return $0 + left - right
    }
    
    return result >= 0 ? result : ~result + 1
}
