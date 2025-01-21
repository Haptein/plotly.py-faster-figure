

from plotly.basedatatypes import BaseTraceHierarchyType as _BaseTraceHierarchyType
import copy as _copy


class Marker(_BaseTraceHierarchyType):

    # class properties
    # --------------------
    _parent_path_str = 'waterfall.decreasing'
    _path_str = 'waterfall.decreasing.marker'
    _valid_props = {"color", "line"}

    # color
    # -----
    @property
    def color(self):
        """
        Sets the marker color of all decreasing values.

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

    # line
    # ----
    @property
    def line(self):
        """
        The 'line' property is an instance of Line
        that may be specified as:
          - An instance of :class:`plotly.graph_objs.waterfall.decreasing.marker.Line`
          - A dict of string/value properties that will be passed
            to the Line constructor

        Returns
        -------
        plotly.graph_objs.waterfall.decreasing.marker.Line
        """
        return self['line']

    @line.setter
    def line(self, val):
        self['line'] = val

    # Self properties description
    # ---------------------------
    @property
    def _prop_descriptions(self):
        return """\
        color
            Sets the marker color of all decreasing values.
        line
            :class:`plotly.graph_objects.waterfall.decreasing.marke
            r.Line` instance or dict with compatible properties
        """
    def __init__(self,
            arg=None,
            color=None,
            line=None,
            **kwargs
        ):
        """
        Construct a new Marker object

        Parameters
        ----------
        arg
            dict of properties compatible with this constructor or
            an instance of
            :class:`plotly.graph_objs.waterfall.decreasing.Marker`
        color
            Sets the marker color of all decreasing values.
        line
            :class:`plotly.graph_objects.waterfall.decreasing.marke
            r.Line` instance or dict with compatible properties

        Returns
        -------
        Marker
        """
        super(Marker, self).__init__('marker')

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
The first argument to the plotly.graph_objs.waterfall.decreasing.Marker
constructor must be a dict or
an instance of :class:`plotly.graph_objs.waterfall.decreasing.Marker`""")

        # Handle skip_invalid
        # -------------------
        self._skip_invalid = kwargs.pop('skip_invalid', False)
        self._validate = kwargs.pop('_validate', True)
        

        # Populate data dict with properties
        # ----------------------------------
        self._init_provided('color', arg, color)
        self._init_provided('line', arg, line)

        # Process unknown kwargs
        # ----------------------
        self._process_kwargs(**dict(arg, **kwargs))

        # Reset skip_invalid
        # ------------------
        self._skip_invalid = False
