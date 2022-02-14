//
//  Solution.swift
//  Remove Duplicates from Sorted List
//
//  Created by 송태환 on 2022/01/13.
//

import Foundation
import XCTest

class TestCase: XCTestCase {
    var sol: Solution!
    
    override func setUpWithError() throws {
        try super.setUpWithError()
        sol = Solution()
    }
    
    override func tearDownWithError() throws {
        try super.tearDownWithError()
        sol = nil
    }
    
    func testSolution() {}
}

class Utility {
    // MARK: - Static method
    static func createListNode(_ data: [Int]) -> ListNode {
        let head = ListNode(data[0])
        
        var tail: ListNode? = head
        
        var count = data.count
        
        while count != 0 {
            tail = tail?.next ?? tail
            count -= 1
        }
        
        for i in 1..<data.count {
            let node = ListNode(data[i])
            tail!.next = node
            tail = node
        }
        
        return head
    }
    
    static func getNodeResult(_ head: ListNode?) -> [Int] {
        var result = [Int]()
        var node: ListNode? = head
        
        while node != nil {
            result.append(node!.val)
            node = node?.next
        }
        
        return result
    }
}

class ListNode {
    var val: Int = 0
    var next: ListNode?
    
    init(_ val: Int) {
        self.val = val
        self.next = nil
    }
    
    init(_ val: Int, _ next: ListNode?) {
        self.val = val
        self.next = next
    }
}

class LinkedList<T: ListNode> {
    private(set) var head: T?
    private(set) var tail: T?
    
    var count: Int {
        var node = self.head
        var count = 1
        
        while let next = node?.next {
            node = next as? T
            count += 1
        }
        
        return count
    }
    
    init(head: T) {
        self.head = head
        self.tail = self._getTail(head)
    }
    
    private func _getTail(_ head: T) -> T {
        var node = head
        
        while let next = node.next {
            node = next as! T
        }
        
        return node
    }
    
    func findNode(at: Int) -> T? {
        var node = head
        var count = 0
        
        while count != at, let next = head?.next {
            node = next as? T
            count += 1
        }
        
        return node
    }
}

class TreeNode {
    var val: Int
    var left: TreeNode?
    var right: TreeNode?
    
    init() {
        self.val = 0
        self.left = nil
        self.right = nil
    }
    
    init(_ val: Int) {
        self.val = val
        self.left = nil
        self.right = nil
    }
    
    init(_ val: Int, _ left: TreeNode?, _ right: TreeNode?) {
        self.val = val
        self.left = left
        self.right = right
    }
}

func addLeaves(root: TreeNode, value: Int) {
    guard let node = value > root.val ? root.right : root.left else {
        if value > root.val {
            root.right = TreeNode(value)
        } else {
            root.left = TreeNode(value)
        }
        
        return
    }
    
    return addLeaves(root: node, value: value)
}

func createTree(_ numbers: [Int]) -> TreeNode {
    let root = TreeNode(numbers[0])
    
    for number in numbers[1...] {
        addLeaves(root: root, value: number)
    }
    
    return root
}
