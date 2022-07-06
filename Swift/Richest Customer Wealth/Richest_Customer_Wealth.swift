//
//  Richest_Customer_Wealth.swift
//  Richest Customer Wealth
//
//  Created by 송태환 on 2022/01/31.
//

import XCTest

class Richest_Customer_Wealth: TestCase {
    override func testSolution() {
        XCTAssertEqual(sol.maximumWealth([[1,2,3],[3,2,1]]), 6)
        XCTAssertEqual(sol.refactor([[1,2,3],[3,2,1]]), 6)
    }
}
