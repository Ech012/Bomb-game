class TamperError(Exception):

    def __init__(self, msg):
        super().__init__(msg)
        self.msg = msg

    def __str__(self):
        return f"{self.msg}"


