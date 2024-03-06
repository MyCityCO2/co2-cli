import time
from abc import ABC, abstractmethod
from typing import Dict, List

import pandas
from loguru import logger


def timer(fn):
    """This decorator allow you to get the time the function take to run. Not useful in prod, but it is in dev."""

    def wrapper(self, *args, **kwargs):
        start_time = time.perf_counter()
        function = fn(self, *args, **kwargs)
        end_time = time.perf_counter()

        final_time = end_time - start_time

        logger.debug(
            f"{fn.__name__} took {final_time} secondes / {final_time / 60} minutes to execute"
        )

        return function

    return wrapper


class AbstractFormatter(ABC):
    def __init__(self):
        self._cities: List[Dict[str, str]] = None
        self._chart_of_account: List[List[Dict[str, str]]] = None
        self._accounting_data: List[Dict[str, str]] = None

    @abstractmethod
    def get_cities(self) -> List[Dict[str, str]]:
        """This need to return an list of dict with three value inside: name, chart_of_account and identifier. Name equal the name of the city, chart_of_account equal to the account set from gen_account_account_data (should be the set's name) and identifier equal the identifier number of the city, it can be and unique id or anything like that"""
        raise NotImplementedError()

    @abstractmethod
    def gen_account_account_data(self) -> List[List[Dict[str, str]]]:
        """This need to return an list of an list of dict with two value inside: name and code. Name equal the name of the account and code equal the identifier of the account. You can have multiple chart of account."""
        raise NotImplementedError()

    @abstractmethod
    def get_account_move(self):
        # TODO: make an docstring for this function
        # {'city': 'Abondance', 'chart_of_account': 'M14', 'identifier': '217400019', 'account': '74834', 'currency': 'EUR', 'date': '2010-12-31', 'debit': 0.0, 'credit': 16395.0}
        raise NotImplementedError()

    @property
    def cities(self) -> pandas.DataFrame:
        if not self._cities:
            self._cities = self.get_cities()
        return pandas.DataFrame(self._cities)

    @property
    def account_move(self):
        if not self._accounting_data:
            self._accounting_data = self.get_account_move()
        return pandas.DataFrame(self._accounting_data)
