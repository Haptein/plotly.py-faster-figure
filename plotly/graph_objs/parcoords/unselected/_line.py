

from __future__ import annotations
from typing import Any
from numpy.typing import NDArray
from plotly.basedatatypes import BaseTraceHierarchyType as _BaseTraceHierarchyType
import copy as _copy


class Line(_BaseTraceHierarchyType):

    # class properties
    # --------------------
    _parent_path_str = 'parcoords.unselected'
    _path_str = 'parcoords.unselected.line'
    _valid_props = {"color", "opacity"}

    # color
    # -----
    @property
    def color(self):
        """
        Sets the base color of unselected lines. in connection with
        `unselected.line.opacity`.

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
        return self['color']

    @color.setter
    def color(self, val):
        self['color'] = val

    # opacity
    # -------
    @property
    def opacity(self):
        """
        Sets the opacity of unselected lines. The default "auto"
        decreases the opacity smoothly as the number of lines
        increases. Use 1 to achieve exact `unselected.line.color`.

        The 'opacity' property is a number and may be specified as:
          - An int or float in the interval [0, 1]

        Returns
        -------
        int|float
        """
        return self['opacity']

    @opacity.setter
    def opacity(self, val):
        self['opacity'] = val

    # Self properties description
    # ---------------------------
    @property
    def _prop_descriptions(self):
        return """\
        color
            Sets the base color of unselected lines. in connection
            with `unselected.line.opacity`.
        opacity
            Sets the opacity of unselected lines. The default
            "auto" decreases the opacity smoothly as the number of
            lines increases. Use 1 to achieve exact
            `unselected.line.color`.
        """
    def __init__(self,
            arg=None,
            color: str|None = None,
            opacity: int|float|None = None,
            **kwargs
        ):
        """
        Construct a new Line object

        Parameters
        ----------
        arg
            dict of properties compatible with this constructor or
            an instance of
            :class:`plotly.graph_objs.parcoords.unselected.Line`
        color
            Sets the base color of unselected lines. in connection
            with `unselected.line.opacity`.
        opacity
            Sets the opacity of unselected lines. The default
            "auto" decreases the opacity smoothly as the number of
            lines increases. Use 1 to achieve exact
            `unselected.line.color`.

        Returns
        -------
        Line
        """
        super().__init__('line')
        if '_parent' in kwargs:
            self._parent = kwargs['_parent']
            return

        # Validate arg
        # ------------
        if arg is None:
            arg = {}
        elif isinstance(arg, self.__class__):
            arg = arg.to_plotly_json()
        elif isinstance(arg, dict):
            arg = _copy.copy(arg)
        else:
            raise ValueError("""\
The first argument to the plotly.graph_objs.parcoords.unselected.Line
constructor must be a dict or
an instance of :class:`plotly.graph_objs.parcoords.unselected.Line`""")

        # Handle skip_invalid
        # -------------------
        self._skip_invalid = kwargs.pop('skip_invalid', False)
        self._validate = kwargs.pop('_validate', True)
        

        # Populate data dict with properties
        # ----------------------------------
        self._init_provided('color', arg, color)
        self._init_provided('opacity', arg, opacity)

        # Process unknown kwargs
        # ----------------------
        self._process_kwargs(**dict(arg, **kwargs))

        # Reset skip_invalid
        # ------------------
        self._skip_invalid = False
