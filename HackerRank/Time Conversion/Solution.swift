//
//  Solution.swift
//  Diagonal Difference
//
//  Created by 송태환 on 2022/01/26.
//

import Foundation

/// [Check out problem](https://www.hackerrank.com/challenges/time-conversion/problem)
func timeConversion(s: String) -> String {
    let period = s.suffix(2)
    var hourString = String(s.prefix(2))
    let hours = Int(hourString)!
    let result = String(s.dropLast(2).dropFirst(2))
    
    if period == "PM" {
        hourString = String(hours == 12 ? hours : hours + 12)
    } else if hours == 12 {
        hourString = "00"
    }
    
    return hourString + result
}
