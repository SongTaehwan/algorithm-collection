//
//  Detect_Capital.swift
//  Detect Capital
//
//  Created by 송태환 on 2022/01/24.
//

import XCTest

class Detect_Capital: TestCase {
    override func testSolution() {
        XCTAssertEqual(sol.detectCapitalUse("Google"), true)
        XCTAssertEqual(sol.detectCapitalUse("USA"), true)
        XCTAssertEqual(sol.detectCapitalUse("FlaG"), false)
        XCTAssertEqual(sol.detectCapitalUse("flaG"), false)
        XCTAssertEqual(sol.detectCapitalUse("leetcode"), true)
        XCTAssertEqual(sol.detectCapitalUse("g"), true)
    }
}

