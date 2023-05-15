from .ErrorsBag import ErrorsBag


class ValidationException(Exception):
    def __init__(self, errorBag: ErrorsBag):
        self.errorBag = errorBag

    def errors(self) -> ErrorsBag:
        return self.errorBag

    def __str__(self):
        return str(self.errorBag)
