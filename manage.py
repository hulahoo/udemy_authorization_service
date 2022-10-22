#!/usr/bin/env python
import os
import sys

if __name__ == '__main__':
    from configurations.management import execute_from_command_line

    os.environ.setdefault("DJANGO_CONFIGURAION", "BaseConfig")
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings.settings')

    execute_from_command_line(sys.argv)
