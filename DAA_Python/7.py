def calculate(num_set, req_sum):
    sublists = get_sublists(num_set)
    solutionLists = []
    solutions = 0
    for i in sublists:
        if sum(i) == req_sum:
            solutions += 1
            solutionLists.append(i)

    return solutionLists, solutions


def get_sublists(num_set):
    from itertools import combinations

    lists = []
    for i in range(len(num_set) + 1):
        lists += [list(j) for j in combinations(num_set, i)]

    return lists


numset = input("Enter the elements: ").split()
numset = [int(i) for i in numset]

req_sum = int(input("Sum required: "))
solutionsLists, solutions = calculate(numset, req_sum)
print(f"Number of Solutions: {solutions}")
print(f"Solution Subsets are: {solutionsLists}")