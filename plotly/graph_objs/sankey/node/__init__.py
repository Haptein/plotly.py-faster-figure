import sys
from _plotly_utils.importers import relative_import

__all__, __getattr__, __dir__ = relative_import(
    __name__, [".hoverlabel"], ["._hoverlabel.Hoverlabel", "._line.Line"]
)
