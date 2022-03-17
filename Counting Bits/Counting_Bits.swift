//
//  Counting_Bits.swift
//  Counting Bits
//
//  Created by 송태환 on 2022/03/17.
//

import XCTest

class Counting_Bits: TestCase {
    override func testSolution() {
        XCTAssertEqual(sol.countBits(2), [0,1,1])
        XCTAssertEqual(sol.countBits(5), [0,1,1,2,1,2])
    }
}

