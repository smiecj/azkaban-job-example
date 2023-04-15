# -*- coding: UTF-8 -*-

from backports import configparser

DEFAULT_SECTION = 'default'

class ConfigParser:
    def __init__(self, config_file):
        self.config = configparser.RawConfigParser()

        with open(config_file, 'r') as f:
            config_string = f'[{DEFAULT_SECTION}]\n' + f.read()

        self.config.read_string(config_string)

    def get(self, key: str):
        return self.config.get(DEFAULT_SECTION, key)