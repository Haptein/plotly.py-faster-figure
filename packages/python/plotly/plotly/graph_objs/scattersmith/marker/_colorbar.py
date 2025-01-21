

from plotly.basedatatypes import BaseTraceHierarchyType as _BaseTraceHierarchyType
import copy as _copy


class ColorBar(_BaseTraceHierarchyType):

    # class properties
    # --------------------
    _parent_path_str = 'scattersmith.marker'
    _path_str = 'scattersmith.marker.colorbar'
    _valid_props = {"bgcolor", "bordercolor", "borderwidth", "dtick", "exponentformat", "labelalias", "len", "lenmode", "minexponent", "nticks", "orientation", "outlinecolor", "outlinewidth", "separatethousands", "showexponent", "showticklabels", "showtickprefix", "showticksuffix", "thickness", "thicknessmode", "tick0", "tickangle", "tickcolor", "tickfont", "tickformat", "tickformatstopdefaults", "tickformatstops", "ticklabeloverflow", "ticklabelposition", "ticklabelstep", "ticklen", "tickmode", "tickprefix", "ticks", "ticksuffix", "ticktext", "ticktextsrc", "tickvals", "tickvalssrc", "tickwidth", "title", "x", "xanchor", "xpad", "xref", "y", "yanchor", "ypad", "yref"}

    # bgcolor
    # -------
    @property
    def bgcolor(self):
        """
        Sets the color of padded area.

        The 'bgcolor' property is a color and may be specified as:
          - A hex string (e.g. '#ff0000')
          - An rgb/rgba string (e.g. 'rgb(255,0,0)')
          - An hsl/hsla string (e.g. 'hsl(0,100%,50%)')
          - An hsv/hsva string (e.g. 'hsv(0,100%,100%)')
          - A named CSS color

        Returns
        -------
        str
        """
        return self['bgcolor']

    @bgcolor.setter
    def bgcolor(self, val):
        self['bgcolor'] = val

    # bordercolor
    # -----------
    @property
    def bordercolor(self):
        """
        Sets the axis line color.

        The 'bordercolor' property is a color and may be specified as:
          - A hex string (e.g. '#ff0000')
          - An rgb/rgba string (e.g. 'rgb(255,0,0)')
          - An hsl/hsla string (e.g. 'hsl(0,100%,50%)')
          - An hsv/hsva string (e.g. 'hsv(0,100%,100%)')
          - A named CSS color

        Returns
        -------
        str
        """
        return self['bordercolor']

    @bordercolor.setter
    def bordercolor(self, val):
        self['bordercolor'] = val

    # borderwidth
    # -----------
    @property
    def borderwidth(self):
        """
        Sets the width (in px) or the border enclosing this color bar.

        The 'borderwidth' property is a number and may be specified as:
          - An int or float in the interval [0, inf]

        Returns
        -------
        int|float
        """
        return self['borderwidth']

    @borderwidth.setter
    def borderwidth(self, val):
        self['borderwidth'] = val

    # dtick
    # -----
    @property
    def dtick(self):
        """
        Sets the step in-between ticks on this axis. Use with `tick0`.
        Must be a positive number, or special strings available to
        "log" and "date" axes. If the axis `type` is "log", then ticks
        are set every 10^(n*dtick) where n is the tick number. For
        example, to set a tick mark at 1, 10, 100, 1000, ... set dtick
        to 1. To set tick marks at 1, 100, 10000, ... set dtick to 2.
        To set tick marks at 1, 5, 25, 125, 625, 3125, ... set dtick to
        log_10(5), or 0.69897000433. "log" has several special values;
        "L<f>", where `f` is a positive number, gives ticks linearly
        spaced in value (but not position). For example `tick0` = 0.1,
        `dtick` = "L0.5" will put ticks at 0.1, 0.6, 1.1, 1.6 etc. To
        show powers of 10 plus small digits between, use "D1" (all
        digits) or "D2" (only 2 and 5). `tick0` is ignored for "D1" and
        "D2". If the axis `type` is "date", then you must convert the
        time to milliseconds. For example, to set the interval between
        ticks to one day, set `dtick` to 86400000.0. "date" also has
        special values "M<n>" gives ticks spaced by a number of months.
        `n` must be a positive integer. To set ticks on the 15th of
        every third month, set `tick0` to "2000-01-15" and `dtick` to
        "M3". To set ticks every 4 years, set `dtick` to "M48"

        The 'dtick' property accepts values of any type

        Returns
        -------
        Any
        """
        return self['dtick']

    @dtick.setter
    def dtick(self, val):
        self['dtick'] = val

    # exponentformat
    # --------------
    @property
    def exponentformat(self):
        """
        Determines a formatting rule for the tick exponents. For
        example, consider the number 1,000,000,000. If "none", it
        appears as 1,000,000,000. If "e", 1e+9. If "E", 1E+9. If
        "power", 1x10^9 (with 9 in a super script). If "SI", 1G. If
        "B", 1B.

        The 'exponentformat' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['none', 'e', 'E', 'power', 'SI', 'B']

        Returns
        -------
        Any
        """
        return self['exponentformat']

    @exponentformat.setter
    def exponentformat(self, val):
        self['exponentformat'] = val

    # labelalias
    # ----------
    @property
    def labelalias(self):
        """
        Replacement text for specific tick or hover labels. For example
        using {US: 'USA', CA: 'Canada'} changes US to USA and CA to
        Canada. The labels we would have shown must match the keys
        exactly, after adding any tickprefix or ticksuffix. For
        negative numbers the minus sign symbol used (U+2212) is wider
        than the regular ascii dash. That means you need to use −1
        instead of -1. labelalias can be used with any axis type, and
        both keys (if needed) and values (if desired) can include html-
        like tags or MathJax.

        The 'labelalias' property accepts values of any type

        Returns
        -------
        Any
        """
        return self['labelalias']

    @labelalias.setter
    def labelalias(self, val):
        self['labelalias'] = val

    # len
    # ---
    @property
    def len(self):
        """
        Sets the length of the color bar This measure excludes the
        padding of both ends. That is, the color bar length is this
        length minus the padding on both ends.

        The 'len' property is a number and may be specified as:
          - An int or float in the interval [0, inf]

        Returns
        -------
        int|float
        """
        return self['len']

    @len.setter
    def len(self, val):
        self['len'] = val

    # lenmode
    # -------
    @property
    def lenmode(self):
        """
        Determines whether this color bar's length (i.e. the measure in
        the color variation direction) is set in units of plot
        "fraction" or in *pixels. Use `len` to set the value.

        The 'lenmode' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['fraction', 'pixels']

        Returns
        -------
        Any
        """
        return self['lenmode']

    @lenmode.setter
    def lenmode(self, val):
        self['lenmode'] = val

    # minexponent
    # -----------
    @property
    def minexponent(self):
        """
        Hide SI prefix for 10^n if |n| is below this number. This only
        has an effect when `tickformat` is "SI" or "B".

        The 'minexponent' property is a number and may be specified as:
          - An int or float in the interval [0, inf]

        Returns
        -------
        int|float
        """
        return self['minexponent']

    @minexponent.setter
    def minexponent(self, val):
        self['minexponent'] = val

    # nticks
    # ------
    @property
    def nticks(self):
        """
        Specifies the maximum number of ticks for the particular axis.
        The actual number of ticks will be chosen automatically to be
        less than or equal to `nticks`. Has an effect only if
        `tickmode` is set to "auto".

        The 'nticks' property is a integer and may be specified as:
          - An int (or float that will be cast to an int)
            in the interval [0, 9223372036854775807]

        Returns
        -------
        int
        """
        return self['nticks']

    @nticks.setter
    def nticks(self, val):
        self['nticks'] = val

    # orientation
    # -----------
    @property
    def orientation(self):
        """
        Sets the orientation of the colorbar.

        The 'orientation' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['h', 'v']

        Returns
        -------
        Any
        """
        return self['orientation']

    @orientation.setter
    def orientation(self, val):
        self['orientation'] = val

    # outlinecolor
    # ------------
    @property
    def outlinecolor(self):
        """
        Sets the axis line color.

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

    # outlinewidth
    # ------------
    @property
    def outlinewidth(self):
        """
        Sets the width (in px) of the axis line.

        The 'outlinewidth' property is a number and may be specified as:
          - An int or float in the interval [0, inf]

        Returns
        -------
        int|float
        """
        return self['outlinewidth']

    @outlinewidth.setter
    def outlinewidth(self, val):
        self['outlinewidth'] = val

    # separatethousands
    # -----------------
    @property
    def separatethousands(self):
        """
        If "true", even 4-digit integers are separated

        The 'separatethousands' property must be specified as a bool
        (either True, or False)

        Returns
        -------
        bool
        """
        return self['separatethousands']

    @separatethousands.setter
    def separatethousands(self, val):
        self['separatethousands'] = val

    # showexponent
    # ------------
    @property
    def showexponent(self):
        """
        If "all", all exponents are shown besides their significands.
        If "first", only the exponent of the first tick is shown. If
        "last", only the exponent of the last tick is shown. If "none",
        no exponents appear.

        The 'showexponent' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['all', 'first', 'last', 'none']

        Returns
        -------
        Any
        """
        return self['showexponent']

    @showexponent.setter
    def showexponent(self, val):
        self['showexponent'] = val

    # showticklabels
    # --------------
    @property
    def showticklabels(self):
        """
        Determines whether or not the tick labels are drawn.

        The 'showticklabels' property must be specified as a bool
        (either True, or False)

        Returns
        -------
        bool
        """
        return self['showticklabels']

    @showticklabels.setter
    def showticklabels(self, val):
        self['showticklabels'] = val

    # showtickprefix
    # --------------
    @property
    def showtickprefix(self):
        """
        If "all", all tick labels are displayed with a prefix. If
        "first", only the first tick is displayed with a prefix. If
        "last", only the last tick is displayed with a suffix. If
        "none", tick prefixes are hidden.

        The 'showtickprefix' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['all', 'first', 'last', 'none']

        Returns
        -------
        Any
        """
        return self['showtickprefix']

    @showtickprefix.setter
    def showtickprefix(self, val):
        self['showtickprefix'] = val

    # showticksuffix
    # --------------
    @property
    def showticksuffix(self):
        """
        Same as `showtickprefix` but for tick suffixes.

        The 'showticksuffix' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['all', 'first', 'last', 'none']

        Returns
        -------
        Any
        """
        return self['showticksuffix']

    @showticksuffix.setter
    def showticksuffix(self, val):
        self['showticksuffix'] = val

    # thickness
    # ---------
    @property
    def thickness(self):
        """
        Sets the thickness of the color bar This measure excludes the
        size of the padding, ticks and labels.

        The 'thickness' property is a number and may be specified as:
          - An int or float in the interval [0, inf]

        Returns
        -------
        int|float
        """
        return self['thickness']

    @thickness.setter
    def thickness(self, val):
        self['thickness'] = val

    # thicknessmode
    # -------------
    @property
    def thicknessmode(self):
        """
        Determines whether this color bar's thickness (i.e. the measure
        in the constant color direction) is set in units of plot
        "fraction" or in "pixels". Use `thickness` to set the value.

        The 'thicknessmode' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['fraction', 'pixels']

        Returns
        -------
        Any
        """
        return self['thicknessmode']

    @thicknessmode.setter
    def thicknessmode(self, val):
        self['thicknessmode'] = val

    # tick0
    # -----
    @property
    def tick0(self):
        """
        Sets the placement of the first tick on this axis. Use with
        `dtick`. If the axis `type` is "log", then you must take the
        log of your starting tick (e.g. to set the starting tick to
        100, set the `tick0` to 2) except when `dtick`=*L<f>* (see
        `dtick` for more info). If the axis `type` is "date", it should
        be a date string, like date data. If the axis `type` is
        "category", it should be a number, using the scale where each
        category is assigned a serial number from zero in the order it
        appears.

        The 'tick0' property accepts values of any type

        Returns
        -------
        Any
        """
        return self['tick0']

    @tick0.setter
    def tick0(self, val):
        self['tick0'] = val

    # tickangle
    # ---------
    @property
    def tickangle(self):
        """
        Sets the angle of the tick labels with respect to the
        horizontal. For example, a `tickangle` of -90 draws the tick
        labels vertically.

        The 'tickangle' property is a angle (in degrees) that may be
        specified as a number between -180 and 180.
        Numeric values outside this range are converted to the equivalent value
        (e.g. 270 is converted to -90).

        Returns
        -------
        int|float
        """
        return self['tickangle']

    @tickangle.setter
    def tickangle(self, val):
        self['tickangle'] = val

    # tickcolor
    # ---------
    @property
    def tickcolor(self):
        """
        Sets the tick color.

        The 'tickcolor' property is a color and may be specified as:
          - A hex string (e.g. '#ff0000')
          - An rgb/rgba string (e.g. 'rgb(255,0,0)')
          - An hsl/hsla string (e.g. 'hsl(0,100%,50%)')
          - An hsv/hsva string (e.g. 'hsv(0,100%,100%)')
          - A named CSS color

        Returns
        -------
        str
        """
        return self['tickcolor']

    @tickcolor.setter
    def tickcolor(self, val):
        self['tickcolor'] = val

    # tickfont
    # --------
    @property
    def tickfont(self):
        """
        Sets the color bar's tick label font

        The 'tickfont' property is an instance of Tickfont
        that may be specified as:
          - An instance of :class:`plotly.graph_objs.scattersmith.marker.colorbar.Tickfont`
          - A dict of string/value properties that will be passed
            to the Tickfont constructor

        Returns
        -------
        plotly.graph_objs.scattersmith.marker.colorbar.Tickfont
        """
        return self['tickfont']

    @tickfont.setter
    def tickfont(self, val):
        self['tickfont'] = val

    # tickformat
    # ----------
    @property
    def tickformat(self):
        """
        Sets the tick label formatting rule using d3 formatting mini-
        languages which are very similar to those in Python. For
        numbers, see:
        https://github.com/d3/d3-format/tree/v1.4.5#d3-format. And for
        dates see: https://github.com/d3/d3-time-
        format/tree/v2.2.3#locale_format. We add two items to d3's date
        formatter: "%h" for half of the year as a decimal number as
        well as "%{n}f" for fractional seconds with n digits. For
        example, *2016-10-13 09:15:23.456* with tickformat
        "%H~%M~%S.%2f" would display "09~15~23.46"

        The 'tickformat' property is a string and must be specified as:
          - A string
          - A number that will be converted to a string

        Returns
        -------
        str
        """
        return self['tickformat']

    @tickformat.setter
    def tickformat(self, val):
        self['tickformat'] = val

    # tickformatstops
    # ---------------
    @property
    def tickformatstops(self):
        """
        The 'tickformatstops' property is a tuple of instances of
        Tickformatstop that may be specified as:
          - A list or tuple of instances of plotly.graph_objs.scattersmith.marker.colorbar.Tickformatstop
          - A list or tuple of dicts of string/value properties that
            will be passed to the Tickformatstop constructor

        Returns
        -------
        tuple[plotly.graph_objs.scattersmith.marker.colorbar.Tickformatstop]
        """
        return self['tickformatstops']

    @tickformatstops.setter
    def tickformatstops(self, val):
        self['tickformatstops'] = val

    # tickformatstopdefaults
    # ----------------------
    @property
    def tickformatstopdefaults(self):
        """
        When used in a template (as layout.template.data.scattersmith.m
        arker.colorbar.tickformatstopdefaults), sets the default
        property values to use for elements of
        scattersmith.marker.colorbar.tickformatstops

        The 'tickformatstopdefaults' property is an instance of Tickformatstop
        that may be specified as:
          - An instance of :class:`plotly.graph_objs.scattersmith.marker.colorbar.Tickformatstop`
          - A dict of string/value properties that will be passed
            to the Tickformatstop constructor

        Returns
        -------
        plotly.graph_objs.scattersmith.marker.colorbar.Tickformatstop
        """
        return self['tickformatstopdefaults']

    @tickformatstopdefaults.setter
    def tickformatstopdefaults(self, val):
        self['tickformatstopdefaults'] = val

    # ticklabeloverflow
    # -----------------
    @property
    def ticklabeloverflow(self):
        """
        Determines how we handle tick labels that would overflow either
        the graph div or the domain of the axis. The default value for
        inside tick labels is *hide past domain*. In other cases the
        default is *hide past div*.

        The 'ticklabeloverflow' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['allow', 'hide past div', 'hide past domain']

        Returns
        -------
        Any
        """
        return self['ticklabeloverflow']

    @ticklabeloverflow.setter
    def ticklabeloverflow(self, val):
        self['ticklabeloverflow'] = val

    # ticklabelposition
    # -----------------
    @property
    def ticklabelposition(self):
        """
        Determines where tick labels are drawn relative to the ticks.
        Left and right options are used when `orientation` is "h", top
        and bottom when `orientation` is "v".

        The 'ticklabelposition' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['outside', 'inside', 'outside top', 'inside top',
                'outside left', 'inside left', 'outside right', 'inside
                right', 'outside bottom', 'inside bottom']

        Returns
        -------
        Any
        """
        return self['ticklabelposition']

    @ticklabelposition.setter
    def ticklabelposition(self, val):
        self['ticklabelposition'] = val

    # ticklabelstep
    # -------------
    @property
    def ticklabelstep(self):
        """
        Sets the spacing between tick labels as compared to the spacing
        between ticks. A value of 1 (default) means each tick gets a
        label. A value of 2 means shows every 2nd label. A larger value
        n means only every nth tick is labeled. `tick0` determines
        which labels are shown. Not implemented for axes with `type`
        "log" or "multicategory", or when `tickmode` is "array".

        The 'ticklabelstep' property is a integer and may be specified as:
          - An int (or float that will be cast to an int)
            in the interval [1, 9223372036854775807]

        Returns
        -------
        int
        """
        return self['ticklabelstep']

    @ticklabelstep.setter
    def ticklabelstep(self, val):
        self['ticklabelstep'] = val

    # ticklen
    # -------
    @property
    def ticklen(self):
        """
        Sets the tick length (in px).

        The 'ticklen' property is a number and may be specified as:
          - An int or float in the interval [0, inf]

        Returns
        -------
        int|float
        """
        return self['ticklen']

    @ticklen.setter
    def ticklen(self, val):
        self['ticklen'] = val

    # tickmode
    # --------
    @property
    def tickmode(self):
        """
        Sets the tick mode for this axis. If "auto", the number of
        ticks is set via `nticks`. If "linear", the placement of the
        ticks is determined by a starting position `tick0` and a tick
        step `dtick` ("linear" is the default value if `tick0` and
        `dtick` are provided). If "array", the placement of the ticks
        is set via `tickvals` and the tick text is `ticktext`. ("array"
        is the default value if `tickvals` is provided).

        The 'tickmode' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['auto', 'linear', 'array']

        Returns
        -------
        Any
        """
        return self['tickmode']

    @tickmode.setter
    def tickmode(self, val):
        self['tickmode'] = val

    # tickprefix
    # ----------
    @property
    def tickprefix(self):
        """
        Sets a tick label prefix.

        The 'tickprefix' property is a string and must be specified as:
          - A string
          - A number that will be converted to a string

        Returns
        -------
        str
        """
        return self['tickprefix']

    @tickprefix.setter
    def tickprefix(self, val):
        self['tickprefix'] = val

    # ticks
    # -----
    @property
    def ticks(self):
        """
        Determines whether ticks are drawn or not. If "", this axis'
        ticks are not drawn. If "outside" ("inside"), this axis' are
        drawn outside (inside) the axis lines.

        The 'ticks' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['outside', 'inside', '']

        Returns
        -------
        Any
        """
        return self['ticks']

    @ticks.setter
    def ticks(self, val):
        self['ticks'] = val

    # ticksuffix
    # ----------
    @property
    def ticksuffix(self):
        """
        Sets a tick label suffix.

        The 'ticksuffix' property is a string and must be specified as:
          - A string
          - A number that will be converted to a string

        Returns
        -------
        str
        """
        return self['ticksuffix']

    @ticksuffix.setter
    def ticksuffix(self, val):
        self['ticksuffix'] = val

    # ticktext
    # --------
    @property
    def ticktext(self):
        """
        Sets the text displayed at the ticks position via `tickvals`.
        Only has an effect if `tickmode` is set to "array". Used with
        `tickvals`.

        The 'ticktext' property is an array that may be specified as a tuple,
        list, numpy array, or pandas Series

        Returns
        -------
        numpy.ndarray
        """
        return self['ticktext']

    @ticktext.setter
    def ticktext(self, val):
        self['ticktext'] = val

    # ticktextsrc
    # -----------
    @property
    def ticktextsrc(self):
        """
        Sets the source reference on Chart Studio Cloud for `ticktext`.

        The 'ticktextsrc' property must be specified as a string or
        as a plotly.grid_objs.Column object

        Returns
        -------
        str
        """
        return self['ticktextsrc']

    @ticktextsrc.setter
    def ticktextsrc(self, val):
        self['ticktextsrc'] = val

    # tickvals
    # --------
    @property
    def tickvals(self):
        """
        Sets the values at which ticks on this axis appear. Only has an
        effect if `tickmode` is set to "array". Used with `ticktext`.

        The 'tickvals' property is an array that may be specified as a tuple,
        list, numpy array, or pandas Series

        Returns
        -------
        numpy.ndarray
        """
        return self['tickvals']

    @tickvals.setter
    def tickvals(self, val):
        self['tickvals'] = val

    # tickvalssrc
    # -----------
    @property
    def tickvalssrc(self):
        """
        Sets the source reference on Chart Studio Cloud for `tickvals`.

        The 'tickvalssrc' property must be specified as a string or
        as a plotly.grid_objs.Column object

        Returns
        -------
        str
        """
        return self['tickvalssrc']

    @tickvalssrc.setter
    def tickvalssrc(self, val):
        self['tickvalssrc'] = val

    # tickwidth
    # ---------
    @property
    def tickwidth(self):
        """
        Sets the tick width (in px).

        The 'tickwidth' property is a number and may be specified as:
          - An int or float in the interval [0, inf]

        Returns
        -------
        int|float
        """
        return self['tickwidth']

    @tickwidth.setter
    def tickwidth(self, val):
        self['tickwidth'] = val

    # title
    # -----
    @property
    def title(self):
        """
        The 'title' property is an instance of Title
        that may be specified as:
          - An instance of :class:`plotly.graph_objs.scattersmith.marker.colorbar.Title`
          - A dict of string/value properties that will be passed
            to the Title constructor

        Returns
        -------
        plotly.graph_objs.scattersmith.marker.colorbar.Title
        """
        return self['title']

    @title.setter
    def title(self, val):
        self['title'] = val

    # x
    # -
    @property
    def x(self):
        """
        Sets the x position with respect to `xref` of the color bar (in
        plot fraction). When `xref` is "paper", defaults to 1.02 when
        `orientation` is "v" and 0.5 when `orientation` is "h". When
        `xref` is "container", defaults to 1 when `orientation` is "v"
        and 0.5 when `orientation` is "h". Must be between 0 and 1 if
        `xref` is "container" and between "-2" and 3 if `xref` is
        "paper".

        The 'x' property is a number and may be specified as:
          - An int or float

        Returns
        -------
        int|float
        """
        return self['x']

    @x.setter
    def x(self, val):
        self['x'] = val

    # xanchor
    # -------
    @property
    def xanchor(self):
        """
        Sets this color bar's horizontal position anchor. This anchor
        binds the `x` position to the "left", "center" or "right" of
        the color bar. Defaults to "left" when `orientation` is "v" and
        "center" when `orientation` is "h".

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

    # xpad
    # ----
    @property
    def xpad(self):
        """
        Sets the amount of padding (in px) along the x direction.

        The 'xpad' property is a number and may be specified as:
          - An int or float in the interval [0, inf]

        Returns
        -------
        int|float
        """
        return self['xpad']

    @xpad.setter
    def xpad(self, val):
        self['xpad'] = val

    # xref
    # ----
    @property
    def xref(self):
        """
        Sets the container `x` refers to. "container" spans the entire
        `width` of the plot. "paper" refers to the width of the
        plotting area only.

        The 'xref' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['container', 'paper']

        Returns
        -------
        Any
        """
        return self['xref']

    @xref.setter
    def xref(self, val):
        self['xref'] = val

    # y
    # -
    @property
    def y(self):
        """
        Sets the y position with respect to `yref` of the color bar (in
        plot fraction). When `yref` is "paper", defaults to 0.5 when
        `orientation` is "v" and 1.02 when `orientation` is "h". When
        `yref` is "container", defaults to 0.5 when `orientation` is
        "v" and 1 when `orientation` is "h". Must be between 0 and 1 if
        `yref` is "container" and between "-2" and 3 if `yref` is
        "paper".

        The 'y' property is a number and may be specified as:
          - An int or float

        Returns
        -------
        int|float
        """
        return self['y']

    @y.setter
    def y(self, val):
        self['y'] = val

    # yanchor
    # -------
    @property
    def yanchor(self):
        """
        Sets this color bar's vertical position anchor This anchor
        binds the `y` position to the "top", "middle" or "bottom" of
        the color bar. Defaults to "middle" when `orientation` is "v"
        and "bottom" when `orientation` is "h".

        The 'yanchor' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['top', 'middle', 'bottom']

        Returns
        -------
        Any
        """
        return self['yanchor']

    @yanchor.setter
    def yanchor(self, val):
        self['yanchor'] = val

    # ypad
    # ----
    @property
    def ypad(self):
        """
        Sets the amount of padding (in px) along the y direction.

        The 'ypad' property is a number and may be specified as:
          - An int or float in the interval [0, inf]

        Returns
        -------
        int|float
        """
        return self['ypad']

    @ypad.setter
    def ypad(self, val):
        self['ypad'] = val

    # yref
    # ----
    @property
    def yref(self):
        """
        Sets the container `y` refers to. "container" spans the entire
        `height` of the plot. "paper" refers to the height of the
        plotting area only.

        The 'yref' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['container', 'paper']

        Returns
        -------
        Any
        """
        return self['yref']

    @yref.setter
    def yref(self, val):
        self['yref'] = val

    # Self properties description
    # ---------------------------
    @property
    def _prop_descriptions(self):
        return """\
        bgcolor
            Sets the color of padded area.
        bordercolor
            Sets the axis line color.
        borderwidth
            Sets the width (in px) or the border enclosing this
            color bar.
        dtick
            Sets the step in-between ticks on this axis. Use with
            `tick0`. Must be a positive number, or special strings
            available to "log" and "date" axes. If the axis `type`
            is "log", then ticks are set every 10^(n*dtick) where n
            is the tick number. For example, to set a tick mark at
            1, 10, 100, 1000, ... set dtick to 1. To set tick marks
            at 1, 100, 10000, ... set dtick to 2. To set tick marks
            at 1, 5, 25, 125, 625, 3125, ... set dtick to
            log_10(5), or 0.69897000433. "log" has several special
            values; "L<f>", where `f` is a positive number, gives
            ticks linearly spaced in value (but not position). For
            example `tick0` = 0.1, `dtick` = "L0.5" will put ticks
            at 0.1, 0.6, 1.1, 1.6 etc. To show powers of 10 plus
            small digits between, use "D1" (all digits) or "D2"
            (only 2 and 5). `tick0` is ignored for "D1" and "D2".
            If the axis `type` is "date", then you must convert the
            time to milliseconds. For example, to set the interval
            between ticks to one day, set `dtick` to 86400000.0.
            "date" also has special values "M<n>" gives ticks
            spaced by a number of months. `n` must be a positive
            integer. To set ticks on the 15th of every third month,
            set `tick0` to "2000-01-15" and `dtick` to "M3". To set
            ticks every 4 years, set `dtick` to "M48"
        exponentformat
            Determines a formatting rule for the tick exponents.
            For example, consider the number 1,000,000,000. If
            "none", it appears as 1,000,000,000. If "e", 1e+9. If
            "E", 1E+9. If "power", 1x10^9 (with 9 in a super
            script). If "SI", 1G. If "B", 1B.
        labelalias
            Replacement text for specific tick or hover labels. For
            example using {US: 'USA', CA: 'Canada'} changes US to
            USA and CA to Canada. The labels we would have shown
            must match the keys exactly, after adding any
            tickprefix or ticksuffix. For negative numbers the
            minus sign symbol used (U+2212) is wider than the
            regular ascii dash. That means you need to use −1
            instead of -1. labelalias can be used with any axis
            type, and both keys (if needed) and values (if desired)
            can include html-like tags or MathJax.
        len
            Sets the length of the color bar This measure excludes
            the padding of both ends. That is, the color bar length
            is this length minus the padding on both ends.
        lenmode
            Determines whether this color bar's length (i.e. the
            measure in the color variation direction) is set in
            units of plot "fraction" or in *pixels. Use `len` to
            set the value.
        minexponent
            Hide SI prefix for 10^n if |n| is below this number.
            This only has an effect when `tickformat` is "SI" or
            "B".
        nticks
            Specifies the maximum number of ticks for the
            particular axis. The actual number of ticks will be
            chosen automatically to be less than or equal to
            `nticks`. Has an effect only if `tickmode` is set to
            "auto".
        orientation
            Sets the orientation of the colorbar.
        outlinecolor
            Sets the axis line color.
        outlinewidth
            Sets the width (in px) of the axis line.
        separatethousands
            If "true", even 4-digit integers are separated
        showexponent
            If "all", all exponents are shown besides their
            significands. If "first", only the exponent of the
            first tick is shown. If "last", only the exponent of
            the last tick is shown. If "none", no exponents appear.
        showticklabels
            Determines whether or not the tick labels are drawn.
        showtickprefix
            If "all", all tick labels are displayed with a prefix.
            If "first", only the first tick is displayed with a
            prefix. If "last", only the last tick is displayed with
            a suffix. If "none", tick prefixes are hidden.
        showticksuffix
            Same as `showtickprefix` but for tick suffixes.
        thickness
            Sets the thickness of the color bar This measure
            excludes the size of the padding, ticks and labels.
        thicknessmode
            Determines whether this color bar's thickness (i.e. the
            measure in the constant color direction) is set in
            units of plot "fraction" or in "pixels". Use
            `thickness` to set the value.
        tick0
            Sets the placement of the first tick on this axis. Use
            with `dtick`. If the axis `type` is "log", then you
            must take the log of your starting tick (e.g. to set
            the starting tick to 100, set the `tick0` to 2) except
            when `dtick`=*L<f>* (see `dtick` for more info). If the
            axis `type` is "date", it should be a date string, like
            date data. If the axis `type` is "category", it should
            be a number, using the scale where each category is
            assigned a serial number from zero in the order it
            appears.
        tickangle
            Sets the angle of the tick labels with respect to the
            horizontal. For example, a `tickangle` of -90 draws the
            tick labels vertically.
        tickcolor
            Sets the tick color.
        tickfont
            Sets the color bar's tick label font
        tickformat
            Sets the tick label formatting rule using d3 formatting
            mini-languages which are very similar to those in
            Python. For numbers, see:
            https://github.com/d3/d3-format/tree/v1.4.5#d3-format.
            And for dates see: https://github.com/d3/d3-time-
            format/tree/v2.2.3#locale_format. We add two items to
            d3's date formatter: "%h" for half of the year as a
            decimal number as well as "%{n}f" for fractional
            seconds with n digits. For example, *2016-10-13
            09:15:23.456* with tickformat "%H~%M~%S.%2f" would
            display "09~15~23.46"
        tickformatstops
            A tuple of :class:`plotly.graph_objects.scattersmith.ma
            rker.colorbar.Tickformatstop` instances or dicts with
            compatible properties
        tickformatstopdefaults
            When used in a template (as layout.template.data.scatte
            rsmith.marker.colorbar.tickformatstopdefaults), sets
            the default property values to use for elements of
            scattersmith.marker.colorbar.tickformatstops
        ticklabeloverflow
            Determines how we handle tick labels that would
            overflow either the graph div or the domain of the
            axis. The default value for inside tick labels is *hide
            past domain*. In other cases the default is *hide past
            div*.
        ticklabelposition
            Determines where tick labels are drawn relative to the
            ticks. Left and right options are used when
            `orientation` is "h", top and bottom when `orientation`
            is "v".
        ticklabelstep
            Sets the spacing between tick labels as compared to the
            spacing between ticks. A value of 1 (default) means
            each tick gets a label. A value of 2 means shows every
            2nd label. A larger value n means only every nth tick
            is labeled. `tick0` determines which labels are shown.
            Not implemented for axes with `type` "log" or
            "multicategory", or when `tickmode` is "array".
        ticklen
            Sets the tick length (in px).
        tickmode
            Sets the tick mode for this axis. If "auto", the number
            of ticks is set via `nticks`. If "linear", the
            placement of the ticks is determined by a starting
            position `tick0` and a tick step `dtick` ("linear" is
            the default value if `tick0` and `dtick` are provided).
            If "array", the placement of the ticks is set via
            `tickvals` and the tick text is `ticktext`. ("array" is
            the default value if `tickvals` is provided).
        tickprefix
            Sets a tick label prefix.
        ticks
            Determines whether ticks are drawn or not. If "", this
            axis' ticks are not drawn. If "outside" ("inside"),
            this axis' are drawn outside (inside) the axis lines.
        ticksuffix
            Sets a tick label suffix.
        ticktext
            Sets the text displayed at the ticks position via
            `tickvals`. Only has an effect if `tickmode` is set to
            "array". Used with `tickvals`.
        ticktextsrc
            Sets the source reference on Chart Studio Cloud for
            `ticktext`.
        tickvals
            Sets the values at which ticks on this axis appear.
            Only has an effect if `tickmode` is set to "array".
            Used with `ticktext`.
        tickvalssrc
            Sets the source reference on Chart Studio Cloud for
            `tickvals`.
        tickwidth
            Sets the tick width (in px).
        title
            :class:`plotly.graph_objects.scattersmith.marker.colorb
            ar.Title` instance or dict with compatible properties
        x
            Sets the x position with respect to `xref` of the color
            bar (in plot fraction). When `xref` is "paper",
            defaults to 1.02 when `orientation` is "v" and 0.5 when
            `orientation` is "h". When `xref` is "container",
            defaults to 1 when `orientation` is "v" and 0.5 when
            `orientation` is "h". Must be between 0 and 1 if `xref`
            is "container" and between "-2" and 3 if `xref` is
            "paper".
        xanchor
            Sets this color bar's horizontal position anchor. This
            anchor binds the `x` position to the "left", "center"
            or "right" of the color bar. Defaults to "left" when
            `orientation` is "v" and "center" when `orientation` is
            "h".
        xpad
            Sets the amount of padding (in px) along the x
            direction.
        xref
            Sets the container `x` refers to. "container" spans the
            entire `width` of the plot. "paper" refers to the width
            of the plotting area only.
        y
            Sets the y position with respect to `yref` of the color
            bar (in plot fraction). When `yref` is "paper",
            defaults to 0.5 when `orientation` is "v" and 1.02 when
            `orientation` is "h". When `yref` is "container",
            defaults to 0.5 when `orientation` is "v" and 1 when
            `orientation` is "h". Must be between 0 and 1 if `yref`
            is "container" and between "-2" and 3 if `yref` is
            "paper".
        yanchor
            Sets this color bar's vertical position anchor This
            anchor binds the `y` position to the "top", "middle" or
            "bottom" of the color bar. Defaults to "middle" when
            `orientation` is "v" and "bottom" when `orientation` is
            "h".
        ypad
            Sets the amount of padding (in px) along the y
            direction.
        yref
            Sets the container `y` refers to. "container" spans the
            entire `height` of the plot. "paper" refers to the
            height of the plotting area only.
        """
    def __init__(self,
            arg=None,
            bgcolor=None,
            bordercolor=None,
            borderwidth=None,
            dtick=None,
            exponentformat=None,
            labelalias=None,
            len=None,
            lenmode=None,
            minexponent=None,
            nticks=None,
            orientation=None,
            outlinecolor=None,
            outlinewidth=None,
            separatethousands=None,
            showexponent=None,
            showticklabels=None,
            showtickprefix=None,
            showticksuffix=None,
            thickness=None,
            thicknessmode=None,
            tick0=None,
            tickangle=None,
            tickcolor=None,
            tickfont=None,
            tickformat=None,
            tickformatstops=None,
            tickformatstopdefaults=None,
            ticklabeloverflow=None,
            ticklabelposition=None,
            ticklabelstep=None,
            ticklen=None,
            tickmode=None,
            tickprefix=None,
            ticks=None,
            ticksuffix=None,
            ticktext=None,
            ticktextsrc=None,
            tickvals=None,
            tickvalssrc=None,
            tickwidth=None,
            title=None,
            x=None,
            xanchor=None,
            xpad=None,
            xref=None,
            y=None,
            yanchor=None,
            ypad=None,
            yref=None,
            **kwargs
        ):
        """
        Construct a new ColorBar object

        Parameters
        ----------
        arg
            dict of properties compatible with this constructor or
            an instance of
            :class:`plotly.graph_objs.scattersmith.marker.ColorBar`
        bgcolor
            Sets the color of padded area.
        bordercolor
            Sets the axis line color.
        borderwidth
            Sets the width (in px) or the border enclosing this
            color bar.
        dtick
            Sets the step in-between ticks on this axis. Use with
            `tick0`. Must be a positive number, or special strings
            available to "log" and "date" axes. If the axis `type`
            is "log", then ticks are set every 10^(n*dtick) where n
            is the tick number. For example, to set a tick mark at
            1, 10, 100, 1000, ... set dtick to 1. To set tick marks
            at 1, 100, 10000, ... set dtick to 2. To set tick marks
            at 1, 5, 25, 125, 625, 3125, ... set dtick to
            log_10(5), or 0.69897000433. "log" has several special
            values; "L<f>", where `f` is a positive number, gives
            ticks linearly spaced in value (but not position). For
            example `tick0` = 0.1, `dtick` = "L0.5" will put ticks
            at 0.1, 0.6, 1.1, 1.6 etc. To show powers of 10 plus
            small digits between, use "D1" (all digits) or "D2"
            (only 2 and 5). `tick0` is ignored for "D1" and "D2".
            If the axis `type` is "date", then you must convert the
            time to milliseconds. For example, to set the interval
            between ticks to one day, set `dtick` to 86400000.0.
            "date" also has special values "M<n>" gives ticks
            spaced by a number of months. `n` must be a positive
            integer. To set ticks on the 15th of every third month,
            set `tick0` to "2000-01-15" and `dtick` to "M3". To set
            ticks every 4 years, set `dtick` to "M48"
        exponentformat
            Determines a formatting rule for the tick exponents.
            For example, consider the number 1,000,000,000. If
            "none", it appears as 1,000,000,000. If "e", 1e+9. If
            "E", 1E+9. If "power", 1x10^9 (with 9 in a super
            script). If "SI", 1G. If "B", 1B.
        labelalias
            Replacement text for specific tick or hover labels. For
            example using {US: 'USA', CA: 'Canada'} changes US to
            USA and CA to Canada. The labels we would have shown
            must match the keys exactly, after adding any
            tickprefix or ticksuffix. For negative numbers the
            minus sign symbol used (U+2212) is wider than the
            regular ascii dash. That means you need to use −1
            instead of -1. labelalias can be used with any axis
            type, and both keys (if needed) and values (if desired)
            can include html-like tags or MathJax.
        len
            Sets the length of the color bar This measure excludes
            the padding of both ends. That is, the color bar length
            is this length minus the padding on both ends.
        lenmode
            Determines whether this color bar's length (i.e. the
            measure in the color variation direction) is set in
            units of plot "fraction" or in *pixels. Use `len` to
            set the value.
        minexponent
            Hide SI prefix for 10^n if |n| is below this number.
            This only has an effect when `tickformat` is "SI" or
            "B".
        nticks
            Specifies the maximum number of ticks for the
            particular axis. The actual number of ticks will be
            chosen automatically to be less than or equal to
            `nticks`. Has an effect only if `tickmode` is set to
            "auto".
        orientation
            Sets the orientation of the colorbar.
        outlinecolor
            Sets the axis line color.
        outlinewidth
            Sets the width (in px) of the axis line.
        separatethousands
            If "true", even 4-digit integers are separated
        showexponent
            If "all", all exponents are shown besides their
            significands. If "first", only the exponent of the
            first tick is shown. If "last", only the exponent of
            the last tick is shown. If "none", no exponents appear.
        showticklabels
            Determines whether or not the tick labels are drawn.
        showtickprefix
            If "all", all tick labels are displayed with a prefix.
            If "first", only the first tick is displayed with a
            prefix. If "last", only the last tick is displayed with
            a suffix. If "none", tick prefixes are hidden.
        showticksuffix
            Same as `showtickprefix` but for tick suffixes.
        thickness
            Sets the thickness of the color bar This measure
            excludes the size of the padding, ticks and labels.
        thicknessmode
            Determines whether this color bar's thickness (i.e. the
            measure in the constant color direction) is set in
            units of plot "fraction" or in "pixels". Use
            `thickness` to set the value.
        tick0
            Sets the placement of the first tick on this axis. Use
            with `dtick`. If the axis `type` is "log", then you
            must take the log of your starting tick (e.g. to set
            the starting tick to 100, set the `tick0` to 2) except
            when `dtick`=*L<f>* (see `dtick` for more info). If the
            axis `type` is "date", it should be a date string, like
            date data. If the axis `type` is "category", it should
            be a number, using the scale where each category is
            assigned a serial number from zero in the order it
            appears.
        tickangle
            Sets the angle of the tick labels with respect to the
            horizontal. For example, a `tickangle` of -90 draws the
            tick labels vertically.
        tickcolor
            Sets the tick color.
        tickfont
            Sets the color bar's tick label font
        tickformat
            Sets the tick label formatting rule using d3 formatting
            mini-languages which are very similar to those in
            Python. For numbers, see:
            https://github.com/d3/d3-format/tree/v1.4.5#d3-format.
            And for dates see: https://github.com/d3/d3-time-
            format/tree/v2.2.3#locale_format. We add two items to
            d3's date formatter: "%h" for half of the year as a
            decimal number as well as "%{n}f" for fractional
            seconds with n digits. For example, *2016-10-13
            09:15:23.456* with tickformat "%H~%M~%S.%2f" would
            display "09~15~23.46"
        tickformatstops
            A tuple of :class:`plotly.graph_objects.scattersmith.ma
            rker.colorbar.Tickformatstop` instances or dicts with
            compatible properties
        tickformatstopdefaults
            When used in a template (as layout.template.data.scatte
            rsmith.marker.colorbar.tickformatstopdefaults), sets
            the default property values to use for elements of
            scattersmith.marker.colorbar.tickformatstops
        ticklabeloverflow
            Determines how we handle tick labels that would
            overflow either the graph div or the domain of the
            axis. The default value for inside tick labels is *hide
            past domain*. In other cases the default is *hide past
            div*.
        ticklabelposition
            Determines where tick labels are drawn relative to the
            ticks. Left and right options are used when
            `orientation` is "h", top and bottom when `orientation`
            is "v".
        ticklabelstep
            Sets the spacing between tick labels as compared to the
            spacing between ticks. A value of 1 (default) means
            each tick gets a label. A value of 2 means shows every
            2nd label. A larger value n means only every nth tick
            is labeled. `tick0` determines which labels are shown.
            Not implemented for axes with `type` "log" or
            "multicategory", or when `tickmode` is "array".
        ticklen
            Sets the tick length (in px).
        tickmode
            Sets the tick mode for this axis. If "auto", the number
            of ticks is set via `nticks`. If "linear", the
            placement of the ticks is determined by a starting
            position `tick0` and a tick step `dtick` ("linear" is
            the default value if `tick0` and `dtick` are provided).
            If "array", the placement of the ticks is set via
            `tickvals` and the tick text is `ticktext`. ("array" is
            the default value if `tickvals` is provided).
        tickprefix
            Sets a tick label prefix.
        ticks
            Determines whether ticks are drawn or not. If "", this
            axis' ticks are not drawn. If "outside" ("inside"),
            this axis' are drawn outside (inside) the axis lines.
        ticksuffix
            Sets a tick label suffix.
        ticktext
            Sets the text displayed at the ticks position via
            `tickvals`. Only has an effect if `tickmode` is set to
            "array". Used with `tickvals`.
        ticktextsrc
            Sets the source reference on Chart Studio Cloud for
            `ticktext`.
        tickvals
            Sets the values at which ticks on this axis appear.
            Only has an effect if `tickmode` is set to "array".
            Used with `ticktext`.
        tickvalssrc
            Sets the source reference on Chart Studio Cloud for
            `tickvals`.
        tickwidth
            Sets the tick width (in px).
        title
            :class:`plotly.graph_objects.scattersmith.marker.colorb
            ar.Title` instance or dict with compatible properties
        x
            Sets the x position with respect to `xref` of the color
            bar (in plot fraction). When `xref` is "paper",
            defaults to 1.02 when `orientation` is "v" and 0.5 when
            `orientation` is "h". When `xref` is "container",
            defaults to 1 when `orientation` is "v" and 0.5 when
            `orientation` is "h". Must be between 0 and 1 if `xref`
            is "container" and between "-2" and 3 if `xref` is
            "paper".
        xanchor
            Sets this color bar's horizontal position anchor. This
            anchor binds the `x` position to the "left", "center"
            or "right" of the color bar. Defaults to "left" when
            `orientation` is "v" and "center" when `orientation` is
            "h".
        xpad
            Sets the amount of padding (in px) along the x
            direction.
        xref
            Sets the container `x` refers to. "container" spans the
            entire `width` of the plot. "paper" refers to the width
            of the plotting area only.
        y
            Sets the y position with respect to `yref` of the color
            bar (in plot fraction). When `yref` is "paper",
            defaults to 0.5 when `orientation` is "v" and 1.02 when
            `orientation` is "h". When `yref` is "container",
            defaults to 0.5 when `orientation` is "v" and 1 when
            `orientation` is "h". Must be between 0 and 1 if `yref`
            is "container" and between "-2" and 3 if `yref` is
            "paper".
        yanchor
            Sets this color bar's vertical position anchor This
            anchor binds the `y` position to the "top", "middle" or
            "bottom" of the color bar. Defaults to "middle" when
            `orientation` is "v" and "bottom" when `orientation` is
            "h".
        ypad
            Sets the amount of padding (in px) along the y
            direction.
        yref
            Sets the container `y` refers to. "container" spans the
            entire `height` of the plot. "paper" refers to the
            height of the plotting area only.

        Returns
        -------
        ColorBar
        """
        super(ColorBar, self).__init__('colorbar')

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
The first argument to the plotly.graph_objs.scattersmith.marker.ColorBar
constructor must be a dict or
an instance of :class:`plotly.graph_objs.scattersmith.marker.ColorBar`""")

        # Handle skip_invalid
        # -------------------
        self._skip_invalid = kwargs.pop('skip_invalid', False)
        self._validate = kwargs.pop('_validate', True)
        

        # Populate data dict with properties
        # ----------------------------------
        self._init_provided('bgcolor', arg, bgcolor)
        self._init_provided('bordercolor', arg, bordercolor)
        self._init_provided('borderwidth', arg, borderwidth)
        self._init_provided('dtick', arg, dtick)
        self._init_provided('exponentformat', arg, exponentformat)
        self._init_provided('labelalias', arg, labelalias)
        self._init_provided('len', arg, len)
        self._init_provided('lenmode', arg, lenmode)
        self._init_provided('minexponent', arg, minexponent)
        self._init_provided('nticks', arg, nticks)
        self._init_provided('orientation', arg, orientation)
        self._init_provided('outlinecolor', arg, outlinecolor)
        self._init_provided('outlinewidth', arg, outlinewidth)
        self._init_provided('separatethousands', arg, separatethousands)
        self._init_provided('showexponent', arg, showexponent)
        self._init_provided('showticklabels', arg, showticklabels)
        self._init_provided('showtickprefix', arg, showtickprefix)
        self._init_provided('showticksuffix', arg, showticksuffix)
        self._init_provided('thickness', arg, thickness)
        self._init_provided('thicknessmode', arg, thicknessmode)
        self._init_provided('tick0', arg, tick0)
        self._init_provided('tickangle', arg, tickangle)
        self._init_provided('tickcolor', arg, tickcolor)
        self._init_provided('tickfont', arg, tickfont)
        self._init_provided('tickformat', arg, tickformat)
        self._init_provided('tickformatstops', arg, tickformatstops)
        self._init_provided('tickformatstopdefaults', arg, tickformatstopdefaults)
        self._init_provided('ticklabeloverflow', arg, ticklabeloverflow)
        self._init_provided('ticklabelposition', arg, ticklabelposition)
        self._init_provided('ticklabelstep', arg, ticklabelstep)
        self._init_provided('ticklen', arg, ticklen)
        self._init_provided('tickmode', arg, tickmode)
        self._init_provided('tickprefix', arg, tickprefix)
        self._init_provided('ticks', arg, ticks)
        self._init_provided('ticksuffix', arg, ticksuffix)
        self._init_provided('ticktext', arg, ticktext)
        self._init_provided('ticktextsrc', arg, ticktextsrc)
        self._init_provided('tickvals', arg, tickvals)
        self._init_provided('tickvalssrc', arg, tickvalssrc)
        self._init_provided('tickwidth', arg, tickwidth)
        self._init_provided('title', arg, title)
        self._init_provided('x', arg, x)
        self._init_provided('xanchor', arg, xanchor)
        self._init_provided('xpad', arg, xpad)
        self._init_provided('xref', arg, xref)
        self._init_provided('y', arg, y)
        self._init_provided('yanchor', arg, yanchor)
        self._init_provided('ypad', arg, ypad)
        self._init_provided('yref', arg, yref)

        # Process unknown kwargs
        # ----------------------
        self._process_kwargs(**dict(arg, **kwargs))

        # Reset skip_invalid
        # ------------------
        self._skip_invalid = False
