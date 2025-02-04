

from plotly.basedatatypes import BaseTraceHierarchyType as _BaseTraceHierarchyType
import copy as _copy


class Marker(_BaseTraceHierarchyType):

    # class properties
    # --------------------
    _parent_path_str = 'choroplethmapbox'
    _path_str = 'choroplethmapbox.marker'
    _valid_props = {"line", "opacity", "opacitysrc"}

    # line
    # ----
    @property
    def line(self):
        """
        The 'line' property is an instance of Line
        that may be specified as:
          - An instance of :class:`plotly.graph_objs.choroplethmapbox.marker.Line`
          - A dict of string/value properties that will be passed
            to the Line constructor

        Returns
        -------
        plotly.graph_objs.choroplethmapbox.marker.Line
        """
        return self['line']

    @line.setter
    def line(self, val):
        self['line'] = val

    # opacity
    # -------
    @property
    def opacity(self):
        """
        Sets the opacity of the locations.

        The 'opacity' property is a number and may be specified as:
          - An int or float in the interval [0, 1]
          - A tuple, list, or one-dimensional numpy array of the above

        Returns
        -------
        int|float|numpy.ndarray
        """
        return self['opacity']

    @opacity.setter
    def opacity(self, val):
        self['opacity'] = val

    # opacitysrc
    # ----------
    @property
    def opacitysrc(self):
        """
        Sets the source reference on Chart Studio Cloud for `opacity`.

        The 'opacitysrc' property must be specified as a string or
        as a plotly.grid_objs.Column object

        Returns
        -------
        str
        """
        return self['opacitysrc']

    @opacitysrc.setter
    def opacitysrc(self, val):
        self['opacitysrc'] = val

    # Self properties description
    # ---------------------------
    @property
    def _prop_descriptions(self):
        return """\
        line
            :class:`plotly.graph_objects.choroplethmapbox.marker.Li
            ne` instance or dict with compatible properties
        opacity
            Sets the opacity of the locations.
        opacitysrc
            Sets the source reference on Chart Studio Cloud for
            `opacity`.
        """
    def __init__(self,
            arg=None,
            line=None,
            opacity=None,
            opacitysrc=None,
            **kwargs
        ):
        """
        Construct a new Marker object

        Parameters
        ----------
        arg
            dict of properties compatible with this constructor or
            an instance of
            :class:`plotly.graph_objs.choroplethmapbox.Marker`
        line
            :class:`plotly.graph_objects.choroplethmapbox.marker.Li
            ne` instance or dict with compatible properties
        opacity
            Sets the opacity of the locations.
        opacitysrc
            Sets the source reference on Chart Studio Cloud for
            `opacity`.

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
The first argument to the plotly.graph_objs.choroplethmapbox.Marker
constructor must be a dict or
an instance of :class:`plotly.graph_objs.choroplethmapbox.Marker`""")

        # Handle skip_invalid
        # -------------------
        self._skip_invalid = kwargs.pop('skip_invalid', False)
        self._validate = kwargs.pop('_validate', True)
        

        # Populate data dict with properties
        # ----------------------------------
        self._init_provided('line', arg, line)
        self._init_provided('opacity', arg, opacity)
        self._init_provided('opacitysrc', arg, opacitysrc)

        # Process unknown kwargs
        # ----------------------
        self._process_kwargs(**dict(arg, **kwargs))

        # Reset skip_invalid
        # ------------------
        self._skip_invalid = False
