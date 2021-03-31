from dataclasses import dataclass

from .json_dataclass import JSONDataclass


@dataclass
class UserCredentials(JSONDataclass):
    username: str
    password: str
