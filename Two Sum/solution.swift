//
//  solution.swift
//  Two Sum
//
//  Created by 송태환 on 2022/01/13.
//

import Foundation

class Solution {
    func twoSum(_ nums: [Int], _ target: Int) -> [Int] {
        var dict = [Int: Int]()
        
        for i in 0..<nums.count {
            let number = nums[i]
            
            if let index = dict[number] {
                return [index, i]
            }
            
            let complement = target - number
            dict[complement] = i
        }
        
        return []
    }
}
