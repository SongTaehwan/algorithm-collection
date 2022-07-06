//
//  Solution.swift
//  Count of Matches in Tournament
//
//  Created by 송태환 on 2022/02/07.
//

import Foundation

/// [Check out the problem](https://leetcode.com/problems/count-of-matches-in-tournament/)
class Solution {
    func numberOfMatches(_ n: Int) -> Int {
        var result = 0
        var teams = n
        
        while teams != 1 {
            let matches = teams >> 1
            teams = teams & 1 == 0 ? matches : matches + 1
            result += matches
        }
        
        return result
    }
    
    func refactor(_ n: Int) -> Int {
        return n - 1
    }
}
