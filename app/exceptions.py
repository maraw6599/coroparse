class CoroparseException(Exception):
    pass

class NetworkException(CoroparseException):
    pass


class DatabaseException(CoroparseException):
    pass


class FormatException(CoroparseException):
    pass


class IOException(CoroparseException):
    pass
