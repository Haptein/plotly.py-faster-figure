

from __future__ import annotations
from typing import Any
from numpy.typing import NDArray
from plotly.basedatatypes import BaseTraceHierarchyType as _BaseTraceHierarchyType
import copy as _copy


class ErrorX(_BaseTraceHierarchyType):

    # class properties
    # --------------------
    _parent_path_str = 'scatter3d'
    _path_str = 'scatter3d.error_x'
    _valid_props = {"array", "arrayminus", "arrayminussrc", "arraysrc", "color", "copy_zstyle", "symmetric", "thickness", "traceref", "tracerefminus", "type", "value", "valueminus", "visible", "width"}

    # array
    # -----
    @property
    def array(self):
        """
        Sets the data corresponding the length of each error bar.
        Values are plotted relative to the underlying data.

        The 'array' property is an array that may be specified as a tuple,
        list, numpy array, or pandas Series

        Returns
        -------
        NDArray
        """
        return self['array']

    @array.setter
    def array(self, val):
        self['array'] = val

    # arrayminus
    # ----------
    @property
    def arrayminus(self):
        """
        Sets the data corresponding the length of each error bar in the
        bottom (left) direction for vertical (horizontal) bars Values
        are plotted relative to the underlying data.

        The 'arrayminus' property is an array that may be specified as a tuple,
        list, numpy array, or pandas Series

        Returns
        -------
        NDArray
        """
        return self['arrayminus']

    @arrayminus.setter
    def arrayminus(self, val):
        self['arrayminus'] = val

    # arrayminussrc
    # -------------
    @property
    def arrayminussrc(self):
        """
        Sets the source reference on Chart Studio Cloud for
        `arrayminus`.

        The 'arrayminussrc' property must be specified as a string or
        as a plotly.grid_objs.Column object

        Returns
        -------
        str
        """
        return self['arrayminussrc']

    @arrayminussrc.setter
    def arrayminussrc(self, val):
        self['arrayminussrc'] = val

    # arraysrc
    # --------
    @property
    def arraysrc(self):
        """
        Sets the source reference on Chart Studio Cloud for `array`.

        The 'arraysrc' property must be specified as a string or
        as a plotly.grid_objs.Column object

        Returns
        -------
        str
        """
        return self['arraysrc']

    @arraysrc.setter
    def arraysrc(self, val):
        self['arraysrc'] = val

    # color
    # -----
    @property
    def color(self):
        """
        Sets the stroke color of the error bars.

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

    # copy_zstyle
    # -----------
    @property
    def copy_zstyle(self):
        """
        The 'copy_zstyle' property must be specified as a bool
        (either True, or False)

        Returns
        -------
        bool
        """
        return self['copy_zstyle']

    @copy_zstyle.setter
    def copy_zstyle(self, val):
        self['copy_zstyle'] = val

    # symmetric
    # ---------
    @property
    def symmetric(self):
        """
        Determines whether or not the error bars have the same length
        in both direction (top/bottom for vertical bars, left/right for
        horizontal bars.

        The 'symmetric' property must be specified as a bool
        (either True, or False)

        Returns
        -------
        bool
        """
        return self['symmetric']

    @symmetric.setter
    def symmetric(self, val):
        self['symmetric'] = val

    # thickness
    # ---------
    @property
    def thickness(self):
        """
        Sets the thickness (in px) of the error bars.

        The 'thickness' property is a number and may be specified as:
          - An int or float in the interval [0, inf]

        Returns
        -------
        int|float
        """
        return self['thickness']

    @thickness.setter
    def thickness(self, val):
        self['thickness'] = val

    # traceref
    # --------
    @property
    def traceref(self):
        """
        The 'traceref' property is a integer and may be specified as:
          - An int (or float that will be cast to an int)
            in the interval [0, 9223372036854775807]

        Returns
        -------
        int
        """
        return self['traceref']

    @traceref.setter
    def traceref(self, val):
        self['traceref'] = val

    # tracerefminus
    # -------------
    @property
    def tracerefminus(self):
        """
        The 'tracerefminus' property is a integer and may be specified as:
          - An int (or float that will be cast to an int)
            in the interval [0, 9223372036854775807]

        Returns
        -------
        int
        """
        return self['tracerefminus']

    @tracerefminus.setter
    def tracerefminus(self, val):
        self['tracerefminus'] = val

    # type
    # ----
    @property
    def type(self):
        """
        Determines the rule used to generate the error bars. If
        "constant", the bar lengths are of a constant value. Set this
        constant in `value`. If "percent", the bar lengths correspond
        to a percentage of underlying data. Set this percentage in
        `value`. If "sqrt", the bar lengths correspond to the square of
        the underlying data. If "data", the bar lengths are set with
        data set `array`.

        The 'type' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['percent', 'constant', 'sqrt', 'data']

        Returns
        -------
        Any
        """
        return self['type']

    @type.setter
    def type(self, val):
        self['type'] = val

    # value
    # -----
    @property
    def value(self):
        """
        Sets the value of either the percentage (if `type` is set to
        "percent") or the constant (if `type` is set to "constant")
        corresponding to the lengths of the error bars.

        The 'value' property is a number and may be specified as:
          - An int or float in the interval [0, inf]

        Returns
        -------
        int|float
        """
        return self['value']

    @value.setter
    def value(self, val):
        self['value'] = val

    # valueminus
    # ----------
    @property
    def valueminus(self):
        """
        Sets the value of either the percentage (if `type` is set to
        "percent") or the constant (if `type` is set to "constant")
        corresponding to the lengths of the error bars in the bottom
        (left) direction for vertical (horizontal) bars

        The 'valueminus' property is a number and may be specified as:
          - An int or float in the interval [0, inf]

        Returns
        -------
        int|float
        """
        return self['valueminus']

    @valueminus.setter
    def valueminus(self, val):
        self['valueminus'] = val

    # visible
    # -------
    @property
    def visible(self):
        """
        Determines whether or not this set of error bars is visible.

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
        Sets the width (in px) of the cross-bar at both ends of the
        error bars.

        The 'width' property is a number and may be specified as:
          - An int or float in the interval [0, inf]

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
        array
            Sets the data corresponding the length of each error
            bar. Values are plotted relative to the underlying
            data.
        arrayminus
            Sets the data corresponding the length of each error
            bar in the bottom (left) direction for vertical
            (horizontal) bars Values are plotted relative to the
            underlying data.
        arrayminussrc
            Sets the source reference on Chart Studio Cloud for
            `arrayminus`.
        arraysrc
            Sets the source reference on Chart Studio Cloud for
            `array`.
        color
            Sets the stroke color of the error bars.
        copy_zstyle

        symmetric
            Determines whether or not the error bars have the same
            length in both direction (top/bottom for vertical bars,
            left/right for horizontal bars.
        thickness
            Sets the thickness (in px) of the error bars.
        traceref

        tracerefminus

        type
            Determines the rule used to generate the error bars. If
            "constant", the bar lengths are of a constant value.
            Set this constant in `value`. If "percent", the bar
            lengths correspond to a percentage of underlying data.
            Set this percentage in `value`. If "sqrt", the bar
            lengths correspond to the square of the underlying
            data. If "data", the bar lengths are set with data set
            `array`.
        value
            Sets the value of either the percentage (if `type` is
            set to "percent") or the constant (if `type` is set to
            "constant") corresponding to the lengths of the error
            bars.
        valueminus
            Sets the value of either the percentage (if `type` is
            set to "percent") or the constant (if `type` is set to
            "constant") corresponding to the lengths of the error
            bars in the bottom (left) direction for vertical
            (horizontal) bars
        visible
            Determines whether or not this set of error bars is
            visible.
        width
            Sets the width (in px) of the cross-bar at both ends of
            the error bars.
        """
    def __init__(self,
            arg=None,
            array: NDArray|None = None,
            arrayminus: NDArray|None = None,
            arrayminussrc: str|None = None,
            arraysrc: str|None = None,
            color: str|None = None,
            copy_zstyle: bool|None = None,
            symmetric: bool|None = None,
            thickness: int|float|None = None,
            traceref: int|None = None,
            tracerefminus: int|None = None,
            type: Any|None = None,
            value: int|float|None = None,
            valueminus: int|float|None = None,
            visible: bool|None = None,
            width: int|float|None = None,
            **kwargs
        ):
        """
        Construct a new ErrorX object

        Parameters
        ----------
        arg
            dict of properties compatible with this constructor or
            an instance of
            :class:`plotly.graph_objs.scatter3d.ErrorX`
        array
            Sets the data corresponding the length of each error
            bar. Values are plotted relative to the underlying
            data.
        arrayminus
            Sets the data corresponding the length of each error
            bar in the bottom (left) direction for vertical
            (horizontal) bars Values are plotted relative to the
            underlying data.
        arrayminussrc
            Sets the source reference on Chart Studio Cloud for
            `arrayminus`.
        arraysrc
            Sets the source reference on Chart Studio Cloud for
            `array`.
        color
            Sets the stroke color of the error bars.
        copy_zstyle

        symmetric
            Determines whether or not the error bars have the same
            length in both direction (top/bottom for vertical bars,
            left/right for horizontal bars.
        thickness
            Sets the thickness (in px) of the error bars.
        traceref

        tracerefminus

        type
            Determines the rule used to generate the error bars. If
            "constant", the bar lengths are of a constant value.
            Set this constant in `value`. If "percent", the bar
            lengths correspond to a percentage of underlying data.
            Set this percentage in `value`. If "sqrt", the bar
            lengths correspond to the square of the underlying
            data. If "data", the bar lengths are set with data set
            `array`.
        value
            Sets the value of either the percentage (if `type` is
            set to "percent") or the constant (if `type` is set to
            "constant") corresponding to the lengths of the error
            bars.
        valueminus
            Sets the value of either the percentage (if `type` is
            set to "percent") or the constant (if `type` is set to
            "constant") corresponding to the lengths of the error
            bars in the bottom (left) direction for vertical
            (horizontal) bars
        visible
            Determines whether or not this set of error bars is
            visible.
        width
            Sets the width (in px) of the cross-bar at both ends of
            the error bars.

        Returns
        -------
        ErrorX
        """
        super().__init__('error_x')
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
The first argument to the plotly.graph_objs.scatter3d.ErrorX
constructor must be a dict or
an instance of :class:`plotly.graph_objs.scatter3d.ErrorX`""")

        # Handle skip_invalid
        # -------------------
        self._skip_invalid = kwargs.pop('skip_invalid', False)
        self._validate = kwargs.pop('_validate', True)
        

        # Populate data dict with properties
        # ----------------------------------
        self._init_provided('array', arg, array)
        self._init_provided('arrayminus', arg, arrayminus)
        self._init_provided('arrayminussrc', arg, arrayminussrc)
        self._init_provided('arraysrc', arg, arraysrc)
        self._init_provided('color', arg, color)
        self._init_provided('copy_zstyle', arg, copy_zstyle)
        self._init_provided('symmetric', arg, symmetric)
        self._init_provided('thickness', arg, thickness)
        self._init_provided('traceref', arg, traceref)
        self._init_provided('tracerefminus', arg, tracerefminus)
        self._init_provided('type', arg, type)
        self._init_provided('value', arg, value)
        self._init_provided('valueminus', arg, valueminus)
        self._init_provided('visible', arg, visible)
        self._init_provided('width', arg, width)

        # Process unknown kwargs
        # ----------------------
        self._process_kwargs(**dict(arg, **kwargs))

        # Reset skip_invalid
        # ------------------
        self._skip_invalid = False
