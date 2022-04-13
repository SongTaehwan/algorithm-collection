//
//  Calculate_Money_in_Leetcode_Bank.swift
//  Calculate Money in Leetcode Bank
//
//  Created by 송태환 on 2022/04/13.
//

import XCTest

class Calculate_Money_in_Leetcode_Bank: TestCase {
    override func testSolution() {
        XCTAssertEqual(sol.totalMoney(4), 10)
        XCTAssertEqual(sol.totalMoney(10), 37)
        XCTAssertEqual(sol.totalMoney(20), 96)
        
        XCTAssertEqual(sol.refactor(4), 10)
        XCTAssertEqual(sol.refactor(10), 37)
        XCTAssertEqual(sol.refactor(20), 96)
    }
}

