//
//  Palindrome_Number_Test.swift
//  Palindrome Number Test
//
//  Created by 송태환 on 2022/01/13.
//

import XCTest
@testable import algorithms

class Palindrome_Number: XCTestCase {
    var sol: Solution!

    override func setUpWithError() throws {
        try super.setUpWithError()
        sol = Solution()
    }

    override func tearDownWithError() throws {
        try super.tearDownWithError()
        sol = nil
    }

    func testNumberIsPalindrome() {
        XCTAssertEqual(sol.isPalindrome(123), false)
        XCTAssertEqual(sol.isPalindrome(121), true)
        XCTAssertEqual(sol.isPalindrome(10), false)
        XCTAssertEqual(sol.isPalindrome(-121), false)
    }
}
