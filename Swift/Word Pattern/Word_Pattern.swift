//
//  Word_Pattern.swift
//  Word Pattern
//
//  Created by 송태환 on 2022/01/17.
//

import XCTest

class Word_Pattern: TestCase {
    func testWordPattern() {
        XCTAssertEqual(sol.wordPattern("abba", "dog cat cat dog"), true)
        XCTAssertEqual(sol.wordPattern("abba", "dog cat cat fish"), false)
        XCTAssertEqual(sol.wordPattern("aaaa", "dog cat cat dog"), false)
        XCTAssertEqual(sol.wordPattern("abba", "dog dog dog dog"), false)
    }
}
