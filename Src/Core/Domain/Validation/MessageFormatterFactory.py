from Src.Core.Domain.Contracts.Factory import Factory as ContractFactory
from .MessageFormatter import MessageFormatter
from Src.Core.Domain.Exceptions import MissingParameter


class MessageFormatterFactory(ContractFactory):
    def __init__(self):
        self.__format = None
        self.__values = None

    def props(self, format: str, values: dict):
        if format is None:
            raise MissingParameter('format')

        if values is None:
            raise MissingParameter('values')

        self.__format = format
        self.__values = values

        return self

    def create(self):
        return MessageFormatter(self.__format, self.__values)
