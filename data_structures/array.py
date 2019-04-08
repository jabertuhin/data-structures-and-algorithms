def right_shift(array):
    """
    Shifts right by one position.

    :param array: contains an array of any size.
    :return: right shifted array by one position.
    """

    # support for empty or one element array
    if 0 <= len(array) <= 1:
        return array[:]

    temp = array[-1]
    hold = array[0]
    for i in range(1, len(array), 1):
        temp_hold = array[i]
        array[i] = hold
        hold = temp_hold
    array[0] = temp
    return array
