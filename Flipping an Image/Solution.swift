//
//  Solution.swift
//  Flipping an Image
//
//  Created by 송태환 on 2022/01/28.
//

import Foundation

class Solution {
    func flipAndInvertImage(_ image: [[Int]]) -> [[Int]] {
        var converted: [Int] = image.flatMap { $0 }.map { $0 ^ 1 }
        var result = Array(repeating: [Int](), count: image.count)

        var index = image.count - 1
        
        while converted.count != 0 {
            let binary = converted.removeLast()
            result[index].append(binary)
            
            if result[index].count == image.count {
                index -= 1
            }
        }
        
        return result
    }
}
