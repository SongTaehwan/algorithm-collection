//
//  Count_Negative_Numbers_in_a_Sorted_Matrix.swift
//  Count Negative Numbers in a Sorted Matrix
//
//  Created by 송태환 on 2022/02/04.
//

import XCTest

class Count_Negative_Numbers_in_a_Sorted_Matrix: TestCase {
    override func testSolution() {
        XCTAssertEqual(sol.countNegatives([[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]), 8)
        XCTAssertEqual(sol.countNegatives([[3,2],[1,0]]), 0)
        
        XCTAssertEqual(sol.refactor([[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]), 8)
        XCTAssertEqual(sol.refactor([[3,2],[1,0]]), 0)
    }
}

