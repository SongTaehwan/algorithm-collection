//
//  Palindrome_Number.swift
//  Palindrome Number
//
//  Created by 송태환 on 2022/01/13.
//

import XCTest
@testable import algorithms

/// [Check out the problem](https://leetcode.com/problems/palindrome-number/)
class Palindrome_Number: TestCase {
    func testNumberIsPalindrome() {
        XCTAssertEqual(sol.isPalindrome(123), false)
        XCTAssertEqual(sol.isPalindrome(121), true)
        XCTAssertEqual(sol.isPalindrome(10), false)
        XCTAssertEqual(sol.isPalindrome(-121), false)
    }
}
