def get_indices_of_item_weights(weights, length, limit):
    """
    UNDESTAND

    input: weights = [ 4, 6, 10, 15, 16 ], length = 5, limit = 21
    output: [ 3, 1 ]  

    input: [ 3, 10, 7, 21, 13], length = 5, limit = 23
    output: [ 4, 1 ]

    PLAN

    check the sum of each number with every other number
    save the sum in the sums dict if the two numbers not calculated yet
    check if the two numbers equal the limit, return indices [x, y] with x being the largest index
    
    """
    # Your code here
    x = 0
    y = 0

    while x < length - 1: # O(n)
        if x == y:
            y += 1
            continue

        if getSum(weights[x], weights[y]) == limit:
            if x >= y:
                return [x, y]
            else:
                return [y, x]
        
        y += 1

        if y == length:
            x += 1
            y = 0



    return None

sums = dict()

def getSum(x, y):
    if (x, y) in sums:
        return sums[(x, y)]

    sums[(x, y)] = x + y
    return sums[(x, y)]


print(get_indices_of_item_weights([ 3, 10, 7, 21, 13], 5, 23)) # ---> [4, 1]
