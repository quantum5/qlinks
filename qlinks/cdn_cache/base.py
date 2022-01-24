import abc


class BaseCDNCache(abc.ABC):
    @abc.abstractmethod
    def __init__(self): ...

    @abc.abstractmethod
    def purge(self, url: str) -> None: ...
