//
//  Solution.swift
//  Maximum Depth of Binary Tree
//
//  Created by 송태환 on 2022/02/15.
//

import Foundation
/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     public var val: Int
 *     public var left: TreeNode?
 *     public var right: TreeNode?
 *     public init() { self.val = 0; self.left = nil; self.right = nil; }
 *     public init(_ val: Int) { self.val = val; self.left = nil; self.right = nil; }
 *     public init(_ val: Int, _ left: TreeNode?, _ right: TreeNode?) {
 *         self.val = val
 *         self.left = left
 *         self.right = right
 *     }
 * }
 */

/// [Check out the problem](https://leetcode.com/problems/maximum-depth-of-binary-tree/)
class Solution {
    func maxDepth(_ root: TreeNode?) -> Int {
        guard let root = root else { return 0 }

        let left = maxDepth(root.left)
        let right = maxDepth(root.right)

        return max(left, right) + 1
    }
}
