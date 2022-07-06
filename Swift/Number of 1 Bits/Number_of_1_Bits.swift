//
//  Number_of_1_Bits.swift
//  Number of 1 Bits
//
//  Created by 송태환 on 2022/03/17.
//

import XCTest

class Number_of_1_Bits: TestCase {
    override func testSolution() {
        XCTAssertEqual(sol.hammingWeight(11), 3)
        XCTAssertEqual(sol.hammingWeight(128), 1)
        XCTAssertEqual(sol.hammingWeight(4294967293), 31)
        
        XCTAssertEqual(sol.refactor(11), 3)
        XCTAssertEqual(sol.refactor(128), 1)
        XCTAssertEqual(sol.refactor(4294967293), 31)
    }
}

