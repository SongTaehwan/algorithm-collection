//
//  Maximum_Depth_of_Binary_Tree.swift
//  Maximum Depth of Binary Tree
//
//  Created by 송태환 on 2022/02/15.
//

import XCTest

class Maximum_Depth_of_Binary_Tree: TestCase {
    override func testSolution() {
        let root1 = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
        XCTAssertEqual(sol.maxDepth(root1), 3)
        let root2 = TreeNode(1, nil, TreeNode(7))
        XCTAssertEqual(sol.maxDepth(root2), 2)
    }
}

