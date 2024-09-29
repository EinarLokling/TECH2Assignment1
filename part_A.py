"""
TECH2 mandatory assignment - Part A

Write the implementation of part A of the exercise below.
"""

def std_loops(values):
    """
    Compute standard deviation of x using loops.

    Parameters
    ----------
    values: Sequence of numbers

    Returns
    -------
    sd : float
        Standard deviation of the list of numbers.
    """

    N = 0
    
    for i in values:
        N += 1
    
    total_sum = 0
    
    for i in range(N):
        total_sum += values[i]
        
    mean = total_sum / N
    
    sum_squared_diff = 0
    
    for i in range(N):
        sum_squared_diff += (values[i] - mean)**2
        
    variance = sum_squared_diff / N
    
    standard_deviation = variance**(1/2)
    
    return standard_deviation

def std_builtin(values):
    """
    Compute standard deviation of x using the built-in functions sum()
    and len().

    Parameters
    ----------
    values: Sequence of numbers

    Returns
    -------
    sd : float
        Standard deviation of the list of numbers.
    """
    
    N = len(values)

    mean = sum(values) / N

    sum_squared_diff = sum((values - mean) ** 2 for values in values)

    variance = sum_squared_diff / N

    standard_deviation = (variance) ** (1/2)

    return standard_deviation