//
//  Lucky_Numbers_in_a_Matrix.swift
//  Lucky Numbers in a Matrix
//
//  Created by 송태환 on 2022/02/11.
//

import XCTest

class Lucky_Numbers_in_a_Matrix: TestCase {
    override func testSolution() {
        XCTAssertEqual(sol.luckyNumbers([
            [3,7,8],
            [9,11,13],
            [15,16,17]
        ]), [15])
        XCTAssertEqual(sol.luckyNumbers([
            [1,10,4,2],
            [9,3,8,7],
            [15,16,17,12]
        ]), [12])
        XCTAssertEqual(sol.luckyNumbers([
            [7,8],
            [1,2]
        ]), [7])
        XCTAssertEqual(sol.luckyNumbers([
            [3,6],
            [7,1],
            [5,2],
            [4,8]
        ]), [])
    }
}

