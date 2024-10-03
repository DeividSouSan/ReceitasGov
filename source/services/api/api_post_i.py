import json
import logging
import os
from abc import ABC, abstractmethod

import requests


class APIPostI(ABC):
    @abstractmethod
    def post_data(self, url: str) -> None:
        pass
