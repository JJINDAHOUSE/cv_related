from nameko import config
from nameko.extensions import DependencyProvider

from region_counter.exceptions import NotFound

import cv2
import numpy as np

from ultralytics import YOLO
from ultralytics.utils.files import increment_path
from ultralytics.utils.plotting import Annotator, colors

from collections import defaultdict
from pathlib import Path


class CounterWrapper:
    """
    Object tracker
    """
    def __init__(self, weights, device):
        self.weights = weights
        self.device = device

    def capture(self):
        pass
    
    def predict_fn(self, frame:np.ndarray=None, classes:list[int]=None) -> list:
        model = YOLO(self.weights)
        model.to(self.device)
        return model.track(frame, persist=True, classes=classes)
    
    def output(self, results):
        pass



class Counter(DependencyProvider):
    """
    """
    def setup(self):
        self.weights = config.get(WEIGHTS)
        self.device = config.get(DEVICE)

    def get_dependency(self, worker_ctx):
        return CounterWrapper(self.weights, self.device)