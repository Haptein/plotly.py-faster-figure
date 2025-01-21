

from plotly.basedatatypes import BaseTraceHierarchyType as _BaseTraceHierarchyType
import copy as _copy


class Textfont(_BaseTraceHierarchyType):

    # class properties
    # --------------------
    _parent_path_str = 'scattermap'
    _path_str = 'scattermap.textfont'
    _valid_props = {"color", "family", "size", "style", "weight"}

    # color
    # -----
    @property
    def color(self):
        """
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

    # family
    # ------
    @property
    def family(self):
        """
        HTML font family - the typeface that will be applied by the web
        browser. The web browser will only be able to apply a font if
        it is available on the system which it operates. Provide
        multiple font families, separated by commas, to indicate the
        preference in which to apply fonts if they aren't available on
        the system. The Chart Studio Cloud (at https://chart-
        studio.plotly.com or on-premise) generates images on a server,
        where only a select number of fonts are installed and
        supported. These include "Arial", "Balto", "Courier New",
        "Droid Sans", "Droid Serif", "Droid Sans Mono", "Gravitas One",
        "Old Standard TT", "Open Sans", "Overpass", "PT Sans Narrow",
        "Raleway", "Times New Roman".

        The 'family' property is a string and must be specified as:
          - A non-empty string

        Returns
        -------
        str
        """
        return self['family']

    @family.setter
    def family(self, val):
        self['family'] = val

    # size
    # ----
    @property
    def size(self):
        """
        The 'size' property is a number and may be specified as:
          - An int or float in the interval [1, inf]

        Returns
        -------
        int|float
        """
        return self['size']

    @size.setter
    def size(self, val):
        self['size'] = val

    # style
    # -----
    @property
    def style(self):
        """
        Sets whether a font should be styled with a normal or italic
        face from its family.

        The 'style' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['normal', 'italic']

        Returns
        -------
        Any
        """
        return self['style']

    @style.setter
    def style(self, val):
        self['style'] = val

    # weight
    # ------
    @property
    def weight(self):
        """
        Sets the weight (or boldness) of the font.

        The 'weight' property is a integer and may be specified as:
          - An int (or float that will be cast to an int)
            in the interval [1, 1000]
            OR exactly one of ['normal', 'bold'] (e.g. 'bold')

        Returns
        -------
        int
        """
        return self['weight']

    @weight.setter
    def weight(self, val):
        self['weight'] = val

    # Self properties description
    # ---------------------------
    @property
    def _prop_descriptions(self):
        return """\
        color

        family
            HTML font family - the typeface that will be applied by
            the web browser. The web browser will only be able to
            apply a font if it is available on the system which it
            operates. Provide multiple font families, separated by
            commas, to indicate the preference in which to apply
            fonts if they aren't available on the system. The Chart
            Studio Cloud (at https://chart-studio.plotly.com or on-
            premise) generates images on a server, where only a
            select number of fonts are installed and supported.
            These include "Arial", "Balto", "Courier New", "Droid
            Sans", "Droid Serif", "Droid Sans Mono", "Gravitas
            One", "Old Standard TT", "Open Sans", "Overpass", "PT
            Sans Narrow", "Raleway", "Times New Roman".
        size

        style
            Sets whether a font should be styled with a normal or
            italic face from its family.
        weight
            Sets the weight (or boldness) of the font.
        """
    def __init__(self,
            arg=None,
            color=None,
            family=None,
            size=None,
            style=None,
            weight=None,
            **kwargs
        ):
        """
        Construct a new Textfont object

        Sets the icon text font (color=map.layer.paint.text-color,
        size=map.layer.layout.text-size). Has an effect only when
        `type` is set to "symbol".

        Parameters
        ----------
        arg
            dict of properties compatible with this constructor or
            an instance of
            :class:`plotly.graph_objs.scattermap.Textfont`
        color

        family
            HTML font family - the typeface that will be applied by
            the web browser. The web browser will only be able to
            apply a font if it is available on the system which it
            operates. Provide multiple font families, separated by
            commas, to indicate the preference in which to apply
            fonts if they aren't available on the system. The Chart
            Studio Cloud (at https://chart-studio.plotly.com or on-
            premise) generates images on a server, where only a
            select number of fonts are installed and supported.
            These include "Arial", "Balto", "Courier New", "Droid
            Sans", "Droid Serif", "Droid Sans Mono", "Gravitas
            One", "Old Standard TT", "Open Sans", "Overpass", "PT
            Sans Narrow", "Raleway", "Times New Roman".
        size

        style
            Sets whether a font should be styled with a normal or
            italic face from its family.
        weight
            Sets the weight (or boldness) of the font.

        Returns
        -------
        Textfont
        """
        super(Textfont, self).__init__('textfont')

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
The first argument to the plotly.graph_objs.scattermap.Textfont
constructor must be a dict or
an instance of :class:`plotly.graph_objs.scattermap.Textfont`""")

        # Handle skip_invalid
        # -------------------
        self._skip_invalid = kwargs.pop('skip_invalid', False)
        self._validate = kwargs.pop('_validate', True)
        

        # Populate data dict with properties
        # ----------------------------------
        self._init_provided('color', arg, color)
        self._init_provided('family', arg, family)
        self._init_provided('size', arg, size)
        self._init_provided('style', arg, style)
        self._init_provided('weight', arg, weight)

        # Process unknown kwargs
        # ----------------------
        self._process_kwargs(**dict(arg, **kwargs))

        # Reset skip_invalid
        # ------------------
        self._skip_invalid = False
