from Src.Core.Domain.Contracts.Rule import Rule as ContractRule
from Src.Core.Logic import Singleton


@Singleton
class Required(ContractRule):
    def message(self) -> str:
        return 'The {attr} field is required'

    def isSatisfiedBy(self, value) -> bool:
        if value is None:
            return False

        if type(value) is str:
            return len(value.strip()) > 0

        # check for sized values
        if hasattr(value, '__len__'):
            return len(value) > 0

        return True

    def name(self) -> str:
        return 'required'
