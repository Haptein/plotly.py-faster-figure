

from plotly.basedatatypes import BaseTraceHierarchyType as _BaseTraceHierarchyType
import copy as _copy


class Fill(_BaseTraceHierarchyType):

    # class properties
    # --------------------
    _parent_path_str = 'table.header'
    _path_str = 'table.header.fill'
    _valid_props = {"color", "colorsrc"}

    # color
    # -----
    @property
    def color(self):
        """
        Sets the cell fill color. It accepts either a specific color or
        an array of colors or a 2D array of colors.

        The 'color' property is a color and may be specified as:
          - A hex string (e.g. '#ff0000')
          - An rgb/rgba string (e.g. 'rgb(255,0,0)')
          - An hsl/hsla string (e.g. 'hsl(0,100%,50%)')
          - An hsv/hsva string (e.g. 'hsv(0,100%,100%)')
          - A named CSS color
          - A list or array of any of the above

        Returns
        -------
        str|numpy.ndarray
        """
        return self['color']

    @color.setter
    def color(self, val):
        self['color'] = val

    # colorsrc
    # --------
    @property
    def colorsrc(self):
        """
        Sets the source reference on Chart Studio Cloud for `color`.

        The 'colorsrc' property must be specified as a string or
        as a plotly.grid_objs.Column object

        Returns
        -------
        str
        """
        return self['colorsrc']

    @colorsrc.setter
    def colorsrc(self, val):
        self['colorsrc'] = val

    # Self properties description
    # ---------------------------
    @property
    def _prop_descriptions(self):
        return """\
        color
            Sets the cell fill color. It accepts either a specific
            color or an array of colors or a 2D array of colors.
        colorsrc
            Sets the source reference on Chart Studio Cloud for
            `color`.
        """
    def __init__(self,
            arg=None,
            color=None,
            colorsrc=None,
            **kwargs
        ):
        """
        Construct a new Fill object

        Parameters
        ----------
        arg
            dict of properties compatible with this constructor or
            an instance of
            :class:`plotly.graph_objs.table.header.Fill`
        color
            Sets the cell fill color. It accepts either a specific
            color or an array of colors or a 2D array of colors.
        colorsrc
            Sets the source reference on Chart Studio Cloud for
            `color`.

        Returns
        -------
        Fill
        """
        super(Fill, self).__init__('fill')

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
The first argument to the plotly.graph_objs.table.header.Fill
constructor must be a dict or
an instance of :class:`plotly.graph_objs.table.header.Fill`""")

        # Handle skip_invalid
        # -------------------
        self._skip_invalid = kwargs.pop('skip_invalid', False)
        self._validate = kwargs.pop('_validate', True)
        

        # Populate data dict with properties
        # ----------------------------------
        self._init_provided('color', arg, color)
        self._init_provided('colorsrc', arg, colorsrc)

        # Process unknown kwargs
        # ----------------------
        self._process_kwargs(**dict(arg, **kwargs))

        # Reset skip_invalid
        # ------------------
        self._skip_invalid = False
