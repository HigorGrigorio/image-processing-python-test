from typing import TypeVar, Generic, Self

T = TypeVar('T')


class Just(Generic[T]):
    def __init__(self, value: any):
        self.value = value


class Nothing:
    def __init__(self):
        pass


class Maybe(Generic[T]):
    def __init__(self, value: Just[T] | Nothing):
        self.wrapper = value

    def isJust(self) -> bool:
        return isinstance(self.wrapper, Just)

    def isNothing(self) -> bool:
        return isinstance(self.wrapper, Nothing)

    def get(self) -> T:
        if self.isJust():
            return self.wrapper.value
        else:
            raise Exception("Maybe.get() called on Nothing")

    def getOrElse(self, default: T) -> T:
        if self.isJust():
            return self.wrapper.value
        else:
            return default

    def map(self, func: callable) -> Self:
        if self.isJust():
            return self.just(func(self.wrapper.value))

    def flatten(self) -> Self:
        if self.wrapper.value is Maybe:
            return self.wrapper
        return self

    def __str__(self):
        if self.isJust():
            return f'Just {self.wrapper.value}'
        else:
            return 'Nothing'

    def __eq__(self, other):
        if not isinstance(other, Maybe):
            return False
        if self.isJust() and other.isJust():
            return self.wrapper.value == other.wrapper.value
        if self.isNothing() and other.isNothing():
            return True
        return False

    def __ne__(self, other):
        return not self.__eq__(other)

    def __bool__(self):
        return self.isJust()

    @staticmethod
    def nothing() -> 'Maybe':
        return Maybe(Nothing())

    @staticmethod
    def just(value: T) -> 'Maybe':
        return Maybe(Just(value))

    @staticmethod
    def flat(value: T) -> 'Maybe':
        return Maybe(Just(value)).flatten()
