//
//  Last_Stone_Weight.swift
//  Last Stone Weight
//
//  Created by 송태환 on 2022/03/18.
//

import XCTest

class Last_Stone_Weight: TestCase {
    override func testSolution() {
        XCTAssertEqual(sol.lastStoneWeight([2,7,4,1,8,1]), 1)
        XCTAssertEqual(sol.lastStoneWeight([1]), 1)
        XCTAssertEqual(sol.lastStoneWeight([2,2]), 0)
    }
}
