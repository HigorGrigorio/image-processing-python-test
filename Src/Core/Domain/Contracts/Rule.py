"""
    The Rule interface defines the contract for a rule used by the Validator.
"""


class Rule:
    """
        Rule is a contract for a rule used by the Validator. It's used by the
        Validator to validate the data before creating an Entity, the data is
        validated based on the rules that are passed to the Validator.

        For each attribute, a list of rules can be defined. If the data is not
        valid, the Validator will return a ValidationException containing the
        bag with the errors. The bag can be accessed through the exception
        instance.

        The Rule interfaces defines a unique name for the rule, the name is used
        to identify the rule in the Validator. This interface also defines
        a method to check if the rule is satisfied by the wrapper and a method to
        return the message of the rule.
    """

    """
        Return the name of the rule.

        :return: The name of the rule.
    """

    def name(self) -> str:
        raise NotImplementedError('name method must be implemented')

    """
        Check if the rule is satisfied by the wrapper.
        
        :param wrapper: The wrapper to be checked.
        
        :return: True if the rule is satisfied, False otherwise.
        
    """

    def isSatisfiedBy(self, value) -> bool:
        raise NotImplementedError('isSatisfiedBy method must be implemented')

    """
        Return the message of the rule. By default, the message already
        contains placeholders for the attribute and the wrapper, so you don't
        need to define them in the message.
        
        The placeholders are:
            - {attribute}: The name of the attribute.
            - {wrapper}: The wrapper of the attribute.
        
        :return: The message of the rule.
        
    """

    def message(self) -> str:
        raise NotImplementedError('message method must be implemented')
