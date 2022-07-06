//
//  Crane_Puppet_Draw_Game.swift
//  Crane Puppet Draw Game
//
//  Created by 송태환 on 2022/01/19.
//

import XCTest

class Crane_Puppet_Draw_Game: TestCase {

    func testSolution() {
        XCTAssertEqual(solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]], [1,5,3,5,1,2,1,4]), 4)
        XCTAssertEqual(solution([[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]], [1, 5, 3, 5, 1, 2, 1, 4]), 0)
    }

}
