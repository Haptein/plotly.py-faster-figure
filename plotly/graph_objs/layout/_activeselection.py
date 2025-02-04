

from plotly.basedatatypes import BaseLayoutHierarchyType as _BaseLayoutHierarchyType
import copy as _copy


class Activeselection(_BaseLayoutHierarchyType):

    # class properties
    # --------------------
    _parent_path_str = 'layout'
    _path_str = 'layout.activeselection'
    _valid_props = {"fillcolor", "opacity"}

    # fillcolor
    # ---------
    @property
    def fillcolor(self):
        """
        Sets the color filling the active selection' interior.

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

    # opacity
    # -------
    @property
    def opacity(self):
        """
        Sets the opacity of the active selection.

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
        fillcolor
            Sets the color filling the active selection' interior.
        opacity
            Sets the opacity of the active selection.
        """
    def __init__(self,
            arg=None,
            fillcolor=None,
            opacity=None,
            **kwargs
        ):
        """
        Construct a new Activeselection object

        Parameters
        ----------
        arg
            dict of properties compatible with this constructor or
            an instance of
            :class:`plotly.graph_objs.layout.Activeselection`
        fillcolor
            Sets the color filling the active selection' interior.
        opacity
            Sets the opacity of the active selection.

        Returns
        -------
        Activeselection
        """
        super().__init__('activeselection')
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
The first argument to the plotly.graph_objs.layout.Activeselection
constructor must be a dict or
an instance of :class:`plotly.graph_objs.layout.Activeselection`""")

        # Handle skip_invalid
        # -------------------
        self._skip_invalid = kwargs.pop('skip_invalid', False)
        self._validate = kwargs.pop('_validate', True)
        

        # Populate data dict with properties
        # ----------------------------------
        self._init_provided('fillcolor', arg, fillcolor)
        self._init_provided('opacity', arg, opacity)

        # Process unknown kwargs
        # ----------------------
        self._process_kwargs(**dict(arg, **kwargs))

        # Reset skip_invalid
        # ------------------
        self._skip_invalid = False
