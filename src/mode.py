"""
This module defines data classes for different modes of an app.
The classes are used to store mode-specific information in a structured way.
"""
from abc import ABC
from dataclasses import dataclass, field
from typing import Optional, Final

@dataclass
class Mode(ABC):
    """Base class for app modes"""
    model_filename: str
    text_filename: str
    mode_name: Final[str] = ''

@dataclass
class PredictionMode(Mode):
    """Prediction mode"""
    mode_name: Final[str] = 'prediction'

@dataclass
class TrainingMode(Mode):
    """Training mode"""
    mode_name: Final[str] = 'training'
    new_model_filename: Optional[str] = None

@dataclass
class UDCComparisonMode(Mode):
    """Training mode"""
    mode_name: Final[str] = 'training'
    udc: Optional[str] = None
