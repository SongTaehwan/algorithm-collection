//
//  Find_the_Highest_Altitude.swift
//  Find the Highest Altitude
//
//  Created by 송태환 on 2022/02/09.
//

import XCTest

class Find_the_Highest_Altitude: TestCase {
    override func testSolution() {
        XCTAssertEqual(sol.largestAltitude([-5, 1, 5, 0, -7]), 1)
        XCTAssertEqual(sol.largestAltitude([-4, -3, -2, -1, 4, 3, 2]), 0)
    }
}
