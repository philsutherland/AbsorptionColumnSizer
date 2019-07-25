class RangeLimitException:
    def __init__(self, message):
        if message:
            super().__init__("Critical Error: " + message + " is out of acceptable range!")
        else:
            super().__init__("Critical Error: Value is out of acceptable range!")
