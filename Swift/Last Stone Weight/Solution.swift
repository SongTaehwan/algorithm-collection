//
//  Solution.swift
//  Last Stone Weight
//
//  Created by 송태환 on 2022/03/18.
//

import Foundation

class Solution {
    func lastStoneWeight(_ stones: [Int]) -> Int {
        var array = stones.sorted()
        
        while array.count > 1 {
            let y = array.removeLast()
            let x = array.removeLast()
            
            if x != y {
                array.append(y - x)
                array = array.sorted()
            }
        }
        
        return array.last ?? 0
    }
}
