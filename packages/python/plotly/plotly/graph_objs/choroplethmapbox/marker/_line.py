

from plotly.basedatatypes import BaseTraceHierarchyType as _BaseTraceHierarchyType
import copy as _copy


class Line(_BaseTraceHierarchyType):

    # class properties
    # --------------------
    _parent_path_str = 'choroplethmapbox.marker'
    _path_str = 'choroplethmapbox.marker.line'
    _valid_props = {"color", "colorsrc", "width", "widthsrc"}

    # color
    # -----
    @property
    def color(self):
        """
        Sets the marker.line color. It accepts either a specific color
        or an array of numbers that are mapped to the colorscale
        relative to the max and min values of the array or relative to
        `marker.line.cmin` and `marker.line.cmax` if set.

        The 'color' property is a color and may be specified as:
          - A hex string (e.g. '#ff0000')
          - An rgb/rgba string (e.g. 'rgb(255,0,0)')
          - An hsl/hsla string (e.g. 'hsl(0,100%,50%)')
          - An hsv/hsva string (e.g. 'hsv(0,100%,100%)')
          - A named CSS color:
                aliceblue, antiquewhite, aqua, aquamarine, azure,
                beige, bisque, black, blanchedalmond, blue,
                blueviolet, brown, burlywood, cadetblue,
                chartreuse, chocolate, coral, cornflowerblue,
                cornsilk, crimson, cyan, darkblue, darkcyan,
                darkgoldenrod, darkgray, darkgrey, darkgreen,
                darkkhaki, darkmagenta, darkolivegreen, darkorange,
                darkorchid, darkred, darksalmon, darkseagreen,
                darkslateblue, darkslategray, darkslategrey,
                darkturquoise, darkviolet, deeppink, deepskyblue,
                dimgray, dimgrey, dodgerblue, firebrick,
                floralwhite, forestgreen, fuchsia, gainsboro,
                ghostwhite, gold, goldenrod, gray, grey, green,
                greenyellow, honeydew, hotpink, indianred, indigo,
                ivory, khaki, lavender, lavenderblush, lawngreen,
                lemonchiffon, lightblue, lightcoral, lightcyan,
                lightgoldenrodyellow, lightgray, lightgrey,
                lightgreen, lightpink, lightsalmon, lightseagreen,
                lightskyblue, lightslategray, lightslategrey,
                lightsteelblue, lightyellow, lime, limegreen,
                linen, magenta, maroon, mediumaquamarine,
                mediumblue, mediumorchid, mediumpurple,
                mediumseagreen, mediumslateblue, mediumspringgreen,
                mediumturquoise, mediumvioletred, midnightblue,
                mintcream, mistyrose, moccasin, navajowhite, navy,
                oldlace, olive, olivedrab, orange, orangered,
                orchid, palegoldenrod, palegreen, paleturquoise,
                palevioletred, papayawhip, peachpuff, peru, pink,
                plum, powderblue, purple, red, rosybrown,
                royalblue, rebeccapurple, saddlebrown, salmon,
                sandybrown, seagreen, seashell, sienna, silver,
                skyblue, slateblue, slategray, slategrey, snow,
                springgreen, steelblue, tan, teal, thistle, tomato,
                turquoise, violet, wheat, white, whitesmoke,
                yellow, yellowgreen
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

    # width
    # -----
    @property
    def width(self):
        """
        Sets the width (in px) of the lines bounding the marker points.

        The 'width' property is a number and may be specified as:
          - An int or float in the interval [0, inf]
          - A tuple, list, or one-dimensional numpy array of the above

        Returns
        -------
        int|float|numpy.ndarray
        """
        return self['width']

    @width.setter
    def width(self, val):
        self['width'] = val

    # widthsrc
    # --------
    @property
    def widthsrc(self):
        """
        Sets the source reference on Chart Studio Cloud for `width`.

        The 'widthsrc' property must be specified as a string or
        as a plotly.grid_objs.Column object

        Returns
        -------
        str
        """
        return self['widthsrc']

    @widthsrc.setter
    def widthsrc(self, val):
        self['widthsrc'] = val

    # Self properties description
    # ---------------------------
    @property
    def _prop_descriptions(self):
        return """\
        color
            Sets the marker.line color. It accepts either a
            specific color or an array of numbers that are mapped
            to the colorscale relative to the max and min values of
            the array or relative to `marker.line.cmin` and
            `marker.line.cmax` if set.
        colorsrc
            Sets the source reference on Chart Studio Cloud for
            `color`.
        width
            Sets the width (in px) of the lines bounding the marker
            points.
        widthsrc
            Sets the source reference on Chart Studio Cloud for
            `width`.
        """
    def __init__(self,
            arg=None,
            color=None,
            colorsrc=None,
            width=None,
            widthsrc=None,
            **kwargs
        ):
        """
        Construct a new Line object

        Parameters
        ----------
        arg
            dict of properties compatible with this constructor or
            an instance of
            :class:`plotly.graph_objs.choroplethmapbox.marker.Line`
        color
            Sets the marker.line color. It accepts either a
            specific color or an array of numbers that are mapped
            to the colorscale relative to the max and min values of
            the array or relative to `marker.line.cmin` and
            `marker.line.cmax` if set.
        colorsrc
            Sets the source reference on Chart Studio Cloud for
            `color`.
        width
            Sets the width (in px) of the lines bounding the marker
            points.
        widthsrc
            Sets the source reference on Chart Studio Cloud for
            `width`.

        Returns
        -------
        Line
        """
        super(Line, self).__init__('line')

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
The first argument to the plotly.graph_objs.choroplethmapbox.marker.Line
constructor must be a dict or
an instance of :class:`plotly.graph_objs.choroplethmapbox.marker.Line`""")

        # Handle skip_invalid
        # -------------------
        self._skip_invalid = kwargs.pop('skip_invalid', False)
        self._validate = kwargs.pop('_validate', True)
        

        # Populate data dict with properties
        # ----------------------------------
        self._init_provided('color', arg, color)
        self._init_provided('colorsrc', arg, colorsrc)
        self._init_provided('width', arg, width)
        self._init_provided('widthsrc', arg, widthsrc)

        # Process unknown kwargs
        # ----------------------
        self._process_kwargs(**dict(arg, **kwargs))

        # Reset skip_invalid
        # ------------------
        self._skip_invalid = False
