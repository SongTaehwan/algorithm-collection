//
//  Solution.swift
//  Fibonacci Number
//
//  Created by 송태환 on 2022/02/23.
//

import Foundation

class Solution {
    func fib(_ n: Int) -> Int {
        guard n > 1 else { return n }
        let result = fib(n-1) + fib(n-2)
        return result
    }
}
