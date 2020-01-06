from jirafs.exceptions import MacroContentError
from jirafs.plugin import (
    BlockElementMacroPlugin,
)


class Plugin(BlockElementMacroPlugin):
    MIN_VERSION = '2.0.0'
    MAX_VERSION = '3.0.0'
    COMPONENT_NAME = 'csv-include'

    def execute_macro(self, data, **kwargs):
        return ''
