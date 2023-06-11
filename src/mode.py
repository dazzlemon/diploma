"""Data classes for app modes"""
from abc import ABC
from dataclasses import dataclass
from udc_code import UdcCode
from keywords import Keywords

@dataclass
class Mode(ABC):
    """Base class for app modes"""
    model_filename: str
    text_filename: str

@dataclass
class PredictionMode(Mode):
    """Prediction mode"""

@dataclass
class UDCComparisonMode(Mode):
    """Prediction and udc comparison mode"""
    udc: UdcCode

@dataclass
class TrainingMode(Mode):
    """Training mode"""
    new_model_filename: str
    udc: UdcCode
    keywords: Keywords
