def fibonacci(n):

    """
    This function returns the nth value of fibonacci series

    Input: integer (n)
    Output: fibonacci[n]
    """

    if n == 0:
        return 0
    if (n==1 or n ==2):
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def lucas(n):

    """
    This function returns the nth value of lucas series

    Input: integer (n)
    Output: lucas[n]
    """

    if n == 0:
        return 2
    if n==1 :
        return 1
    else:
        return lucas(n-1) + lucas(n-2)


def sum_series (n,first=0,second=1):
    """
    This function returns the nth value of user custom series in which each element is the sum of the previous two elements, first and second elements are user defined

    Input: integer, first element (integer) optional, second element (integer) optional
    Output: nth element of the resulting series
    """

    if n == 0:
        return first
    if n == 1 :
        return second
    else:
        return sum_series(n-1,first,second) + sum_series(n-2,first,second)
