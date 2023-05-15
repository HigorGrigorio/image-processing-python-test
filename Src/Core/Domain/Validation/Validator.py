from Src.Core.Domain.Contracts.Validator import Validator as ContractValidator
from Src.Core.Domain.Validation.ValidationException import ValidationException, ErrorsBag
from Src.Core.Domain.Exceptions.MissingParameter import MissingParameter
from .MessageFormatterFactory import MessageFormatterFactory
from .RulesBag import RulesBag
from .MessagesBag import MessagesBag

"""
    
"""


class Validator(ContractValidator):
    def __init__(
            self,
            rules: RulesBag,
            messages: MessagesBag,
            data: dict,
            formatterFactory: MessageFormatterFactory = None
    ):
        self.__formatterFactory = formatterFactory if formatterFactory is not None else MessageFormatterFactory()
        self.__messages = messages if messages is not None else MessagesBag()

        if rules is None:
            raise RuntimeError('rules is None')

        self.__rules = rules

        if data is None:
            raise RuntimeError('data is None')

        self.__data = data
        self.__bag = None

    """
        Validates the data only if it has not been validated before.
    """

    def __validate(self):
        # If the bag is None, it means that the data has not been validated before.
        if self.__bag is None:
            self.__bag = ErrorsBag()

            for attr in self.__rules.keys():
                for rule in self.__rules[attr]:
                    if not rule.isSatisfiedBy(self.__data[attr]):
                        # Select the format from the messages dictionary if it exists
                        name = attr + '.' + rule.name()

                        message = self.__messages[name] if name in self.__messages.keys() else rule.message()

                        # Make a formatter for replacing the placeholders in the message
                        formatter = self.__formatterFactory.props(
                            message,
                            {
                                'attr': attr,
                                'wrapper': self.__data[attr]
                            }
                        ).create()

                        # Add the error to the error bag
                        self.__error(attr, formatter.format())

                        # Stop validating the attribute if the rule is not satisfied
                        break

    def __attribute(self, attr):
        if attr in self.__data:
            return self.__data[attr]
        raise MissingParameter(attr)

    def __error(self, key: str, message: str):
        self.__bag.addError(key, message)

    def rules(self) -> RulesBag:
        return self.__rules

    def messages(self) -> MessagesBag:
        return self.__messages

    def isValid(self) -> bool:
        self.__validate()
        return not self.__bag.hasErrors()

    def validate(self) -> dict:
        self.__validate()

        if self.__bag.hasErrors():
            raise ValidationException(self.__bag)

        return self.__data

    def errors(self) -> set:
        return self.__bag.errors()
