//
//  Number_of_Strings_That_Appear_as_Substrings_in_Word.swift
//  Number of Strings That Appear as Substrings in Word
//
//  Created by 송태환 on 2022/03/31.
//

import XCTest

class Number_of_Strings_That_Appear_as_Substrings_in_Word: TestCase {
    override func testSolution() {
        XCTAssertEqual(sol.numOfStrings(["a","abc","bc","d"], "abc"), 3)
        XCTAssertEqual(sol.numOfStrings(["a","b","c"], "aaaaabbbbb"), 2)
        XCTAssertEqual(sol.numOfStrings(["a","a","a"], "ab"), 3)
    }
}

