"""
    This module defines the Validator interface.
"""

from .Rule import Rule


class Validator:
    """
        Validator is a contract for validating data.
        It's used by the Factory to validate the data before creating an Entity,
        the data is validated based on the rules defined by inheritance.
    """

    """
        Validates the data if not validated yet and returns if the data is valid.

        :return: True if the data is valid, False otherwise.
    """

    def isValid(self) -> bool:
        raise NotImplementedError('isValid method must be implemented')

    """
        Validates the data if not validated yet and returns the data if valid.
        If the data is not valid, it raises a ValidationException containing 
        the bag with the errors. The bag can be accessed through the exception
        instance.
        
        During the validation, the messages defined by the user are used if 
        available, otherwise the default messages provided by the rules are used.
        
        By default, the messages already contain placeholders, see :Rule: to more 
        information, for the attribute that are replaced by the name of the 
        attribute and the wrapper that are replaced by the wrapper of the attribute 
        by the Formatter instance in the validation process, so you don't need 
        to define them in the message.
        
        You can customize the replacement of the placeholders passing a custom
        Formatter instance to the Validator.
          
        :return: The data if valid.
        :raise ValidationException: If the data is not valid.
    """

    def validate(self) -> dict:
        raise NotImplementedError('validate method must be implemented')

    """
        Validates the data if not validated yet and returns a set 
        containing the errors if the data is not valid. If the data 
        is valid, it returns an empty set.
    """

    def errors(self) -> set[str, str]:
        raise NotImplementedError('errors method must be implemented')

    """
        Return the rules associated with the validator.
        
        :return: A dictionary containing the rules.
    """

    def rules(self) -> dict[str, list[Rule]]:
        raise NotImplementedError('rules method must be implemented')

    """
        If desired, you can define custom messages for the rules. The key
        is a combination between the name of attribute and the name of the
        rule, allowing more than one rule per attribute to be customized, 
        and the wrapper is the message.
        
        The is a string that can contain the placeholders. Prefer the built-in
        placeholders {attr} and {wrapper} to refer to the attribute name and
        the wrapper, respectively.
        
        :return: A dictionary containing the messages.
    """

    def messages(self) -> dict[str, str]:
        raise NotImplementedError('messages method must be implemented')
