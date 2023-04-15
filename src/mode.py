from abc import ABC, abstractmethod

class Mode(ABC):
    """Base class for app modes"""
    @abstractmethod
    def handle_mode(self, args) -> None:
        pass


class PredictionMode(Mode):
    """Prediction mode"""
    def handle_mode(self, args) -> None:
        pass


class TrainingMode(Mode):
    """Training mode"""
    def handle_mode(self, args) -> None:
        pass


class UDCComparisonMode(Mode):
    """UDC comparison mode"""
    def handle_mode(self, args) -> None:
        pass
