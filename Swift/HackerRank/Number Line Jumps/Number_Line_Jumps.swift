//
//  Number_Line_Jumps.swift
//  Number Line Jumps
//
//  Created by 송태환 on 2022/01/26.
//

import XCTest

class Number_Line_Jumps: XCTestCase {
    func testSolution() {
        XCTAssertEqual(kangaroo(x1: 0, v1: 3,  x2: 4, v2: 2), "YES")
        XCTAssertEqual(kangaroo(x1: 0, v1: 2,  x2: 5, v2: 3), "NO")
        XCTAssertEqual(kangaroo(x1: 21, v1: 6,  x2: 47, v2: 3), "NO")
        XCTAssertEqual(kangaroo(x1: 28, v1: 8,  x2: 96, v2: 2), "NO")
        XCTAssertEqual(kangaroo(x1: 45, v1: 7,  x2: 56, v2: 2), "NO")
    }

}
