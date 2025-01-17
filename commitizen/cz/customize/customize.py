try:
    from jinja2 import Template
except ImportError:
    from string import Template

from commitizen import defaults
from commitizen.cz.base import BaseCommitizen

__all__ = ["CustomizeCommitsCz"]


class CustomizeCommitsCz(BaseCommitizen):
    bump_pattern = defaults.bump_pattern
    bump_map = defaults.bump_map

    def __init__(self, config: dict):
        super(CustomizeCommitsCz, self).__init__(config)
        self.custom_config = self.config.get("customize")

        custom_bump_pattern = self.custom_config.get("bump_pattern")
        if custom_bump_pattern:
            self.bump_pattern = custom_bump_pattern

        custom_bump_map = self.custom_config.get("bump_map")
        if custom_bump_map:
            self.bump_map = custom_bump_map

    def questions(self) -> list:
        return self.custom_config.get("questions")

    def message(self, answers: dict) -> str:
        message_template = Template(self.custom_config.get("message_template"))
        if getattr(Template, "substitute", None):
            return message_template.substitute(**answers)
        else:
            return message_template.render(**answers)

    def example(self) -> str:
        return self.custom_config.get("example")

    def schema(self) -> str:
        return self.custom_config.get("schema")

    def info(self) -> str:
        info_path = self.custom_config.get("info_path")
        info = self.custom_config.get("info")
        if info_path:
            with open(info_path, "r") as f:
                content = f.read()
            return content
        elif info:
            return info
        raise NotImplementedError("Not Implemented yet")
