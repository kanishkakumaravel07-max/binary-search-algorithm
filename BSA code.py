def binary_search(arr, target): 
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid  # Target found, return index 
        elif arr[mid] < target:
            left = mid + 1 
        else:
            right = mid - 1
    return -1  # Target not found

# Get user input for array and target
arr = list(map(int, input("Enter sorted numbers separated by spaces: ").split()))
target = int(input("Enter the target number to search for its index: "))

# Ensure the array is sorted (just in case) 
arr.sort()

# Perform binary search
result = binary_search(arr, target)

# Display result 
if result != -1:
    print(f"Target found at index {result}") 
else:
    print("Target not found in the array")
