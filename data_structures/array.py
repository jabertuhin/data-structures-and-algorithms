def right_shift(number_list):
    """
    Shifts right by one position.

    :param number_list: contains an array of any size.
    :return: right shifted array by one position.
    """

    temp = number_list[len(number_list) - 1]
    hold = number_list[0]
    for i in range(1, len(number_list), 1):
        temp_hold = number_list[i]
        number_list[i] = hold
        hold = temp_hold
    number_list[0] = temp
    return number_list
