

from __future__ import annotations
from typing import Any
from numpy.typing import NDArray
from plotly.basedatatypes import BaseTraceHierarchyType as _BaseTraceHierarchyType
import copy as _copy


class Box(_BaseTraceHierarchyType):

    # class properties
    # --------------------
    _parent_path_str = 'violin'
    _path_str = 'violin.box'
    _valid_props = {"fillcolor", "line", "visible", "width"}

    # fillcolor
    # ---------
    @property
    def fillcolor(self):
        """
        Sets the inner box plot fill color.

        The 'fillcolor' property is a color and may be specified as:
          - A hex string (e.g. '#ff0000')
          - An rgb/rgba string (e.g. 'rgb(255,0,0)')
          - An hsl/hsla string (e.g. 'hsl(0,100%,50%)')
          - An hsv/hsva string (e.g. 'hsv(0,100%,100%)')
          - A named CSS color

        Returns
        -------
        str
        """
        return self['fillcolor']

    @fillcolor.setter
    def fillcolor(self, val):
        self['fillcolor'] = val

    # line
    # ----
    @property
    def line(self):
        """
        The 'line' property is an instance of Line
        that may be specified as:
          - An instance of :class:`plotly.graph_objs.violin.box.Line`
          - A dict of string/value properties that will be passed
            to the Line constructor

        Returns
        -------
        plotly.graph_objs.violin.box.Line
        """
        return self['line']

    @line.setter
    def line(self, val):
        self['line'] = val

    # visible
    # -------
    @property
    def visible(self):
        """
        Determines if an miniature box plot is drawn inside the
        violins.

        The 'visible' property must be specified as a bool
        (either True, or False)

        Returns
        -------
        bool
        """
        return self['visible']

    @visible.setter
    def visible(self, val):
        self['visible'] = val

    # width
    # -----
    @property
    def width(self):
        """
        Sets the width of the inner box plots relative to the violins'
        width. For example, with 1, the inner box plots are as wide as
        the violins.

        The 'width' property is a number and may be specified as:
          - An int or float in the interval [0, 1]

        Returns
        -------
        int|float
        """
        return self['width']

    @width.setter
    def width(self, val):
        self['width'] = val

    # Self properties description
    # ---------------------------
    @property
    def _prop_descriptions(self):
        return """\
        fillcolor
            Sets the inner box plot fill color.
        line
            :class:`plotly.graph_objects.violin.box.Line` instance
            or dict with compatible properties
        visible
            Determines if an miniature box plot is drawn inside the
            violins.
        width
            Sets the width of the inner box plots relative to the
            violins' width. For example, with 1, the inner box
            plots are as wide as the violins.
        """
    def __init__(self,
            arg=None,
            fillcolor: str|None = None,
            line: None|None = None,
            visible: bool|None = None,
            width: int|float|None = None,
            **kwargs
        ):
        """
        Construct a new Box object

        Parameters
        ----------
        arg
            dict of properties compatible with this constructor or
            an instance of :class:`plotly.graph_objs.violin.Box`
        fillcolor
            Sets the inner box plot fill color.
        line
            :class:`plotly.graph_objects.violin.box.Line` instance
            or dict with compatible properties
        visible
            Determines if an miniature box plot is drawn inside the
            violins.
        width
            Sets the width of the inner box plots relative to the
            violins' width. For example, with 1, the inner box
            plots are as wide as the violins.

        Returns
        -------
        Box
        """
        super().__init__('box')
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
The first argument to the plotly.graph_objs.violin.Box
constructor must be a dict or
an instance of :class:`plotly.graph_objs.violin.Box`""")

        # Handle skip_invalid
        # -------------------
        self._skip_invalid = kwargs.pop('skip_invalid', False)
        self._validate = kwargs.pop('_validate', True)
        

        # Populate data dict with properties
        # ----------------------------------
        self._init_provided('fillcolor', arg, fillcolor)
        self._init_provided('line', arg, line)
        self._init_provided('visible', arg, visible)
        self._init_provided('width', arg, width)

        # Process unknown kwargs
        # ----------------------
        self._process_kwargs(**dict(arg, **kwargs))

        # Reset skip_invalid
        # ------------------
        self._skip_invalid = False
