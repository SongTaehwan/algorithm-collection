//
//  Merge_Strings_Alternately.swift
//  Merge Strings Alternately
//
//  Created by 송태환 on 2022/01/27.
//

import XCTest

class Merge_Strings_Alternately: TestCase {
    override func testSolution() {
        XCTAssertEqual(sol.mergeAlternately("abc", "pqr"), "apbqcr")
        XCTAssertEqual(sol.mergeAlternately("ab", "pqrs"), "apbqrs")
        XCTAssertEqual(sol.mergeAlternately("abcd", "pq"), "apbqcd")
        
        XCTAssertEqual(sol.refactor("abc", "pqr"), "apbqcr")
        XCTAssertEqual(sol.refactor("ab", "pqrs"), "apbqrs")
        XCTAssertEqual(sol.refactor("abcd", "pq"), "apbqcd")
    }
}
