
# 📘 Day 34: Allocate Minimum Pages
## Problem Statement:
Given an array arr[] where each element represents the number of pages in a book, and an integer k representing the number of students, allocate books such that:

- Each student gets at least one book.

- Allocation is contiguous.

- No book is assigned to more than one student.

- The goal is to minimize the maximum number of pages assigned to any student.

- Return -1 if allocation isn’t possible.

## ✅ Approach
- Use Binary Search to minimize the maximum pages any student can get.

- The search space is between max(arr) and sum(arr).

- For each midpoint (mid), check if it's possible to allocate books within that limit.

- If yes, try for a smaller max; if not, try a larger one.

## 🧠 Key Concepts
- Greedy check to see if k students can be assigned with current mid as max.

- Binary Search to optimize the max pages.

## 📊 Complexity
- Time Complexity: O(N log S) where N is number of books, and S = sum(arr) - max(arr)

- Space Complexity: O(1)    
