from __future__ import annotations
from typing import Any
from numpy.typing import NDArray
from plotly.basedatatypes import BaseLayoutHierarchyType as _BaseLayoutHierarchyType
import copy as _copy


class Pad(_BaseLayoutHierarchyType):

    _parent_path_str = "layout.updatemenu"
    _path_str = "layout.updatemenu.pad"
    _valid_props = {"b", "l", "r", "t"}

    @property
    def b(self):
        """
        The amount of padding (in px) along the bottom of the
        component.

        The 'b' property is a number and may be specified as:
          - An int or float

        Returns
        -------
        int|float
        """
        return self["b"]

    @b.setter
    def b(self, val):
        self["b"] = val

    @property
    def l(self):
        """
        The amount of padding (in px) on the left side of the
        component.

        The 'l' property is a number and may be specified as:
          - An int or float

        Returns
        -------
        int|float
        """
        return self["l"]

    @l.setter
    def l(self, val):
        self["l"] = val

    @property
    def r(self):
        """
        The amount of padding (in px) on the right side of the
        component.

        The 'r' property is a number and may be specified as:
          - An int or float

        Returns
        -------
        int|float
        """
        return self["r"]

    @r.setter
    def r(self, val):
        self["r"] = val

    @property
    def t(self):
        """
        The amount of padding (in px) along the top of the component.

        The 't' property is a number and may be specified as:
          - An int or float

        Returns
        -------
        int|float
        """
        return self["t"]

    @t.setter
    def t(self, val):
        self["t"] = val

    @property
    def _prop_descriptions(self):
        return """\
        b
            The amount of padding (in px) along the bottom of the
            component.
        l
            The amount of padding (in px) on the left side of the
            component.
        r
            The amount of padding (in px) on the right side of the
            component.
        t
            The amount of padding (in px) along the top of the
            component.
        """

    def __init__(
        self,
        arg=None,
        b: int | float | None = None,
        l: int | float | None = None,
        r: int | float | None = None,
        t: int | float | None = None,
        **kwargs,
    ):
        """
        Construct a new Pad object

        Sets the padding around the buttons or dropdown menu.

        Parameters
        ----------
        arg
            dict of properties compatible with this constructor or
            an instance of
            :class:`plotly.graph_objs.layout.updatemenu.Pad`
        b
            The amount of padding (in px) along the bottom of the
            component.
        l
            The amount of padding (in px) on the left side of the
            component.
        r
            The amount of padding (in px) on the right side of the
            component.
        t
            The amount of padding (in px) along the top of the
            component.

        Returns
        -------
        Pad
        """
        super().__init__("pad")
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
The first argument to the plotly.graph_objs.layout.updatemenu.Pad
constructor must be a dict or
an instance of :class:`plotly.graph_objs.layout.updatemenu.Pad`"""
            )

        self._skip_invalid = kwargs.pop("skip_invalid", False)
        self._validate = kwargs.pop("_validate", True)

        self._init_provided("b", arg, b)
        self._init_provided("l", arg, l)
        self._init_provided("r", arg, r)
        self._init_provided("t", arg, t)
        self._process_kwargs(**dict(arg, **kwargs))
        self._skip_invalid = False
