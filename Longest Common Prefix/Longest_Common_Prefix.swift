//
//  Longest_Common_Prefix.swift
//  Longest Common Prefix
//
//  Created by 송태환 on 2022/01/13.
//

import XCTest

/// [Check out the problem](https://leetcode.com/problems/longest-common-prefix/)
class Longest_Common_Prefix: TestCase {
    func testLongestCommonPrefix() {
        XCTAssertEqual(sol.longestCommonPrefix(["flower","flow","flight"]), "fl")
        XCTAssertEqual(sol.longestCommonPrefix(["dog","racecar","car"]), "")
    }
}
