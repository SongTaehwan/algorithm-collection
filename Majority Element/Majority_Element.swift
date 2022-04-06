//
//  Majority_Element.swift
//  Majority Element
//
//  Created by 송태환 on 2022/04/06.
//

import XCTest

class Majority_Element: TestCase {
    override func testSolution() {
        XCTAssertEqual(sol.majorityElement([3,2,3]), 3)
        XCTAssertEqual(sol.majorityElement([2,2,1,1,1,2,2]), 2)
    }
}

