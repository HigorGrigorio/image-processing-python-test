class ErrorsBag:
    def __init__(self):
        self.errors = dict[str, list[str]]()

    def addError(self, key, error):
        if key not in self.errors:
            self.errors[key] = []

        self.errors[key].append(error)

    def errors(self) -> dict[str, list[str]]:
        return self.errors

    def getErrors(self, key: str) -> list[str]:
        return self.errors[key]

    def hasError(self, key: str) -> bool:
        return key in self.errors

    def hasErrors(self) -> bool:
        return len(self.errors) > 0

    def count(self) -> int:
        return len(self.errors)

    # convert to string
    def __str__(self):
        return str(self.errors)
