//
//  Binary_Tree_Inorder_Traversal.swift
//  Binary Tree Inorder Traversal
//
//  Created by 송태환 on 2022/02/27.
//

import XCTest

class Binary_Tree_Inorder_Traversal: TestCase {
    override func testSolution() {
        var root = TreeNode() // null 처리하는 트리 생성함수 만들기
        XCTAssertEqual(sol.inorderTraversal(root), [1,3,2])
        
        var root = TreeNode()
        XCTAssertEqual(sol.inorderTraversal(root), [])
        
        var root = TreeNode(1)
        XCTAssertEqual(sol.inorderTraversal(root), [1])
    }
}

