//
//  Solution.swift
//  Build an Array With Stack Operations
//
//  Created by 송태환 on 2022/03/29.
//

import Foundation

class Solution {
    func buildArray2(_ target: [Int], _ n: Int) -> [String] {
        var numbers = target
        var result = [String]()
        
        for i in 1...target.max()! {
            let number = numbers.remove(at: 0)

            if i == number {
                result.append("Push")
            } else {
                result.append("Push")
                result.append("Pop")
                numbers.insert(number, at: 0)
            }
            
            if numbers.isEmpty {
                return result
            }
        }
        
        return result
    }
    
    func buildArray(_ target: [Int], _ n: Int) -> [String] {
        let set = Set(target)
        var result = [String]()
        
        for i in 1...target.last! {
            result.append("Push")
            
            if !set.contains(i) {
                result.append("Pop")
            }
        }
        
        return result
    }
}
