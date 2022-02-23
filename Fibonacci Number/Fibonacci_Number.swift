//
//  Fibonacci_Number.swift
//  Fibonacci Number
//
//  Created by 송태환 on 2022/02/23.
//

import XCTest

/// [Check out the problem](https://leetcode.com/problems/fibonacci-number/)
class Fibonacci_Number: TestCase {
    override func testSolution() {
        XCTAssertEqual(sol.fib(2), 1)
        XCTAssertEqual(sol.fib(3), 2)
        XCTAssertEqual(sol.fib(4), 3)
    }
}

