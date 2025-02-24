from __future__ import annotations
from typing import Any
from numpy.typing import NDArray
from plotly.basedatatypes import BaseTraceHierarchyType as _BaseTraceHierarchyType
import copy as _copy


class Unselected(_BaseTraceHierarchyType):

    _parent_path_str = "scattergeo"
    _path_str = "scattergeo.unselected"
    _valid_props = {"marker", "textfont"}

    @property
    def marker(self):
        """
        The 'marker' property is an instance of Marker
        that may be specified as:
          - An instance of :class:`plotly.graph_objs.scattergeo.unselected.Marker`
          - A dict of string/value properties that will be passed
            to the Marker constructor

        Returns
        -------
        plotly.graph_objs.scattergeo.unselected.Marker
        """
        return self["marker"]

    @marker.setter
    def marker(self, val):
        self["marker"] = val

    @property
    def textfont(self):
        """
        The 'textfont' property is an instance of Textfont
        that may be specified as:
          - An instance of :class:`plotly.graph_objs.scattergeo.unselected.Textfont`
          - A dict of string/value properties that will be passed
            to the Textfont constructor

        Returns
        -------
        plotly.graph_objs.scattergeo.unselected.Textfont
        """
        return self["textfont"]

    @textfont.setter
    def textfont(self, val):
        self["textfont"] = val

    @property
    def _prop_descriptions(self):
        return """\
        marker
            :class:`plotly.graph_objects.scattergeo.unselected.Mark
            er` instance or dict with compatible properties
        textfont
            :class:`plotly.graph_objects.scattergeo.unselected.Text
            font` instance or dict with compatible properties
        """

    def __init__(
        self,
        arg=None,
        marker: None | None = None,
        textfont: None | None = None,
        **kwargs,
    ):
        """
        Construct a new Unselected object

        Parameters
        ----------
        arg
            dict of properties compatible with this constructor or
            an instance of
            :class:`plotly.graph_objs.scattergeo.Unselected`
        marker
            :class:`plotly.graph_objects.scattergeo.unselected.Mark
            er` instance or dict with compatible properties
        textfont
            :class:`plotly.graph_objects.scattergeo.unselected.Text
            font` instance or dict with compatible properties

        Returns
        -------
        Unselected
        """
        super().__init__("unselected")
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
The first argument to the plotly.graph_objs.scattergeo.Unselected
constructor must be a dict or
an instance of :class:`plotly.graph_objs.scattergeo.Unselected`"""
            )

        self._skip_invalid = kwargs.pop("skip_invalid", False)
        self._validate = kwargs.pop("_validate", True)

        self._init_provided("marker", arg, marker)
        self._init_provided("textfont", arg, textfont)
        self._process_kwargs(**dict(arg, **kwargs))
        self._skip_invalid = False
