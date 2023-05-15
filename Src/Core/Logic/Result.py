"""
    The Result interface is used to define the contract for the Result class.
"""

from typing import TypedDict, TypeVar, Generic, Self


class Error(TypedDict):
    type: str
    message: str


class Reason(TypedDict):
    message: str
    error: Error


def reason(message: str = '', error=None) -> Reason:
    if error is None:
        return Reason(message=message, error={message: '', error: ''})

    return {
        'message': message,
        'error': {
            'type': error['type'],
            'message': error['message']
        }
    }


T = TypeVar('T')


class Result(Generic[T]):
    def __init__(self, value: T = None, rea: Reason = None, isFailure: bool = False):
        if isFailure and value is not None:
            raise RuntimeError('Cannot create a failure result with a wrapper')

        if not isFailure and rea is not None:
            raise RuntimeError('Cannot create a successful result with a reason')

        self.__value = value
        self.__reason = rea
        self.__isFailure = isFailure

    def isFailure(self):
        return self.__isFailure

    def isSuccess(self):
        return not self.__isFailure

    def getReason(self) -> Reason:
        if self.isSuccess():
            raise RuntimeError('Cannot get reason from a successful result')
        return self.__reason

    def getValue(self) -> T:
        if self.isFailure():
            raise RuntimeError('Cannot get wrapper from a failed result')
        return self.__value


def success(value: T = None) -> Result[T]:
    return Result(value)


def fail(rea: Reason | dict) -> Result:
    if type(rea) is dict:
        rea = reason(message=rea['message'], error=rea['error'])
    return Result(rea=rea, isFailure=True)
