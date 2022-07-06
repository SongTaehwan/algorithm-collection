//
//  Unique_Number_of_Occurrences.swift
//  Unique Number of Occurrences
//
//  Created by 송태환 on 2022/02/16.
//

import XCTest

class Unique_Number_of_Occurrences: TestCase {
    override func testSolution() {
        XCTAssertEqual(sol.uniqueOccurrences([1,2,2,1,1,3]), true)
        XCTAssertEqual(sol.uniqueOccurrences([1,2]), false)
        XCTAssertEqual(sol.uniqueOccurrences([-3,0,1,-3,1,1,1,-3,10,0]), true)
    }
}

