def intersection(arrays):
    """
    YOUR CODE HERE
    """
    # Your code here
    
    length = len(arrays)
    cache = {}
    result = []
    
    # store elements in first array in cache
    for integer in arrays[0]:
        cache[integer] = 0
    
    # check if items in cache
    for array in arrays:
        for integer in array:
            if integer in cache:
                cache[integer] += 1

    for item in cache:
        if cache[item] == length:
            result.append(item)

    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
