
def mulofmn(num1 : int, num2 : int, limit: int) -> int:
    """
        This function returns the number of multiples of two numbers m and n between a certain limit
    Args:
        num1 (int):
        num2 (int):
        limit (int)
    Returns:
        int:
    """    
    count_num1 = limit//num1
    count_num2 = limit//num2
    count_num1_num2 = limit//(num1*num2)
    count = count_num1+count_num2-count_num1_num2
    return count
