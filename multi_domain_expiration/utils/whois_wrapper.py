"""
This module gets and parses results from python-whois library.
"""
import socket
from dataclasses import dataclass
from datetime import datetime
from typing import Union, Generator, Any

import whois
from whois.parser import PywhoisError

from .config import Config


@dataclass
class WhoisWrapper:
    """
    Whois wrapper to get and to parse results from python-whois library.
    """
    targets: Generator

    @classmethod
    def get_results(cls, targets: Generator) -> list[dict[str, str]]:
        """
        Method to create object and get results.
        :param targets: generator which returns a row containing domain name from input file.
        :return: list[dict[str, str]] results in dictionary containing results.
        """
        obj: 'WhoisWrapper' = cls(targets=targets)
        return [obj.clean_result(result) for target in obj.targets
                if (result := obj.is_registered(obj._clean_target(target)))]

    def clean_result(self, result: whois) -> dict[str, str]:
        """
        Method to clean results from unnecessary data.
        :param result: dictionary with whois response.
        :return: dict[str, str] dictionary with needed results.
        """
        expiration_date: datetime = self.get_expiration_date(expiration_date=result.expiration_date)
        return {
            'exist': True,
            'target': result.domain,
            'expiration_date': str(result.expiration_date),
            'expired': self.is_expired(expiration_date=expiration_date),
            'expire_soon': self.is_expire_soon(expiration_date=expiration_date),
            'creation_date': str(result.creation_date),
            'updated_dates': self.get_updates_dates(updated_date=result.updated_date),
            'country': result.country,
        }

    @staticmethod
    def is_registered(target: str) -> Union[bool, Any]:
        """
        Check if domain valid and registered
        :return: whois | bool
        """
        try:
            w = whois.whois(target)
        except (PywhoisError, socket.herror):
            return False
        else:
            return w if w.domain_name else False

    @staticmethod
    def _clean_target(target: str) -> str:
        return target.strip()

    @staticmethod
    def get_updates_dates(updated_date: Union[str, list]) -> Union[str, list]:
        """
        Method to gain proper updates date.
        :param updated_date: result from whois request.
        :return: str | list containing datetime.
        """
        return list(map(str, updated_date)) if isinstance(updated_date, list) else str(updated_date)

    @staticmethod
    def is_expired(expiration_date: datetime) -> bool:
        """
        Method to check if domain registration is expired.
        :param expiration_date: result from whois request.
        :return: bool
        """
        return expiration_date < datetime.now()

    @staticmethod
    def get_expiration_date(expiration_date: Union[list, datetime]) -> datetime:
        """
        Method to gain proper expiration date.
        :param expiration_date: result from whois request.
        :return: datetime last expiration date.
        """
        return expiration_date[0] if isinstance(expiration_date, list) else expiration_date

    @staticmethod
    def is_expire_soon(expiration_date: Union[list, datetime]) -> bool:
        """
        Method to check if domain can expire soon.
        :param expiration_date: result from whois request.
        :return: bool if will expire in next few month default days number is 60.
        """
        return (expiration_date - datetime.now()).days <= Config.DEFAULT_DAYS_EXPIRATION
