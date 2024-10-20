from enum import Enum


class UserRegex(Enum):
    NAME = (r'^[A-Za-zА-Яа-яЇїІіЄєҐґ\'\-]+$', "The name can consist of letters, apostrophes, and hyphens")
    SURNAME = (r'^[A-Za-zА-Яа-яЇїІіЄєҐґ\'\-]+$', 'The surname can consist of letters, apostrophes, and hyphens')
    PHONE = (r'^\+?[\d\s\-\(\)]+$',
             'The phone number can contain numbers, spaces, hyphens, parentheses, and “+” at the beginning')

    def __init__(self, pattern: str, msg: str):
        self.pattern = pattern
        self.msg = msg
