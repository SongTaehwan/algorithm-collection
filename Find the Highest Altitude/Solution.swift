//
//  Solution.swift
//  Find the Highest Altitude
//
//  Created by 송태환 on 2022/02/09.
//

import Foundation

class Solution {
    func largestAltitude(_ gain: [Int]) -> Int {
        var sum = 0
        var maxSum = 0
        
        for num in gain {
            sum = sum + num
            maxSum = max(maxSum, sum)
        }
        
        return maxSum
    }
}
