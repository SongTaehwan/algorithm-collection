//
//  Count_of_Matches_in_Tournament.swift
//  Count of Matches in Tournament
//
//  Created by 송태환 on 2022/02/07.
//

import XCTest

class Count_of_Matches_in_Tournament: TestCase {
    override func testSolution() {
        XCTAssertEqual(sol.numberOfMatches(7), 6)
        XCTAssertEqual(sol.numberOfMatches(14), 13)
        XCTAssertEqual(sol.refactor(7), 6)
        XCTAssertEqual(sol.refactor(14), 13)
    }
}

