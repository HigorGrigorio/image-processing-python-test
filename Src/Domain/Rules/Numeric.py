from Src.Core.Domain.Contracts.Rule import Rule as ContractRule
from Src.Core.Logic import Singleton


@Singleton
class Numeric(ContractRule):
    def isSatisfiedBy(self, value) -> bool:
        return value is not None and value != '' or type(value) is int or type(value) is float or type(value) is complex or type(str) is str and str.isnumeric(value)

    def message(self) -> str:
        return 'The {attr} field must be numeric'

    def name(self) -> str:
        return 'numeric'
