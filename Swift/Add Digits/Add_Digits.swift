//
//  Add_Digits.swift
//  Add Digits
//
//  Created by 송태환 on 2022/02/08.
//

import XCTest

class Add_Digits: TestCase {
    override func testSolution() {
        XCTAssertEqual(sol.addDigits(38), 2)
        XCTAssertEqual(sol.addDigits(11), 2)
        XCTAssertEqual(sol.addDigits(0), 0)
        XCTAssertEqual(sol.addDigits(10), 1)
        
        XCTAssertEqual(sol.refactor(38), 2)
        XCTAssertEqual(sol.refactor(11), 2)
        XCTAssertEqual(sol.refactor(0), 0)
        XCTAssertEqual(sol.refactor(10), 1)
    }
}
