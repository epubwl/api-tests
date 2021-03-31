from dataclasses import dataclass

from .json_dataclass import JSONDataclass


@dataclass
class PasswordChange(JSONDataclass):
    currentPassword: str
    newPassword: str
