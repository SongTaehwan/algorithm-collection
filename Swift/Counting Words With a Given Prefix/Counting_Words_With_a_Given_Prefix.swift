//
//  Counting_Words_With_a_Given_Prefix.swift
//  Counting Words With a Given Prefix
//
//  Created by 송태환 on 2022/04/05.
//

import XCTest

class Counting_Words_With_a_Given_Prefix: TestCase {
    override func testSolution() {
        XCTAssertEqual(sol.prefixCount(["pay","attention","practice","attend"], "at"), 2)
        XCTAssertEqual(sol.prefixCount(["leetcode","win","loops","success"], "code"), 0)
    }
}

