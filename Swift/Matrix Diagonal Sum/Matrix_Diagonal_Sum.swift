//
//  Matrix_Diagonal_Sum.swift
//  Matrix Diagonal Sum
//
//  Created by 송태환 on 2022/01/28.
//

import XCTest

class Matrix_Diagonal_Sum: TestCase {
    override func testSolution() {
        XCTAssertEqual(sol.diagonalSum([[1,2,3],
                                        [4,5,6],
                                        [7,8,9]]), 25)
        XCTAssertEqual(sol.diagonalSum([[1,1,1,1],
                                        [1,1,1,1],
                                        [1,1,1,1],
                                        [1,1,1,1]]), 8)
        XCTAssertEqual(sol.diagonalSum([[5]]), 5)
        
        XCTAssertEqual(sol.refactor([[1,2,3],
                                        [4,5,6],
                                        [7,8,9]]), 25)
        XCTAssertEqual(sol.refactor([[1,1,1,1],
                                        [1,1,1,1],
                                        [1,1,1,1],
                                        [1,1,1,1]]), 8)
        XCTAssertEqual(sol.refactor([[5]]), 5)
    }
}

