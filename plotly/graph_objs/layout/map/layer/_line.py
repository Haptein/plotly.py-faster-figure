from __future__ import annotations
from typing import Any
from numpy.typing import NDArray
from plotly.basedatatypes import BaseLayoutHierarchyType as _BaseLayoutHierarchyType
import copy as _copy


class Line(_BaseLayoutHierarchyType):

    _parent_path_str = "layout.map.layer"
    _path_str = "layout.map.layer.line"
    _valid_props = {"dash", "dashsrc", "width"}

    @property
    def dash(self):
        """
        Sets the length of dashes and gaps (map.layer.paint.line-
        dasharray). Has an effect only when `type` is set to "line".

        The 'dash' property is an array that may be specified as a tuple,
        list, numpy array, or pandas Series

        Returns
        -------
        NDArray
        """
        return self["dash"]

    @dash.setter
    def dash(self, val):
        self["dash"] = val

    @property
    def dashsrc(self):
        """
        Sets the source reference on Chart Studio Cloud for `dash`.

        The 'dashsrc' property must be specified as a string or
        as a plotly.grid_objs.Column object

        Returns
        -------
        str
        """
        return self["dashsrc"]

    @dashsrc.setter
    def dashsrc(self, val):
        self["dashsrc"] = val

    @property
    def width(self):
        """
        Sets the line width (map.layer.paint.line-width). Has an effect
        only when `type` is set to "line".

        The 'width' property is a number and may be specified as:
          - An int or float

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
        dash
            Sets the length of dashes and gaps
            (map.layer.paint.line-dasharray). Has an effect only
            when `type` is set to "line".
        dashsrc
            Sets the source reference on Chart Studio Cloud for
            `dash`.
        width
            Sets the line width (map.layer.paint.line-width). Has
            an effect only when `type` is set to "line".
        """

    def __init__(
        self,
        arg=None,
        dash: NDArray | None = None,
        dashsrc: str | None = None,
        width: int | float | None = None,
        **kwargs,
    ):
        """
        Construct a new Line object

        Parameters
        ----------
        arg
            dict of properties compatible with this constructor or
            an instance of
            :class:`plotly.graph_objs.layout.map.layer.Line`
        dash
            Sets the length of dashes and gaps
            (map.layer.paint.line-dasharray). Has an effect only
            when `type` is set to "line".
        dashsrc
            Sets the source reference on Chart Studio Cloud for
            `dash`.
        width
            Sets the line width (map.layer.paint.line-width). Has
            an effect only when `type` is set to "line".

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
The first argument to the plotly.graph_objs.layout.map.layer.Line
constructor must be a dict or
an instance of :class:`plotly.graph_objs.layout.map.layer.Line`"""
            )

        self._skip_invalid = kwargs.pop("skip_invalid", False)
        self._validate = kwargs.pop("_validate", True)

        self._init_provided("dash", arg, dash)
        self._init_provided("dashsrc", arg, dashsrc)
        self._init_provided("width", arg, width)
        self._process_kwargs(**dict(arg, **kwargs))
        self._skip_invalid = False
