//
//  Build_an_Array_With_Stack_Operations.swift
//  Build an Array With Stack Operations
//
//  Created by 송태환 on 2022/03/29.
//

import XCTest

class Build_an_Array_With_Stack_Operations: TestCase {
    override func testSolution() {
        XCTAssertEqual(sol.buildArray([1,3], 3), ["Push","Push","Pop","Push"])
        XCTAssertEqual(sol.buildArray([1,2,3], 3), ["Push","Push","Push"])
        XCTAssertEqual(sol.buildArray([1,2], 4), ["Push","Push"])
    }
}

