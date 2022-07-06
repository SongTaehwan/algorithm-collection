//
//  Time_Conversion.swift
//  Time Conversion
//
//  Created by 송태환 on 2022/01/26.
//

import XCTest

class Time_Conversion: XCTestCase {
    func testSolution() {
        XCTAssertEqual(timeConversion(s: "07:05:45PM"), "19:05:45")
        XCTAssertEqual(timeConversion(s: "12:05:45AM"), "00:05:45")
    }

}
