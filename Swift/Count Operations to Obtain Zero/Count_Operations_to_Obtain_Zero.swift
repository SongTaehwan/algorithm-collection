//
//  Count_Operations_to_Obtain_Zero.swift
//  Count Operations to Obtain Zero
//
//  Created by 송태환 on 2022/03/23.
//

import XCTest

class Count_Operations_to_Obtain_Zero: TestCase {
    override func testSolution() {
        XCTAssertEqual(sol.countOperations(2, 3), 3)
        XCTAssertEqual(sol.countOperations(10, 10), 1)
    }
}

