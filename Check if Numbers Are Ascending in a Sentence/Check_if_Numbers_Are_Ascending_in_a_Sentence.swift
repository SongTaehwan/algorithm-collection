//
//  Check_if_Numbers_Are_Ascending_in_a_Sentence.swift
//  Check if Numbers Are Ascending in a Sentence
//
//  Created by 송태환 on 2022/02/24.
//

import XCTest

class Check_if_Numbers_Are_Ascending_in_a_Sentence: TestCase {
    override func testSolution() {
        XCTAssertEqual(sol.areNumbersAscending("1 box has 3 blue 4 red 6 green and 12 yellow marbles"), true)
        XCTAssertEqual(sol.areNumbersAscending("sunset is at 7 51 pm overnight lows will be in the low 50 and 60 s"), false)
        
        XCTAssertEqual(sol.refactor("1 box has 3 blue 4 red 6 green and 12 yellow marbles"), true)
        XCTAssertEqual(sol.refactor("sunset is at 7 51 pm overnight lows will be in the low 50 and 60 s"), false)
    }
}

