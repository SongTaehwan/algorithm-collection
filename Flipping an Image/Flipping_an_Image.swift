//
//  Flipping_an_Image.swift
//  Flipping an Image
//
//  Created by 송태환 on 2022/01/28.
//

import XCTest

class Flipping_an_Image: TestCase {
    override func testSolution() {
        XCTAssertEqual(sol.flipAndInvertImage([[1,1,0],[1,0,1],[0,0,0]]), [[1,0,0],[0,1,0],[1,1,1]])
        XCTAssertEqual(sol.flipAndInvertImage([[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]), [[1,1,0,0],[0,1,1,0],[0,0,0,1],[1,0,1,0]])
    }
}

