//
//  Solution.swift
//  Reverse Bits
//
//  Created by 송태환 on 2022/01/19.
//

import Foundation

/// [Check out the problem](https://programmers.co.kr/learn/courses/30/lessons/64061)
func solution(_ board:[[Int]], _ moves:[Int]) -> Int {
    let indice = moves.map { $0 - 1 }

    var rows = Array(board.reversed())
    var stack = [Int]()
    
    for index in indice {
        let isEmptyRow = (rows.last ?? []).reduce(0,+) == 0

        if isEmptyRow {
            _ = rows.popLast()
        }

        var rowIndex = rows.count - 1

        while rowIndex >= 0  {
            let item = rows[rowIndex][index]

            if item == 0 {
                rowIndex -= 1
                continue
            }

            stack.append(item)
            rows[rowIndex][index] = 0
            break
        }
    }
    
    var index = 0
    var result = 0

    while index < stack.count {
        guard index + 1 != stack.count else { break }
        
        if stack[index] == stack[index + 1] {
            stack.remove(at: index)
            stack.remove(at: index)
            result += 2
            index = max(index - 1, 0)
            
            continue
        }

        index += 1
    }
    
    return result
}
