//
//  Solution.swift
//  Reverse Bits
//
//  Created by 송태환 on 2022/01/19.
//

import Foundation

func solution(_ s:String) -> String {
    var result = ""
    var index = 0
    
    for char in s {
        result += (index % 2 == 0 ? char.uppercased() : char.lowercased())
        index += 1
        
        if char == " " {
            index = 0
        }
    }
    
    return result
}
