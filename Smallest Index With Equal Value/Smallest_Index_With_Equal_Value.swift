//
//  Smallest_Index_With_Equal_Value.swift
//  Smallest Index With Equal Value
//
//  Created by 송태환 on 2022/02/18.
//

import XCTest

class Smallest_Index_With_Equal_Value: TestCase {
    override func testSolution() {
        XCTAssertEqual(sol.smallestEqual([0,1,2]), 0)
        XCTAssertEqual(sol.smallestEqual([4,3,2,1]), 2)
        XCTAssertEqual(sol.smallestEqual([1,2,3,4,5,6,7,8,9,0]), -1)
    }
}

