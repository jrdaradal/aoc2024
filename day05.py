# 2024 Advent of Code Day 04 Solution
# John Roy Daradal 

# SolutionA: 7024
# SolutionB: 4151

from utils import * 

rule = tuple[int,int]

def input05(full: bool) -> tuple[list[rule], list[list[int]]]:
    rules: list[rule] = []
    pages: list[list[int]] = []
    part2 = False 
    for line in readLines(getPath(5, full)):
        if part2:
            pages.append([int(x) for x in line.split(',')])
        elif line == '':
            part2 = True
        else:
            a,b = [int(x) for x in line.split('|')]
            rules.append((a,b))
    return rules, pages

def day05A():
    full = True 
    rules, pages = input05(full)
    rules = ruleBook(rules) 
    total = 0 
    for numbers in pages:
        if isValid(numbers, rules):
            total += mid(numbers)
    print(total)

def day05B():
    full = True 
    rules, pages = input05(full)
    rules = ruleBook(rules)
    total = 0 
    for numbers in pages:
        numbers, valid = correctOrder(numbers, rules)
        if not valid:
            total += mid(numbers)
    print(total)

def mid(numbers: list[int]) -> int:
    idx = len(numbers) // 2 
    return numbers[idx]

def ruleBook(rules: list[rule]) -> dict[int,set[int]]:
    book: dict[int,set[int]] = {}
    for before, after in rules:
        book.setdefault(after, set())
        book[after].add(before)
    return book 

def isValid(numbers: list[int], rules: dict[int,set[int]]) -> bool:
    for i in range(0, len(numbers)-1):
        after = set(numbers[i+1:])
        blacklist = rules.get(numbers[i], set())
        common = after.intersection(blacklist)
        if len(common) > 0:
            return False 
    return True

def correctOrder(numbers: list[int], rules: dict[int,set[int]]) -> tuple[list[int], bool]:
    valid = True 
    idx, limit = 0, len(numbers)-1
    while idx < limit:
        curr = numbers[idx]
        after = set(numbers[idx+1:])
        blacklist = rules.get(curr, set())
        common = after.intersection(blacklist)
        if len(common) == 0:
            idx += 1
        else:
            valid = False 
            insert = max(numbers.index(x) for x in common) + 1
            numbers[idx] = None 
            numbers = numbers[:insert] + [curr] + numbers[insert:]
            numbers.remove(None)
    return numbers, valid

if __name__ == '__main__':
    day05A()
    day05B()