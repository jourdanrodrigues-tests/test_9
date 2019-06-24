import os
import re


class DotEnvReader:
    """
    Usage: `DotEnvReader('path').read()`
    """

    def __init__(self, path: str):
        self.path = path

    def read(self) -> None:
        try:
            with open(self.path) as f:
                content = f.read()
        except IOError:
            return

        for line in content.splitlines():
            try:
                os.environ.setdefault(*self._extract_key_value(line))
            except self.InvalidEnvLine:
                pass

    def _extract_key_value(self, line):
        match = re.match(r'\A([A-Za-z_0-9]+)=(.*)\Z', re.sub(r'( +)?#(.+)?', '', line))
        if not match:
            raise self.InvalidEnvLine
        return [os.path.expandvars(value).strip() for value in match.group(1, 2)]

    class InvalidEnvLine(Exception):
        pass
