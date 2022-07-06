//
//  Sum_of_Unique_Elements.swift
//  Sum of Unique Elements
//
//  Created by 송태환 on 2022/04/04.
//

import XCTest

class Sum_of_Unique_Elements: TestCase {
    override func testSolution() {
        XCTAssertEqual(sol.sumOfUnique([1,2,3,2]), 4)
        XCTAssertEqual(sol.sumOfUnique([1,1,1,1,1]), 0)
        XCTAssertEqual(sol.sumOfUnique([1,2,3,4,5]), 15)
    }
}
