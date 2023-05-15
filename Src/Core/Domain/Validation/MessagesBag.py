"""
    Defines a type alias for messages dictionary
"""

from typing import TypeAlias

"""
    MessagesBag is a dictionary of messages that can be used in the validation.
    The keys are the a combination of the attribute name and the rule name, and 
    the values are the messages that can contain placeholders for replacements.
"""

MessagesBag: TypeAlias = dict[str, str]
