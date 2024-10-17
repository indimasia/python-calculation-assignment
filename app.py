def calculate(list_of_integer):
    min_value = min(list_of_integer)
    max_value = max(list_of_integer)
    odd = [value for value in list_of_integer if value % 2 != 0]
    
    return {
        'listOfInteger': list_of_integer,
        'min': min_value,
        'max': max_value,
        'odd': odd
    }

# Example usage
calculate_result = calculate([1,5,4,3,2,4,5,5])
print(calculate_result)
