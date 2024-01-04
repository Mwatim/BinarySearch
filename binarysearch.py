def binarySearch(list_of_numbers, target):
    """
    This function takes in a list of numbers and returns the target.

    Parameters:
    -List of numbers
    -Target

    Results:
    -Target index if it exists
    """
    (left, right) = (0, len(list_of_numbers) - 1)

    while left <= right:
        # mitigate integer overflow
        mid_value = left + (right - left) // 2
        if target == list_of_numbers[mid_value]:
            return mid_value
        
        elif target < list_of_numbers[mid_value]:
            return mid_value - 1
        
        else:
            left = mid_value + 1

    return -1

if __name__ == '__main__':
    list_of_numbers = [2,3,5,81,95,52,42,7,8,10,12,15,18,20]
    target = 52

    index = binarySearch(list_of_numbers, target)

    if index != -1:
        print(f"Element found at index {index}")
    else:
        print("Element not found in the list")