//
//  Binary_Search.swift
//  Binary Search
//
//  Created by 송태환 on 2022/01/14.
//

import XCTest

class Binary_Search: TestCase {
    func testBinarySearch() {
        XCTAssertEqual(sol.search([-1,0,3,5,9,12], 9), 4)
        XCTAssertEqual(sol.search([-1,0,3,5,9,12], 2), -1)
        XCTAssertEqual(sol.refactored([-1,0,3,5,9,12], 9), 4)
        XCTAssertEqual(sol.refactored([-1,0,3,5,9,12], 2), -1)
    }
}
