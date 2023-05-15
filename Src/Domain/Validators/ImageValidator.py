from Src.Core.Domain.Validation import MessagesBag, MessageFormatterFactory, Validator
from Src.Domain.Rules.Required import Required
from Src.Domain.Rules.Numeric import Numeric


class ImageValidator(Validator):
    def __init__(
            self,
            data: dict,
            messages: MessagesBag = None,
            formatterFactory: MessageFormatterFactory = None
    ):
        super().__init__({
            'date': {Required()},
            'azimuth': {Required(), Numeric()},
            'sun_elevation': {Required(), Numeric()}
        }, messages, data, formatterFactory)

    @staticmethod
    def create(
            data: dict,
            messages: MessagesBag = None,
            formatterFactory: MessageFormatterFactory = None
    ):
        return ImageValidator(
            data,
            messages,
            formatterFactory
        )
