def comparar(num1, num2, num3):
    """

    :param num1: int
    :param num2: int
    :param num3: int
    :return: int
    """
    if num1>num2:
        if num1>num3:
            return(1)
    if num2>num1:
        if num2>num3:
            return(2)
    if num3>num1:
        if num3>num2:
            print(var)
            return(3)
    return(0)
