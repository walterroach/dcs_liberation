from __future__ import annotations

import logging
from pathlib import Path
from typing import Iterable

from babel import Locale
from jinja2 import Environment
from jinja2.environment import Template

class Translation:
    __translations = {
        'en_US',
        'zh'
    }
    current: Locale = Locale('zh')
    default: Locale = Locale('en', 'US')

    @staticmethod
    def load_template(env: Environment, name: str, sep: str="_", suff:str=".j2") -> Template:
        for i in env.loader.list_templates():
            print(i)
            if i.startswith(name):
                if i.endswith(sep + str(Translation.current) + suff):
                    return env.get_template(i)
                elif i.endswith(sep + str(Translation.current.language) + suff):
                    return env.get_template(i)
        logging.error(f"Failed to find {Translation.current} template for {name} in {env.loader.searchpath}")        

    @classmethod
    def translations(cls) -> Iterable:
        for locale in cls.__translations:
            yield Locale.parse(locale)


# TRANSLATIONS = [
#     'en_US',
#     'zh'
# ]
# env = Environment(
#     loader=FileSystemLoader("resources/briefing/templates"),
#     autoescape=select_autoescape(
#         disabled_extensions=("",),
#         default_for_string=True,
#         default=True,
#         ),
#     trim_blocks=True,
#     lstrip_blocks=True,
#     )

# template = Translation.load_template(env, "briefingtemplate")
# print("done")
