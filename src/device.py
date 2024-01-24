import abc


class Device(abc.ABC):
    @abc.abstractmethod
    def parse(self, command):
        raise NotImplementedError
