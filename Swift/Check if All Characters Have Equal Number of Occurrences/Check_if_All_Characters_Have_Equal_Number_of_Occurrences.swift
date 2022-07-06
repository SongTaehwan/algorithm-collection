//
//  Check_if_All_Characters_Have_Equal_Number_of_Occurrences.swift
//  Check if All Characters Have Equal Number of Occurrences
//
//  Created by 송태환 on 2022/01/20.
//

import XCTest

class Check_if_All_Characters_Have_Equal_Number_of_Occurrences: TestCase {
    override func testSolution() {
        XCTAssertEqual(sol.areOccurrencesEqual("abacbc"), true)
        XCTAssertEqual(sol.areOccurrencesEqual("aaabb"), false)
        XCTAssertEqual(sol.refactored("abacbc"), true)
        XCTAssertEqual(sol.refactored("aaabb"), false)
    }
}
