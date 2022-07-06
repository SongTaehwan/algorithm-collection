//
//  Excel_Sheet_Column_Number.swift
//  Excel Sheet Column Number
//
//  Created by 송태환 on 2022/02/22.
//

import XCTest

class Excel_Sheet_Column_Number: TestCase {
    override func testSolution() {
        XCTAssertEqual(sol.titleToNumber("A"), 1)
        XCTAssertEqual(sol.titleToNumber("AB"), 28)
        XCTAssertEqual(sol.titleToNumber("ZY"), 701)
    }
}

