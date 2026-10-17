# Problem 1: CyclicRotation
# PseudoCode:

# Function solution_to_problem_one(A,K):
#     If length of A is 0:
#         Return A
#.    length <-- length of A
#     new_arr <-- array with size length filled with 0
#     movement <-- length - (K % length)
#     For i from 0 to length:
#        If i + movement is greater or equal to length:
#            calculate the new index by subtracting length from i + movement
#        Else:  
#           calculate the new index by adding i + movement
# return the new_arr
#
#

# Solution to problem 1:

# A represents an array and K represents a integer
def solution_to_problem_one(A,K):

    if len(A) == 0:
        return A

    length = len(A)
    new_arr = length * [0]

    movement = length - (K % length)

    for i in range(length):

        if i+movement >= length:
            new_arr[i] = A[i+movement - length]
        else:
            new_arr[i] = A[i+movement]

    return new_arr




# Problem 2: OddOccurrencesInArray
# PseudoCode:
# Function solution_to_problem_two(A):
#     If the length of A is equal to 0:
#         Return zero 
#     Sort array A

#     For i from 0 to length of (A - 1) with the step size of 2:
#         If index i of array A is not equal to index i + 1 of array A:
#             Return index i of array A

#     Return index of the last element of array A


# Solution to problem 2:
def solution_to_problem_two(A):
    if len(A) == 0:
        return 0

    A.sort()
    
    for i in range(0, len(A)-1,2): 
        if A[i] != A[i+1]:
            return A[i]
    return A[-1]




# Problem 3: FrogJmp
# PseudoCode:
# Function solution_to_problem_three(X,Y,D):
#     distance <-- Y - X
#     count <-- distance // D

#     If remainder of distance divided by D is not equal to 0:
#         count is added by 1

#     Return the total count

# Solution to problem 3:
def solution_to_problem_three(X, Y, D):
    distance = Y-X
    count = distance // D
    if distance % D != 0:
        count+=1

    return count




# Problem 4: PermMissingElem
# PseudoCode
# Function solution_to_problem_four(A):
#     length <-- length of array A
#     expected_length <-- length + 1
#     actual_sum <-- (1+expected_length) multiply by expected_length then divide 2

#     Return actual_sum - the sum of array A

# Solution to problem 4:
def solution_to_problem_four(A):
    length = len(A)
    expected_length = length + 1
    actual_sum = (1+expected_length) * expected_length // 2

    return actual_sum - sum(A)    


# Problem 5: PermCheck
# PseudoCode
# Function solution_to_problem_five(A):
#     If the length of the set of A is not equal to the length of A:
#         Return 0
#     length <-- length of A
#     sorted_a <-- sort array A
#     max_val <-- last element of sorted_a
#     actual_sum <-- (1+max_val) multiply by max_val then divide 2
#     If actual_sum - sum of A is equal to 0:
#         Return 1
#     Return 0

# Solution to problem 5:
def solution_to_problem_five(A):

    if len(set(A)) != len(A):
        return 0

    length = len(A)
    sorted_a = sorted(A)
    max_val = sorted_a[length-1]
    actual_sum = (1+max_val)*max_val // 2

    if(actual_sum - sum(A)) == 0:
        return 1
    return 0


