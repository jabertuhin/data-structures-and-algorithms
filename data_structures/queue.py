"""
This code was a part of a Udacity course[DS and Algorithms in python] Quiz.
"""


class Queue:
    def __init__(self, head=None):
        self.storage = [head]

    def enqueue(self, new_element):
        """"
        This method inserts object in the queue.
        """
        self.storage.append(new_element)

    def peek(self):
        """"
        This method returns the first object inserted in the queue.
        :return: object that was inserted in the queue.
        """
        return self.storage[0]

    def dequeue(self):
        """"
        This method returns the peek value of the queue and also removes it from queue.
        :return: object that was inserted in the queue.
        """
        return self.storage.pop(0)

    def size(self):
        """"
        This method returns the number of elements present in the queue.
        :return: numerical value(int type).
        """
        return len(self.storage)

    def empty(self):
        """"
        This method returns True if the queue is empty or False otherwise.
        :return: boolean value
        """
        if len(self.storage) > 0:
            return False
        else:
            return True