"""
    Defines a type alias for rules dictionary
"""

from Src.Core.Domain.Contracts.Rule import Rule
from typing import TypeAlias

"""
    RulesBag is a dictionary of rules for each attribute of a class.
"""
RulesBag: TypeAlias = dict[str, set[Rule]]
