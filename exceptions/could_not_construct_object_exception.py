class CouldNotConstructObjectException(Exception):
    def __init__(self, message):
        if message:
            super().__init__("Critical Error: " + message + " object could not be constructed!")
        else:
            super().__init__("Critical Error: Could not construct object!")
