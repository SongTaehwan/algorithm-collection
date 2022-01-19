//
//  Solution.swift
//  Can Place Flowers
//
//  Created by 송태환 on 2022/01/18.
//

import Foundation

/// [Check out the problem](https://leetcode.com/problems/can-place-flowers/submissions/)
class Solution {
    /// Greedy
    func canPlaceFlowers(_ flowerbed: [Int], _ n: Int) -> Bool {
        var flowerbed = flowerbed
        var count = 0, i = 0
        
        while i < flowerbed.count {
            let next = (i == flowerbed.count - 1) || flowerbed[i + 1] == 0
            let prev = (i == 0) || flowerbed[i - 1] == 0
            let current = flowerbed[i] == 0
            
            if current && prev && next {
                flowerbed[i] = 1
                count += 1
            }
            
            if count >= n {
                return true
            }
            
            i += 1
        }
        
        return false
    }
}
