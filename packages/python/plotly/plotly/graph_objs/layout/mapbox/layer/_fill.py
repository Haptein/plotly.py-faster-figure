

from plotly.basedatatypes import BaseLayoutHierarchyType as _BaseLayoutHierarchyType
import copy as _copy


class Fill(_BaseLayoutHierarchyType):

    # class properties
    # --------------------
    _parent_path_str = 'layout.mapbox.layer'
    _path_str = 'layout.mapbox.layer.fill'
    _valid_props = {"outlinecolor"}

    # outlinecolor
    # ------------
    @property
    def outlinecolor(self):
        """
        Sets the fill outline color (mapbox.layer.paint.fill-outline-
        color). Has an effect only when `type` is set to "fill".

        The 'outlinecolor' property is a color and may be specified as:
          - A hex string (e.g. '#ff0000')
          - An rgb/rgba string (e.g. 'rgb(255,0,0)')
          - An hsl/hsla string (e.g. 'hsl(0,100%,50%)')
          - An hsv/hsva string (e.g. 'hsv(0,100%,100%)')
          - A named CSS color

        Returns
        -------
        str
        """
        return self['outlinecolor']

    @outlinecolor.setter
    def outlinecolor(self, val):
        self['outlinecolor'] = val

    # Self properties description
    # ---------------------------
    @property
    def _prop_descriptions(self):
        return """\
        outlinecolor
            Sets the fill outline color (mapbox.layer.paint.fill-
            outline-color). Has an effect only when `type` is set
            to "fill".
        """
    def __init__(self,
            arg=None,
            outlinecolor=None,
            **kwargs
        ):
        """
        Construct a new Fill object

        Parameters
        ----------
        arg
            dict of properties compatible with this constructor or
            an instance of
            :class:`plotly.graph_objs.layout.mapbox.layer.Fill`
        outlinecolor
            Sets the fill outline color (mapbox.layer.paint.fill-
            outline-color). Has an effect only when `type` is set
            to "fill".

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
The first argument to the plotly.graph_objs.layout.mapbox.layer.Fill
constructor must be a dict or
an instance of :class:`plotly.graph_objs.layout.mapbox.layer.Fill`""")

        # Handle skip_invalid
        # -------------------
        self._skip_invalid = kwargs.pop('skip_invalid', False)
        self._validate = kwargs.pop('_validate', True)
        

        # Populate data dict with properties
        # ----------------------------------
        self._init_provided('outlinecolor', arg, outlinecolor)

        # Process unknown kwargs
        # ----------------------
        self._process_kwargs(**dict(arg, **kwargs))

        # Reset skip_invalid
        # ------------------
        self._skip_invalid = False
