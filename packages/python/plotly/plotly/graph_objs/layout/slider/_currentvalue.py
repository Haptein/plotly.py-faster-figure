

from plotly.basedatatypes import BaseLayoutHierarchyType as _BaseLayoutHierarchyType
import copy as _copy


class Currentvalue(_BaseLayoutHierarchyType):

    # class properties
    # --------------------
    _parent_path_str = 'layout.slider'
    _path_str = 'layout.slider.currentvalue'
    _valid_props = {"font", "offset", "prefix", "suffix", "visible", "xanchor"}

    # font
    # ----
    @property
    def font(self):
        """
        Sets the font of the current value label text.

        The 'font' property is an instance of Font
        that may be specified as:
          - An instance of :class:`plotly.graph_objs.layout.slider.currentvalue.Font`
          - A dict of string/value properties that will be passed
            to the Font constructor

        Returns
        -------
        plotly.graph_objs.layout.slider.currentvalue.Font
        """
        return self['font']

    @font.setter
    def font(self, val):
        self['font'] = val

    # offset
    # ------
    @property
    def offset(self):
        """
        The amount of space, in pixels, between the current value label
        and the slider.

        The 'offset' property is a number and may be specified as:
          - An int or float

        Returns
        -------
        int|float
        """
        return self['offset']

    @offset.setter
    def offset(self, val):
        self['offset'] = val

    # prefix
    # ------
    @property
    def prefix(self):
        """
        When currentvalue.visible is true, this sets the prefix of the
        label.

        The 'prefix' property is a string and must be specified as:
          - A string
          - A number that will be converted to a string

        Returns
        -------
        str
        """
        return self['prefix']

    @prefix.setter
    def prefix(self, val):
        self['prefix'] = val

    # suffix
    # ------
    @property
    def suffix(self):
        """
        When currentvalue.visible is true, this sets the suffix of the
        label.

        The 'suffix' property is a string and must be specified as:
          - A string
          - A number that will be converted to a string

        Returns
        -------
        str
        """
        return self['suffix']

    @suffix.setter
    def suffix(self, val):
        self['suffix'] = val

    # visible
    # -------
    @property
    def visible(self):
        """
        Shows the currently-selected value above the slider.

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

    # xanchor
    # -------
    @property
    def xanchor(self):
        """
        The alignment of the value readout relative to the length of
        the slider.

        The 'xanchor' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['left', 'center', 'right']

        Returns
        -------
        Any
        """
        return self['xanchor']

    @xanchor.setter
    def xanchor(self, val):
        self['xanchor'] = val

    # Self properties description
    # ---------------------------
    @property
    def _prop_descriptions(self):
        return """\
        font
            Sets the font of the current value label text.
        offset
            The amount of space, in pixels, between the current
            value label and the slider.
        prefix
            When currentvalue.visible is true, this sets the prefix
            of the label.
        suffix
            When currentvalue.visible is true, this sets the suffix
            of the label.
        visible
            Shows the currently-selected value above the slider.
        xanchor
            The alignment of the value readout relative to the
            length of the slider.
        """
    def __init__(self,
            arg=None,
            font=None,
            offset=None,
            prefix=None,
            suffix=None,
            visible=None,
            xanchor=None,
            **kwargs
        ):
        """
        Construct a new Currentvalue object

        Parameters
        ----------
        arg
            dict of properties compatible with this constructor or
            an instance of
            :class:`plotly.graph_objs.layout.slider.Currentvalue`
        font
            Sets the font of the current value label text.
        offset
            The amount of space, in pixels, between the current
            value label and the slider.
        prefix
            When currentvalue.visible is true, this sets the prefix
            of the label.
        suffix
            When currentvalue.visible is true, this sets the suffix
            of the label.
        visible
            Shows the currently-selected value above the slider.
        xanchor
            The alignment of the value readout relative to the
            length of the slider.

        Returns
        -------
        Currentvalue
        """
        super(Currentvalue, self).__init__('currentvalue')

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
The first argument to the plotly.graph_objs.layout.slider.Currentvalue
constructor must be a dict or
an instance of :class:`plotly.graph_objs.layout.slider.Currentvalue`""")

        # Handle skip_invalid
        # -------------------
        self._skip_invalid = kwargs.pop('skip_invalid', False)
        self._validate = kwargs.pop('_validate', True)
        

        # Populate data dict with properties
        # ----------------------------------
        self._init_provided('font', arg, font)
        self._init_provided('offset', arg, offset)
        self._init_provided('prefix', arg, prefix)
        self._init_provided('suffix', arg, suffix)
        self._init_provided('visible', arg, visible)
        self._init_provided('xanchor', arg, xanchor)

        # Process unknown kwargs
        # ----------------------
        self._process_kwargs(**dict(arg, **kwargs))

        # Reset skip_invalid
        # ------------------
        self._skip_invalid = False
