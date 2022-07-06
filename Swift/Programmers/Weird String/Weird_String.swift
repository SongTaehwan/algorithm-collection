//
//  Weird_String.swift
//  Weird String
//
//  Created by 송태환 on 2022/01/19.
//

import XCTest

class Weird_String: TestCase {

    func testSolution() {
        XCTAssertEqual(solution("try hello world"), "TrY HeLlO WoRlD")
        XCTAssertEqual(solution("hello from the other side"), "HeLlO FrOm ThE OtHeR SiDe")
    }

}
