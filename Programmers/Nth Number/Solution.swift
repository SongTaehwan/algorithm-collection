//
//  Solution.swift
//  Reverse Bits
//
//  Created by 송태환 on 2022/01/19.
//

import Foundation

func solution(_ array:[Int], _ commands:[[Int]]) -> [Int] {
    return commands.map { command in
        let range = (command[0] - 1)...(command[1] - 1)
        let position = command[2] - 1
        return array[range].sorted()[position]
    }
}
