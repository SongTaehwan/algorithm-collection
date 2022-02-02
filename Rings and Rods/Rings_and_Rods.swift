//
//  Rings_and_Rods.swift
//  Rings and Rods
//
//  Created by 송태환 on 2022/02/02.
//

import XCTest

class Rings_and_Rods: TestCase {
    override func testSolution() {
        XCTAssertEqual(sol.countPoints("R3G2B1"), 0)
        XCTAssertEqual(sol.countPoints("B0B6G0R6R0R6G9"), 1)
        XCTAssertEqual(sol.countPoints("B0R0G0R9R0B0G0"), 1)
        XCTAssertEqual(sol.countPoints("G4"), 0)
    }
}

