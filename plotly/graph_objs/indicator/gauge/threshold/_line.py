from __future__ import annotations
from typing import Any
from numpy.typing import NDArray
from plotly.basedatatypes import BaseTraceHierarchyType as _BaseTraceHierarchyType
import copy as _copy


class Line(_BaseTraceHierarchyType):

    _parent_path_str = "indicator.gauge.threshold"
    _path_str = "indicator.gauge.threshold.line"
    _valid_props = {"color", "width"}

    @property
    def color(self):
        """
        Sets the color of the threshold line.

        The 'color' property is a color and may be specified as:
          - A hex string (e.g. '#ff0000')
          - An rgb/rgba string (e.g. 'rgb(255,0,0)')
          - An hsl/hsla string (e.g. 'hsl(0,100%,50%)')
          - An hsv/hsva string (e.g. 'hsv(0,100%,100%)')
          - A named CSS color

        Returns
        -------
        str
        """
        return self["color"]

    @color.setter
    def color(self, val):
        self["color"] = val

    @property
    def width(self):
        """
        Sets the width (in px) of the threshold line.

        The 'width' property is a number and may be specified as:
          - An int or float in the interval [0, inf]

        Returns
        -------
        int|float
        """
        return self["width"]

    @width.setter
    def width(self, val):
        self["width"] = val

    @property
    def _prop_descriptions(self):
        return """\
        color
            Sets the color of the threshold line.
        width
            Sets the width (in px) of the threshold line.
        """

    def __init__(
        self,
        arg=None,
        color: str | None = None,
        width: int | float | None = None,
        **kwargs,
    ):
        """
        Construct a new Line object

        Parameters
        ----------
        arg
            dict of properties compatible with this constructor or
            an instance of :class:`plotly.graph_objs.indicator.gaug
            e.threshold.Line`
        color
            Sets the color of the threshold line.
        width
            Sets the width (in px) of the threshold line.

        Returns
        -------
        Line
        """
        super().__init__("line")
        if "_parent" in kwargs:
            self._parent = kwargs["_parent"]
            return

        if arg is None:
            arg = {}
        elif isinstance(arg, self.__class__):
            arg = arg.to_plotly_json()
        elif isinstance(arg, dict):
            arg = _copy.copy(arg)
        else:
            raise ValueError(
                """\
The first argument to the plotly.graph_objs.indicator.gauge.threshold.Line
constructor must be a dict or
an instance of :class:`plotly.graph_objs.indicator.gauge.threshold.Line`"""
            )

        self._skip_invalid = kwargs.pop("skip_invalid", False)
        self._validate = kwargs.pop("_validate", True)

        self._init_provided("color", arg, color)
        self._init_provided("width", arg, width)
        self._process_kwargs(**dict(arg, **kwargs))
        self._skip_invalid = False
