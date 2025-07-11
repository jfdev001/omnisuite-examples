"""Classes for reading and post processing data."""

from abc import ABC, abstractmethod
from omnisuite_examples.grid import Grid2D


class AbstractReader(ABC):
    """Abstract class for reading and post processing (e.g., weather) data."""
    @abstractmethod
    def read(self):
        raise NotImplementedError

    @abstractmethod
    def postprocess(self):
        raise NotImplementedError

    @property
    @abstractmethod
    def grid(self) -> Grid2D:
        raise NotImplementedError
