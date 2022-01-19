//
//  Nth_Number.swift
//  Nth Number
//
//  Created by 송태환 on 2022/01/19.
//

import XCTest

class Nth_Number: TestCase {
    func testSolution() {
        XCTAssertEqual(solution([1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]]), [5, 6, 3])
    }

}
