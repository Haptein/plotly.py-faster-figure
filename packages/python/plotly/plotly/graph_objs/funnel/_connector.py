

from plotly.basedatatypes import BaseTraceHierarchyType as _BaseTraceHierarchyType
import copy as _copy


class Connector(_BaseTraceHierarchyType):

    # class properties
    # --------------------
    _parent_path_str = 'funnel'
    _path_str = 'funnel.connector'
    _valid_props = {"fillcolor", "line", "visible"}

    # fillcolor
    # ---------
    @property
    def fillcolor(self):
        """
        Sets the fill color.

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
          - An instance of :class:`plotly.graph_objs.funnel.connector.Line`
          - A dict of string/value properties that will be passed
            to the Line constructor

        Returns
        -------
        plotly.graph_objs.funnel.connector.Line
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
        Determines if connector regions and lines are drawn.

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

    # Self properties description
    # ---------------------------
    @property
    def _prop_descriptions(self):
        return """\
        fillcolor
            Sets the fill color.
        line
            :class:`plotly.graph_objects.funnel.connector.Line`
            instance or dict with compatible properties
        visible
            Determines if connector regions and lines are drawn.
        """
    def __init__(self,
            arg=None,
            fillcolor=None,
            line=None,
            visible=None,
            **kwargs
        ):
        """
        Construct a new Connector object

        Parameters
        ----------
        arg
            dict of properties compatible with this constructor or
            an instance of
            :class:`plotly.graph_objs.funnel.Connector`
        fillcolor
            Sets the fill color.
        line
            :class:`plotly.graph_objects.funnel.connector.Line`
            instance or dict with compatible properties
        visible
            Determines if connector regions and lines are drawn.

        Returns
        -------
        Connector
        """
        super(Connector, self).__init__('connector')

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
The first argument to the plotly.graph_objs.funnel.Connector
constructor must be a dict or
an instance of :class:`plotly.graph_objs.funnel.Connector`""")

        # Handle skip_invalid
        # -------------------
        self._skip_invalid = kwargs.pop('skip_invalid', False)
        self._validate = kwargs.pop('_validate', True)
        

        # Populate data dict with properties
        # ----------------------------------
        self._init_provided('fillcolor', arg, fillcolor)
        self._init_provided('line', arg, line)
        self._init_provided('visible', arg, visible)

        # Process unknown kwargs
        # ----------------------
        self._process_kwargs(**dict(arg, **kwargs))

        # Reset skip_invalid
        # ------------------
        self._skip_invalid = False
