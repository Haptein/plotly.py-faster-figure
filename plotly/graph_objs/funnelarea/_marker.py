

from plotly.basedatatypes import BaseTraceHierarchyType as _BaseTraceHierarchyType
import copy as _copy


class Marker(_BaseTraceHierarchyType):

    # class properties
    # --------------------
    _parent_path_str = 'funnelarea'
    _path_str = 'funnelarea.marker'
    _valid_props = {"colors", "colorssrc", "line", "pattern"}

    # colors
    # ------
    @property
    def colors(self):
        """
        Sets the color of each sector. If not specified, the default
        trace color set is used to pick the sector colors.

        The 'colors' property is an array that may be specified as a tuple,
        list, numpy array, or pandas Series

        Returns
        -------
        numpy.ndarray
        """
        return self['colors']

    @colors.setter
    def colors(self, val):
        self['colors'] = val

    # colorssrc
    # ---------
    @property
    def colorssrc(self):
        """
        Sets the source reference on Chart Studio Cloud for `colors`.

        The 'colorssrc' property must be specified as a string or
        as a plotly.grid_objs.Column object

        Returns
        -------
        str
        """
        return self['colorssrc']

    @colorssrc.setter
    def colorssrc(self, val):
        self['colorssrc'] = val

    # line
    # ----
    @property
    def line(self):
        """
        The 'line' property is an instance of Line
        that may be specified as:
          - An instance of :class:`plotly.graph_objs.funnelarea.marker.Line`
          - A dict of string/value properties that will be passed
            to the Line constructor

        Returns
        -------
        plotly.graph_objs.funnelarea.marker.Line
        """
        return self['line']

    @line.setter
    def line(self, val):
        self['line'] = val

    # pattern
    # -------
    @property
    def pattern(self):
        """
        Sets the pattern within the marker.

        The 'pattern' property is an instance of Pattern
        that may be specified as:
          - An instance of :class:`plotly.graph_objs.funnelarea.marker.Pattern`
          - A dict of string/value properties that will be passed
            to the Pattern constructor

        Returns
        -------
        plotly.graph_objs.funnelarea.marker.Pattern
        """
        return self['pattern']

    @pattern.setter
    def pattern(self, val):
        self['pattern'] = val

    # Self properties description
    # ---------------------------
    @property
    def _prop_descriptions(self):
        return """\
        colors
            Sets the color of each sector. If not specified, the
            default trace color set is used to pick the sector
            colors.
        colorssrc
            Sets the source reference on Chart Studio Cloud for
            `colors`.
        line
            :class:`plotly.graph_objects.funnelarea.marker.Line`
            instance or dict with compatible properties
        pattern
            Sets the pattern within the marker.
        """
    def __init__(self,
            arg=None,
            colors=None,
            colorssrc=None,
            line=None,
            pattern=None,
            **kwargs
        ):
        """
        Construct a new Marker object

        Parameters
        ----------
        arg
            dict of properties compatible with this constructor or
            an instance of
            :class:`plotly.graph_objs.funnelarea.Marker`
        colors
            Sets the color of each sector. If not specified, the
            default trace color set is used to pick the sector
            colors.
        colorssrc
            Sets the source reference on Chart Studio Cloud for
            `colors`.
        line
            :class:`plotly.graph_objects.funnelarea.marker.Line`
            instance or dict with compatible properties
        pattern
            Sets the pattern within the marker.

        Returns
        -------
        Marker
        """
        super().__init__('marker')
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
The first argument to the plotly.graph_objs.funnelarea.Marker
constructor must be a dict or
an instance of :class:`plotly.graph_objs.funnelarea.Marker`""")

        # Handle skip_invalid
        # -------------------
        self._skip_invalid = kwargs.pop('skip_invalid', False)
        self._validate = kwargs.pop('_validate', True)
        

        # Populate data dict with properties
        # ----------------------------------
        self._init_provided('colors', arg, colors)
        self._init_provided('colorssrc', arg, colorssrc)
        self._init_provided('line', arg, line)
        self._init_provided('pattern', arg, pattern)

        # Process unknown kwargs
        # ----------------------
        self._process_kwargs(**dict(arg, **kwargs))

        # Reset skip_invalid
        # ------------------
        self._skip_invalid = False
