from plotly.basedatatypes import BaseTraceHierarchyType as _BaseTraceHierarchyType
import copy as _copy


class Marker(_BaseTraceHierarchyType):

    # class properties
    # --------------------
    _parent_path_str = "scatter3d"
    _path_str = "scatter3d.marker"
    _valid_props = {
        "autocolorscale",
        "cauto",
        "cmax",
        "cmid",
        "cmin",
        "color",
        "coloraxis",
        "colorbar",
        "colorscale",
        "colorsrc",
        "line",
        "opacity",
        "reversescale",
        "showscale",
        "size",
        "sizemin",
        "sizemode",
        "sizeref",
        "sizesrc",
        "symbol",
        "symbolsrc",
    }

    # autocolorscale
    # --------------
    @property
    def autocolorscale(self):
        """
        Determines whether the colorscale is a default palette
        (`autocolorscale: true`) or the palette determined by
        `marker.colorscale`. Has an effect only if in `marker.color` is
        set to a numerical array. In case `colorscale` is unspecified
        or `autocolorscale` is true, the default palette will be chosen
        according to whether numbers in the `color` array are all
        positive, all negative or mixed.

        The 'autocolorscale' property must be specified as a bool
        (either True, or False)

        Returns
        -------
        bool
        """
        return self["autocolorscale"]

    @autocolorscale.setter
    def autocolorscale(self, val):
        self["autocolorscale"] = val

    # cauto
    # -----
    @property
    def cauto(self):
        """
        Determines whether or not the color domain is computed with
        respect to the input data (here in `marker.color`) or the
        bounds set in `marker.cmin` and `marker.cmax` Has an effect
        only if in `marker.color` is set to a numerical array. Defaults
        to `false` when `marker.cmin` and `marker.cmax` are set by the
        user.

        The 'cauto' property must be specified as a bool
        (either True, or False)

        Returns
        -------
        bool
        """
        return self["cauto"]

    @cauto.setter
    def cauto(self, val):
        self["cauto"] = val

    # cmax
    # ----
    @property
    def cmax(self):
        """
        Sets the upper bound of the color domain. Has an effect only if
        in `marker.color` is set to a numerical array. Value should
        have the same units as in `marker.color` and if set,
        `marker.cmin` must be set as well.

        The 'cmax' property is a number and may be specified as:
          - An int or float

        Returns
        -------
        int|float
        """
        return self["cmax"]

    @cmax.setter
    def cmax(self, val):
        self["cmax"] = val

    # cmid
    # ----
    @property
    def cmid(self):
        """
        Sets the mid-point of the color domain by scaling `marker.cmin`
        and/or `marker.cmax` to be equidistant to this point. Has an
        effect only if in `marker.color` is set to a numerical array.
        Value should have the same units as in `marker.color`. Has no
        effect when `marker.cauto` is `false`.

        The 'cmid' property is a number and may be specified as:
          - An int or float

        Returns
        -------
        int|float
        """
        return self["cmid"]

    @cmid.setter
    def cmid(self, val):
        self["cmid"] = val

    # cmin
    # ----
    @property
    def cmin(self):
        """
        Sets the lower bound of the color domain. Has an effect only if
        in `marker.color` is set to a numerical array. Value should
        have the same units as in `marker.color` and if set,
        `marker.cmax` must be set as well.

        The 'cmin' property is a number and may be specified as:
          - An int or float

        Returns
        -------
        int|float
        """
        return self["cmin"]

    @cmin.setter
    def cmin(self, val):
        self["cmin"] = val

    # color
    # -----
    @property
    def color(self):
        """
        Sets the marker color. It accepts either a specific color or an
        array of numbers that are mapped to the colorscale relative to
        the max and min values of the array or relative to
        `marker.cmin` and `marker.cmax` if set.

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
          - A number that will be interpreted as a color
            according to scatter3d.marker.colorscale
          - A list or array of any of the above

        Returns
        -------
        str|numpy.ndarray
        """
        return self["color"]

    @color.setter
    def color(self, val):
        self["color"] = val

    # coloraxis
    # ---------
    @property
    def coloraxis(self):
        """
        Sets a reference to a shared color axis. References to these
        shared color axes are "coloraxis", "coloraxis2", "coloraxis3",
        etc. Settings for these shared color axes are set in the
        layout, under `layout.coloraxis`, `layout.coloraxis2`, etc.
        Note that multiple color scales can be linked to the same color
        axis.

        The 'coloraxis' property is an identifier of a particular
        subplot, of type 'coloraxis', that may be specified as the string 'coloraxis'
        optionally followed by an integer >= 1
        (e.g. 'coloraxis', 'coloraxis1', 'coloraxis2', 'coloraxis3', etc.)

        Returns
        -------
        str
        """
        return self["coloraxis"]

    @coloraxis.setter
    def coloraxis(self, val):
        self["coloraxis"] = val

    # colorbar
    # --------
    @property
    def colorbar(self):
        """
        The 'colorbar' property is an instance of ColorBar
        that may be specified as:
          - An instance of :class:`plotly.graph_objs.scatter3d.marker.ColorBar`
          - A dict of string/value properties that will be passed
            to the ColorBar constructor

        Returns
        -------
        plotly.graph_objs.scatter3d.marker.ColorBar
        """
        return self["colorbar"]

    @colorbar.setter
    def colorbar(self, val):
        self["colorbar"] = val

    # colorscale
    # ----------
    @property
    def colorscale(self):
        """
        Sets the colorscale. Has an effect only if in `marker.color` is
        set to a numerical array. The colorscale must be an array
        containing arrays mapping a normalized value to an rgb, rgba,
        hex, hsl, hsv, or named color string. At minimum, a mapping for
        the lowest (0) and highest (1) values are required. For
        example, `[[0, 'rgb(0,0,255)'], [1, 'rgb(255,0,0)']]`. To
        control the bounds of the colorscale in color space, use
        `marker.cmin` and `marker.cmax`. Alternatively, `colorscale`
        may be a palette name string of the following list: Blackbody,B
        luered,Blues,Cividis,Earth,Electric,Greens,Greys,Hot,Jet,Picnic
        ,Portland,Rainbow,RdBu,Reds,Viridis,YlGnBu,YlOrRd.

        The 'colorscale' property is a colorscale and may be
        specified as:
          - A list of colors that will be spaced evenly to create the colorscale.
            Many predefined colorscale lists are included in the sequential, diverging,
            and cyclical modules in the plotly.colors package.
          - A list of 2-element lists where the first element is the
            normalized color level value (starting at 0 and ending at 1),
            and the second item is a valid color string.
            (e.g. [[0, 'green'], [0.5, 'red'], [1.0, 'rgb(0, 0, 255)']])
          - One of the following named colorscales:
                ['aggrnyl', 'agsunset', 'algae', 'amp', 'armyrose', 'balance',
                 'blackbody', 'bluered', 'blues', 'blugrn', 'bluyl', 'brbg',
                 'brwnyl', 'bugn', 'bupu', 'burg', 'burgyl', 'cividis', 'curl',
                 'darkmint', 'deep', 'delta', 'dense', 'earth', 'edge', 'electric',
                 'emrld', 'fall', 'geyser', 'gnbu', 'gray', 'greens', 'greys',
                 'haline', 'hot', 'hsv', 'ice', 'icefire', 'inferno', 'jet',
                 'magenta', 'magma', 'matter', 'mint', 'mrybm', 'mygbm', 'oranges',
                 'orrd', 'oryel', 'oxy', 'peach', 'phase', 'picnic', 'pinkyl',
                 'piyg', 'plasma', 'plotly3', 'portland', 'prgn', 'pubu', 'pubugn',
                 'puor', 'purd', 'purp', 'purples', 'purpor', 'rainbow', 'rdbu',
                 'rdgy', 'rdpu', 'rdylbu', 'rdylgn', 'redor', 'reds', 'solar',
                 'spectral', 'speed', 'sunset', 'sunsetdark', 'teal', 'tealgrn',
                 'tealrose', 'tempo', 'temps', 'thermal', 'tropic', 'turbid',
                 'turbo', 'twilight', 'viridis', 'ylgn', 'ylgnbu', 'ylorbr',
                 'ylorrd'].
            Appending '_r' to a named colorscale reverses it.

        Returns
        -------
        str
        """
        return self["colorscale"]

    @colorscale.setter
    def colorscale(self, val):
        self["colorscale"] = val

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
        return self["colorsrc"]

    @colorsrc.setter
    def colorsrc(self, val):
        self["colorsrc"] = val

    # line
    # ----
    @property
    def line(self):
        """
        The 'line' property is an instance of Line
        that may be specified as:
          - An instance of :class:`plotly.graph_objs.scatter3d.marker.Line`
          - A dict of string/value properties that will be passed
            to the Line constructor

        Returns
        -------
        plotly.graph_objs.scatter3d.marker.Line
        """
        return self["line"]

    @line.setter
    def line(self, val):
        self["line"] = val

    # opacity
    # -------
    @property
    def opacity(self):
        """
        Sets the marker opacity. Note that the marker opacity for
        scatter3d traces must be a scalar value for performance
        reasons. To set a blending opacity value (i.e. which is not
        transparent), set "marker.color" to an rgba color and use its
        alpha channel.

        The 'opacity' property is a number and may be specified as:
          - An int or float in the interval [0, 1]

        Returns
        -------
        int|float
        """
        return self["opacity"]

    @opacity.setter
    def opacity(self, val):
        self["opacity"] = val

    # reversescale
    # ------------
    @property
    def reversescale(self):
        """
        Reverses the color mapping if true. Has an effect only if in
        `marker.color` is set to a numerical array. If true,
        `marker.cmin` will correspond to the last color in the array
        and `marker.cmax` will correspond to the first color.

        The 'reversescale' property must be specified as a bool
        (either True, or False)

        Returns
        -------
        bool
        """
        return self["reversescale"]

    @reversescale.setter
    def reversescale(self, val):
        self["reversescale"] = val

    # showscale
    # ---------
    @property
    def showscale(self):
        """
        Determines whether or not a colorbar is displayed for this
        trace. Has an effect only if in `marker.color` is set to a
        numerical array.

        The 'showscale' property must be specified as a bool
        (either True, or False)

        Returns
        -------
        bool
        """
        return self["showscale"]

    @showscale.setter
    def showscale(self, val):
        self["showscale"] = val

    # size
    # ----
    @property
    def size(self):
        """
        Sets the marker size (in px).

        The 'size' property is a number and may be specified as:
          - An int or float in the interval [0, inf]
          - A tuple, list, or one-dimensional numpy array of the above

        Returns
        -------
        int|float|numpy.ndarray
        """
        return self["size"]

    @size.setter
    def size(self, val):
        self["size"] = val

    # sizemin
    # -------
    @property
    def sizemin(self):
        """
        Has an effect only if `marker.size` is set to a numerical
        array. Sets the minimum size (in px) of the rendered marker
        points.

        The 'sizemin' property is a number and may be specified as:
          - An int or float in the interval [0, inf]

        Returns
        -------
        int|float
        """
        return self["sizemin"]

    @sizemin.setter
    def sizemin(self, val):
        self["sizemin"] = val

    # sizemode
    # --------
    @property
    def sizemode(self):
        """
        Has an effect only if `marker.size` is set to a numerical
        array. Sets the rule for which the data in `size` is converted
        to pixels.

        The 'sizemode' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['diameter', 'area']

        Returns
        -------
        Any
        """
        return self["sizemode"]

    @sizemode.setter
    def sizemode(self, val):
        self["sizemode"] = val

    # sizeref
    # -------
    @property
    def sizeref(self):
        """
        Has an effect only if `marker.size` is set to a numerical
        array. Sets the scale factor used to determine the rendered
        size of marker points. Use with `sizemin` and `sizemode`.

        The 'sizeref' property is a number and may be specified as:
          - An int or float

        Returns
        -------
        int|float
        """
        return self["sizeref"]

    @sizeref.setter
    def sizeref(self, val):
        self["sizeref"] = val

    # sizesrc
    # -------
    @property
    def sizesrc(self):
        """
        Sets the source reference on Chart Studio Cloud for `size`.

        The 'sizesrc' property must be specified as a string or
        as a plotly.grid_objs.Column object

        Returns
        -------
        str
        """
        return self["sizesrc"]

    @sizesrc.setter
    def sizesrc(self, val):
        self["sizesrc"] = val

    # symbol
    # ------
    @property
    def symbol(self):
        """
        Sets the marker symbol type.

        The 'symbol' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['circle', 'circle-open', 'cross', 'diamond',
                'diamond-open', 'square', 'square-open', 'x']
          - A tuple, list, or one-dimensional numpy array of the above

        Returns
        -------
        Any|numpy.ndarray
        """
        return self["symbol"]

    @symbol.setter
    def symbol(self, val):
        self["symbol"] = val

    # symbolsrc
    # ---------
    @property
    def symbolsrc(self):
        """
        Sets the source reference on Chart Studio Cloud for `symbol`.

        The 'symbolsrc' property must be specified as a string or
        as a plotly.grid_objs.Column object

        Returns
        -------
        str
        """
        return self["symbolsrc"]

    @symbolsrc.setter
    def symbolsrc(self, val):
        self["symbolsrc"] = val

    # Self properties description
    # ---------------------------
    @property
    def _prop_descriptions(self):
        return """\
        autocolorscale
            Determines whether the colorscale is a default palette
            (`autocolorscale: true`) or the palette determined by
            `marker.colorscale`. Has an effect only if in
            `marker.color` is set to a numerical array. In case
            `colorscale` is unspecified or `autocolorscale` is
            true, the default palette will be chosen according to
            whether numbers in the `color` array are all positive,
            all negative or mixed.
        cauto
            Determines whether or not the color domain is computed
            with respect to the input data (here in `marker.color`)
            or the bounds set in `marker.cmin` and `marker.cmax`
            Has an effect only if in `marker.color` is set to a
            numerical array. Defaults to `false` when `marker.cmin`
            and `marker.cmax` are set by the user.
        cmax
            Sets the upper bound of the color domain. Has an effect
            only if in `marker.color` is set to a numerical array.
            Value should have the same units as in `marker.color`
            and if set, `marker.cmin` must be set as well.
        cmid
            Sets the mid-point of the color domain by scaling
            `marker.cmin` and/or `marker.cmax` to be equidistant to
            this point. Has an effect only if in `marker.color` is
            set to a numerical array. Value should have the same
            units as in `marker.color`. Has no effect when
            `marker.cauto` is `false`.
        cmin
            Sets the lower bound of the color domain. Has an effect
            only if in `marker.color` is set to a numerical array.
            Value should have the same units as in `marker.color`
            and if set, `marker.cmax` must be set as well.
        color
            Sets the marker color. It accepts either a specific
            color or an array of numbers that are mapped to the
            colorscale relative to the max and min values of the
            array or relative to `marker.cmin` and `marker.cmax` if
            set.
        coloraxis
            Sets a reference to a shared color axis. References to
            these shared color axes are "coloraxis", "coloraxis2",
            "coloraxis3", etc. Settings for these shared color axes
            are set in the layout, under `layout.coloraxis`,
            `layout.coloraxis2`, etc. Note that multiple color
            scales can be linked to the same color axis.
        colorbar
            :class:`plotly.graph_objects.scatter3d.marker.ColorBar`
            instance or dict with compatible properties
        colorscale
            Sets the colorscale. Has an effect only if in
            `marker.color` is set to a numerical array. The
            colorscale must be an array containing arrays mapping a
            normalized value to an rgb, rgba, hex, hsl, hsv, or
            named color string. At minimum, a mapping for the
            lowest (0) and highest (1) values are required. For
            example, `[[0, 'rgb(0,0,255)'], [1, 'rgb(255,0,0)']]`.
            To control the bounds of the colorscale in color space,
            use `marker.cmin` and `marker.cmax`. Alternatively,
            `colorscale` may be a palette name string of the
            following list: Blackbody,Bluered,Blues,Cividis,Earth,E
            lectric,Greens,Greys,Hot,Jet,Picnic,Portland,Rainbow,Rd
            Bu,Reds,Viridis,YlGnBu,YlOrRd.
        colorsrc
            Sets the source reference on Chart Studio Cloud for
            `color`.
        line
            :class:`plotly.graph_objects.scatter3d.marker.Line`
            instance or dict with compatible properties
        opacity
            Sets the marker opacity. Note that the marker opacity
            for scatter3d traces must be a scalar value for
            performance reasons. To set a blending opacity value
            (i.e. which is not transparent), set "marker.color" to
            an rgba color and use its alpha channel.
        reversescale
            Reverses the color mapping if true. Has an effect only
            if in `marker.color` is set to a numerical array. If
            true, `marker.cmin` will correspond to the last color
            in the array and `marker.cmax` will correspond to the
            first color.
        showscale
            Determines whether or not a colorbar is displayed for
            this trace. Has an effect only if in `marker.color` is
            set to a numerical array.
        size
            Sets the marker size (in px).
        sizemin
            Has an effect only if `marker.size` is set to a
            numerical array. Sets the minimum size (in px) of the
            rendered marker points.
        sizemode
            Has an effect only if `marker.size` is set to a
            numerical array. Sets the rule for which the data in
            `size` is converted to pixels.
        sizeref
            Has an effect only if `marker.size` is set to a
            numerical array. Sets the scale factor used to
            determine the rendered size of marker points. Use with
            `sizemin` and `sizemode`.
        sizesrc
            Sets the source reference on Chart Studio Cloud for
            `size`.
        symbol
            Sets the marker symbol type.
        symbolsrc
            Sets the source reference on Chart Studio Cloud for
            `symbol`.
        """

    def __init__(
        self,
        arg=None,
        autocolorscale=None,
        cauto=None,
        cmax=None,
        cmid=None,
        cmin=None,
        color=None,
        coloraxis=None,
        colorbar=None,
        colorscale=None,
        colorsrc=None,
        line=None,
        opacity=None,
        reversescale=None,
        showscale=None,
        size=None,
        sizemin=None,
        sizemode=None,
        sizeref=None,
        sizesrc=None,
        symbol=None,
        symbolsrc=None,
        **kwargs,
    ):
        """
        Construct a new Marker object

        Parameters
        ----------
        arg
            dict of properties compatible with this constructor or
            an instance of
            :class:`plotly.graph_objs.scatter3d.Marker`
        autocolorscale
            Determines whether the colorscale is a default palette
            (`autocolorscale: true`) or the palette determined by
            `marker.colorscale`. Has an effect only if in
            `marker.color` is set to a numerical array. In case
            `colorscale` is unspecified or `autocolorscale` is
            true, the default palette will be chosen according to
            whether numbers in the `color` array are all positive,
            all negative or mixed.
        cauto
            Determines whether or not the color domain is computed
            with respect to the input data (here in `marker.color`)
            or the bounds set in `marker.cmin` and `marker.cmax`
            Has an effect only if in `marker.color` is set to a
            numerical array. Defaults to `false` when `marker.cmin`
            and `marker.cmax` are set by the user.
        cmax
            Sets the upper bound of the color domain. Has an effect
            only if in `marker.color` is set to a numerical array.
            Value should have the same units as in `marker.color`
            and if set, `marker.cmin` must be set as well.
        cmid
            Sets the mid-point of the color domain by scaling
            `marker.cmin` and/or `marker.cmax` to be equidistant to
            this point. Has an effect only if in `marker.color` is
            set to a numerical array. Value should have the same
            units as in `marker.color`. Has no effect when
            `marker.cauto` is `false`.
        cmin
            Sets the lower bound of the color domain. Has an effect
            only if in `marker.color` is set to a numerical array.
            Value should have the same units as in `marker.color`
            and if set, `marker.cmax` must be set as well.
        color
            Sets the marker color. It accepts either a specific
            color or an array of numbers that are mapped to the
            colorscale relative to the max and min values of the
            array or relative to `marker.cmin` and `marker.cmax` if
            set.
        coloraxis
            Sets a reference to a shared color axis. References to
            these shared color axes are "coloraxis", "coloraxis2",
            "coloraxis3", etc. Settings for these shared color axes
            are set in the layout, under `layout.coloraxis`,
            `layout.coloraxis2`, etc. Note that multiple color
            scales can be linked to the same color axis.
        colorbar
            :class:`plotly.graph_objects.scatter3d.marker.ColorBar`
            instance or dict with compatible properties
        colorscale
            Sets the colorscale. Has an effect only if in
            `marker.color` is set to a numerical array. The
            colorscale must be an array containing arrays mapping a
            normalized value to an rgb, rgba, hex, hsl, hsv, or
            named color string. At minimum, a mapping for the
            lowest (0) and highest (1) values are required. For
            example, `[[0, 'rgb(0,0,255)'], [1, 'rgb(255,0,0)']]`.
            To control the bounds of the colorscale in color space,
            use `marker.cmin` and `marker.cmax`. Alternatively,
            `colorscale` may be a palette name string of the
            following list: Blackbody,Bluered,Blues,Cividis,Earth,E
            lectric,Greens,Greys,Hot,Jet,Picnic,Portland,Rainbow,Rd
            Bu,Reds,Viridis,YlGnBu,YlOrRd.
        colorsrc
            Sets the source reference on Chart Studio Cloud for
            `color`.
        line
            :class:`plotly.graph_objects.scatter3d.marker.Line`
            instance or dict with compatible properties
        opacity
            Sets the marker opacity. Note that the marker opacity
            for scatter3d traces must be a scalar value for
            performance reasons. To set a blending opacity value
            (i.e. which is not transparent), set "marker.color" to
            an rgba color and use its alpha channel.
        reversescale
            Reverses the color mapping if true. Has an effect only
            if in `marker.color` is set to a numerical array. If
            true, `marker.cmin` will correspond to the last color
            in the array and `marker.cmax` will correspond to the
            first color.
        showscale
            Determines whether or not a colorbar is displayed for
            this trace. Has an effect only if in `marker.color` is
            set to a numerical array.
        size
            Sets the marker size (in px).
        sizemin
            Has an effect only if `marker.size` is set to a
            numerical array. Sets the minimum size (in px) of the
            rendered marker points.
        sizemode
            Has an effect only if `marker.size` is set to a
            numerical array. Sets the rule for which the data in
            `size` is converted to pixels.
        sizeref
            Has an effect only if `marker.size` is set to a
            numerical array. Sets the scale factor used to
            determine the rendered size of marker points. Use with
            `sizemin` and `sizemode`.
        sizesrc
            Sets the source reference on Chart Studio Cloud for
            `size`.
        symbol
            Sets the marker symbol type.
        symbolsrc
            Sets the source reference on Chart Studio Cloud for
            `symbol`.

        Returns
        -------
        Marker
        """
        super(Marker, self).__init__("marker")

        if "_parent" in kwargs:
            self._parent = kwargs["_parent"]
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
            raise ValueError(
                """\
The first argument to the plotly.graph_objs.scatter3d.Marker
constructor must be a dict or
an instance of :class:`plotly.graph_objs.scatter3d.Marker`"""
            )

        # Handle skip_invalid
        # -------------------
        self._skip_invalid = kwargs.pop("skip_invalid", False)
        self._validate = kwargs.pop("_validate", True)

        # Populate data dict with properties
        # ----------------------------------
        _v = arg.pop("autocolorscale", None)
        _v = autocolorscale if autocolorscale is not None else _v
        if _v is not None:
            self["autocolorscale"] = _v
        _v = arg.pop("cauto", None)
        _v = cauto if cauto is not None else _v
        if _v is not None:
            self["cauto"] = _v
        _v = arg.pop("cmax", None)
        _v = cmax if cmax is not None else _v
        if _v is not None:
            self["cmax"] = _v
        _v = arg.pop("cmid", None)
        _v = cmid if cmid is not None else _v
        if _v is not None:
            self["cmid"] = _v
        _v = arg.pop("cmin", None)
        _v = cmin if cmin is not None else _v
        if _v is not None:
            self["cmin"] = _v
        _v = arg.pop("color", None)
        _v = color if color is not None else _v
        if _v is not None:
            self["color"] = _v
        _v = arg.pop("coloraxis", None)
        _v = coloraxis if coloraxis is not None else _v
        if _v is not None:
            self["coloraxis"] = _v
        _v = arg.pop("colorbar", None)
        _v = colorbar if colorbar is not None else _v
        if _v is not None:
            self["colorbar"] = _v
        _v = arg.pop("colorscale", None)
        _v = colorscale if colorscale is not None else _v
        if _v is not None:
            self["colorscale"] = _v
        _v = arg.pop("colorsrc", None)
        _v = colorsrc if colorsrc is not None else _v
        if _v is not None:
            self["colorsrc"] = _v
        _v = arg.pop("line", None)
        _v = line if line is not None else _v
        if _v is not None:
            self["line"] = _v
        _v = arg.pop("opacity", None)
        _v = opacity if opacity is not None else _v
        if _v is not None:
            self["opacity"] = _v
        _v = arg.pop("reversescale", None)
        _v = reversescale if reversescale is not None else _v
        if _v is not None:
            self["reversescale"] = _v
        _v = arg.pop("showscale", None)
        _v = showscale if showscale is not None else _v
        if _v is not None:
            self["showscale"] = _v
        _v = arg.pop("size", None)
        _v = size if size is not None else _v
        if _v is not None:
            self["size"] = _v
        _v = arg.pop("sizemin", None)
        _v = sizemin if sizemin is not None else _v
        if _v is not None:
            self["sizemin"] = _v
        _v = arg.pop("sizemode", None)
        _v = sizemode if sizemode is not None else _v
        if _v is not None:
            self["sizemode"] = _v
        _v = arg.pop("sizeref", None)
        _v = sizeref if sizeref is not None else _v
        if _v is not None:
            self["sizeref"] = _v
        _v = arg.pop("sizesrc", None)
        _v = sizesrc if sizesrc is not None else _v
        if _v is not None:
            self["sizesrc"] = _v
        _v = arg.pop("symbol", None)
        _v = symbol if symbol is not None else _v
        if _v is not None:
            self["symbol"] = _v
        _v = arg.pop("symbolsrc", None)
        _v = symbolsrc if symbolsrc is not None else _v
        if _v is not None:
            self["symbolsrc"] = _v

        # Process unknown kwargs
        # ----------------------
        self._process_kwargs(**dict(arg, **kwargs))

        # Reset skip_invalid
        # ------------------
        self._skip_invalid = False
