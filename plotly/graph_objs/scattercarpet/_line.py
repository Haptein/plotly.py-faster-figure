

from plotly.basedatatypes import BaseTraceHierarchyType as _BaseTraceHierarchyType
import copy as _copy


class Line(_BaseTraceHierarchyType):

    # class properties
    # --------------------
    _parent_path_str = 'scattercarpet'
    _path_str = 'scattercarpet.line'
    _valid_props = {"backoff", "backoffsrc", "color", "dash", "shape", "smoothing", "width"}

    # backoff
    # -------
    @property
    def backoff(self):
        """
        Sets the line back off from the end point of the nth line
        segment (in px). This option is useful e.g. to avoid overlap
        with arrowhead markers. With "auto" the lines would trim before
        markers if `marker.angleref` is set to "previous".

        The 'backoff' property is a number and may be specified as:
          - An int or float in the interval [0, inf]
          - A tuple, list, or one-dimensional numpy array of the above

        Returns
        -------
        int|float|numpy.ndarray
        """
        return self['backoff']

    @backoff.setter
    def backoff(self, val):
        self['backoff'] = val

    # backoffsrc
    # ----------
    @property
    def backoffsrc(self):
        """
        Sets the source reference on Chart Studio Cloud for `backoff`.

        The 'backoffsrc' property must be specified as a string or
        as a plotly.grid_objs.Column object

        Returns
        -------
        str
        """
        return self['backoffsrc']

    @backoffsrc.setter
    def backoffsrc(self, val):
        self['backoffsrc'] = val

    # color
    # -----
    @property
    def color(self):
        """
        Sets the line color.

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

    # dash
    # ----
    @property
    def dash(self):
        """
        Sets the dash style of lines. Set to a dash type string
        ("solid", "dot", "dash", "longdash", "dashdot", or
        "longdashdot") or a dash length list in px (eg
        "5px,10px,2px,2px").

        The 'dash' property is an enumeration that may be specified as:
          - One of the following dash styles:
                ['solid', 'dot', 'dash', 'longdash', 'dashdot', 'longdashdot']
          - A string containing a dash length list in pixels or percentages
                (e.g. '5px 10px 2px 2px', '5, 10, 2, 2', '10% 20% 40%', etc.)

        Returns
        -------
        str
        """
        return self['dash']

    @dash.setter
    def dash(self, val):
        self['dash'] = val

    # shape
    # -----
    @property
    def shape(self):
        """
        Determines the line shape. With "spline" the lines are drawn
        using spline interpolation. The other available values
        correspond to step-wise line shapes.

        The 'shape' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['linear', 'spline']

        Returns
        -------
        Any
        """
        return self['shape']

    @shape.setter
    def shape(self, val):
        self['shape'] = val

    # smoothing
    # ---------
    @property
    def smoothing(self):
        """
        Has an effect only if `shape` is set to "spline" Sets the
        amount of smoothing. 0 corresponds to no smoothing (equivalent
        to a "linear" shape).

        The 'smoothing' property is a number and may be specified as:
          - An int or float in the interval [0, 1.3]

        Returns
        -------
        int|float
        """
        return self['smoothing']

    @smoothing.setter
    def smoothing(self, val):
        self['smoothing'] = val

    # width
    # -----
    @property
    def width(self):
        """
        Sets the line width (in px).

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
        backoff
            Sets the line back off from the end point of the nth
            line segment (in px). This option is useful e.g. to
            avoid overlap with arrowhead markers. With "auto" the
            lines would trim before markers if `marker.angleref` is
            set to "previous".
        backoffsrc
            Sets the source reference on Chart Studio Cloud for
            `backoff`.
        color
            Sets the line color.
        dash
            Sets the dash style of lines. Set to a dash type string
            ("solid", "dot", "dash", "longdash", "dashdot", or
            "longdashdot") or a dash length list in px (eg
            "5px,10px,2px,2px").
        shape
            Determines the line shape. With "spline" the lines are
            drawn using spline interpolation. The other available
            values correspond to step-wise line shapes.
        smoothing
            Has an effect only if `shape` is set to "spline" Sets
            the amount of smoothing. 0 corresponds to no smoothing
            (equivalent to a "linear" shape).
        width
            Sets the line width (in px).
        """
    def __init__(self,
            arg=None,
            backoff=None,
            backoffsrc=None,
            color=None,
            dash=None,
            shape=None,
            smoothing=None,
            width=None,
            **kwargs
        ):
        """
        Construct a new Line object

        Parameters
        ----------
        arg
            dict of properties compatible with this constructor or
            an instance of
            :class:`plotly.graph_objs.scattercarpet.Line`
        backoff
            Sets the line back off from the end point of the nth
            line segment (in px). This option is useful e.g. to
            avoid overlap with arrowhead markers. With "auto" the
            lines would trim before markers if `marker.angleref` is
            set to "previous".
        backoffsrc
            Sets the source reference on Chart Studio Cloud for
            `backoff`.
        color
            Sets the line color.
        dash
            Sets the dash style of lines. Set to a dash type string
            ("solid", "dot", "dash", "longdash", "dashdot", or
            "longdashdot") or a dash length list in px (eg
            "5px,10px,2px,2px").
        shape
            Determines the line shape. With "spline" the lines are
            drawn using spline interpolation. The other available
            values correspond to step-wise line shapes.
        smoothing
            Has an effect only if `shape` is set to "spline" Sets
            the amount of smoothing. 0 corresponds to no smoothing
            (equivalent to a "linear" shape).
        width
            Sets the line width (in px).

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
The first argument to the plotly.graph_objs.scattercarpet.Line
constructor must be a dict or
an instance of :class:`plotly.graph_objs.scattercarpet.Line`""")

        # Handle skip_invalid
        # -------------------
        self._skip_invalid = kwargs.pop('skip_invalid', False)
        self._validate = kwargs.pop('_validate', True)
        

        # Populate data dict with properties
        # ----------------------------------
        self._init_provided('backoff', arg, backoff)
        self._init_provided('backoffsrc', arg, backoffsrc)
        self._init_provided('color', arg, color)
        self._init_provided('dash', arg, dash)
        self._init_provided('shape', arg, shape)
        self._init_provided('smoothing', arg, smoothing)
        self._init_provided('width', arg, width)

        # Process unknown kwargs
        # ----------------------
        self._process_kwargs(**dict(arg, **kwargs))

        # Reset skip_invalid
        # ------------------
        self._skip_invalid = False
