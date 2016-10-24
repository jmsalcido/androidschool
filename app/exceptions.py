class UserNotFoundException(Exception):

    def __init__(self, message):
        super(UserNotFoundException, self).__init__(message)
        self.message = message
