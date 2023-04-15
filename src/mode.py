"""Data classes for app modes"""
from abc import ABC
from dataclasses import dataclass
from typing import Optional, Final

@dataclass
class Mode(ABC):
    """Base class for app modes"""
    model_filename: str
    text_filename: str
		# idk what's the problem with this class
    # pylint: disable=invalid-name
    mode_name: Final[str] = ''

@dataclass
class PredictionMode(Mode):
    """Prediction mode"""
    mode_name: Final[str] = 'Prediction'

@dataclass
class UDCComparisonMode(Mode):
    """Prediction and udc comparison mode"""
    mode_name: Final[str] = 'Prediction and udc comparison'
    udc: Optional[str] = None

@dataclass
class TrainingMode(Mode):
    """Training mode"""
    mode_name: Final[str] = 'Training'
    new_model_filename: Optional[str] = None
