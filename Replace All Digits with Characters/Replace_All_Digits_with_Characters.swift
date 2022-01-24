//
//  Replace_All_Digits_with_Characters.swift
//  Replace All Digits with Characters
//
//  Created by 송태환 on 2022/01/24.
//

import XCTest

class Replace_All_Digits_with_Characters: TestCase {
    override func testSolution() {
        XCTAssertEqual(sol.replaceDigits("a1c1e1"), "abcdef")
        XCTAssertEqual(sol.replaceDigits("a1b2c3d4e"), "abbdcfdhe")
        XCTAssertEqual(sol.refactored("a1c1e1"), "abcdef")
        XCTAssertEqual(sol.refactored("a1b2c3d4e"), "abbdcfdhe")
    }
}

