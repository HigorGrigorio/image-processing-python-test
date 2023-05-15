from Src.Core.Domain.Contracts.Formatter import Formatter as ContractFormatter


# Parse a message with a given format, replacing the attributes with the given values
class MessageFormatter(ContractFormatter):
    def __init__(self, replacer: str, values: dict = None):
        self.replacer = replacer
        self.values = values
        self.parsed = None

    def result(self) -> str:
        return self.parsed

    def attributes(self) -> set:
        return set(self.values.keys())

    def __value(self, attr: str) -> str:
        if attr in self.attributes():
            return self.values[attr]
        raise Exception(f'Placeholder {attr} not found in message format')

    def format(self) -> str:
        if self.parsed is None:
            self.parsed = self.replacer
            for placeholder in self.attributes():
                self.parsed = self.parsed.replace('{' + placeholder + '}', self.__value(placeholder))
        return self.parsed
