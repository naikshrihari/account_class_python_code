class AgeException(Exception):
    def __init__(self, msg="Age is not in range"):
        self.__msg=msg

    def __str__(self):
        return self.__msg

class RemainBalanceException(Exception):
    def __init__(self, msg="Amount is less than min amount condition"):
        self.__msg=msg
    def __str__(self):
        return self.__msg
