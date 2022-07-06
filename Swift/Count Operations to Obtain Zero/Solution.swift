//
//  Solution.swift
//  Count Operations to Obtain Zero
//
//  Created by 송태환 on 2022/03/23.
//

import Foundation
/// [Checkout the problem](https://leetcode.com/problems/count-operations-to-obtain-zero/)
class Solution {
    func countOperations(_ num1: Int, _ num2: Int) -> Int {
        var num1 = num1
        var num2 = num2
        var count = 0
        
        while num1 != 0 && num2 != 0 {
            if num1 >= num2 {
                num1 = num1 - num2
            } else {
                num2 = num2 - num1
            }
            
            count += 1
        }
            
        return count
    }
}
