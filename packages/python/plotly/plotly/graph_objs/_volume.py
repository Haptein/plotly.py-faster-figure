

from plotly.basedatatypes import BaseTraceType as _BaseTraceType
import copy as _copy


class Volume(_BaseTraceType):

    # class properties
    # --------------------
    _parent_path_str = ''
    _path_str = 'volume'
    _valid_props = {"autocolorscale", "caps", "cauto", "cmax", "cmid", "cmin", "coloraxis", "colorbar", "colorscale", "contour", "customdata", "customdatasrc", "flatshading", "hoverinfo", "hoverinfosrc", "hoverlabel", "hovertemplate", "hovertemplatesrc", "hovertext", "hovertextsrc", "ids", "idssrc", "isomax", "isomin", "legend", "legendgroup", "legendgrouptitle", "legendrank", "legendwidth", "lighting", "lightposition", "meta", "metasrc", "name", "opacity", "opacityscale", "reversescale", "scene", "showlegend", "showscale", "slices", "spaceframe", "stream", "surface", "text", "textsrc", "type", "uid", "uirevision", "value", "valuehoverformat", "valuesrc", "visible", "x", "xhoverformat", "xsrc", "y", "yhoverformat", "ysrc", "z", "zhoverformat", "zsrc"}

    # autocolorscale
    # --------------
    @property
    def autocolorscale(self):
        """
        Determines whether the colorscale is a default palette
        (`autocolorscale: true`) or the palette determined by
        `colorscale`. In case `colorscale` is unspecified or
        `autocolorscale` is true, the default palette will be chosen
        according to whether numbers in the `color` array are all
        positive, all negative or mixed.

        The 'autocolorscale' property must be specified as a bool
        (either True, or False)

        Returns
        -------
        bool
        """
        return self['autocolorscale']

    @autocolorscale.setter
    def autocolorscale(self, val):
        self['autocolorscale'] = val

    # caps
    # ----
    @property
    def caps(self):
        """
        The 'caps' property is an instance of Caps
        that may be specified as:
          - An instance of :class:`plotly.graph_objs.volume.Caps`
          - A dict of string/value properties that will be passed
            to the Caps constructor
    
            Supported dict properties:
                
                x
                    :class:`plotly.graph_objects.volume.caps.X`
                    instance or dict with compatible properties
                y
                    :class:`plotly.graph_objects.volume.caps.Y`
                    instance or dict with compatible properties
                z
                    :class:`plotly.graph_objects.volume.caps.Z`
                    instance or dict with compatible properties

        Returns
        -------
        plotly.graph_objs.volume.Caps
        """
        return self['caps']

    @caps.setter
    def caps(self, val):
        self['caps'] = val

    # cauto
    # -----
    @property
    def cauto(self):
        """
        Determines whether or not the color domain is computed with
        respect to the input data (here `value`) or the bounds set in
        `cmin` and `cmax` Defaults to `false` when `cmin` and `cmax`
        are set by the user.

        The 'cauto' property must be specified as a bool
        (either True, or False)

        Returns
        -------
        bool
        """
        return self['cauto']

    @cauto.setter
    def cauto(self, val):
        self['cauto'] = val

    # cmax
    # ----
    @property
    def cmax(self):
        """
        Sets the upper bound of the color domain. Value should have the
        same units as `value` and if set, `cmin` must be set as well.

        The 'cmax' property is a number and may be specified as:
          - An int or float

        Returns
        -------
        int|float
        """
        return self['cmax']

    @cmax.setter
    def cmax(self, val):
        self['cmax'] = val

    # cmid
    # ----
    @property
    def cmid(self):
        """
        Sets the mid-point of the color domain by scaling `cmin` and/or
        `cmax` to be equidistant to this point. Value should have the
        same units as `value`. Has no effect when `cauto` is `false`.

        The 'cmid' property is a number and may be specified as:
          - An int or float

        Returns
        -------
        int|float
        """
        return self['cmid']

    @cmid.setter
    def cmid(self, val):
        self['cmid'] = val

    # cmin
    # ----
    @property
    def cmin(self):
        """
        Sets the lower bound of the color domain. Value should have the
        same units as `value` and if set, `cmax` must be set as well.

        The 'cmin' property is a number and may be specified as:
          - An int or float

        Returns
        -------
        int|float
        """
        return self['cmin']

    @cmin.setter
    def cmin(self, val):
        self['cmin'] = val

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
        return self['coloraxis']

    @coloraxis.setter
    def coloraxis(self, val):
        self['coloraxis'] = val

    # colorbar
    # --------
    @property
    def colorbar(self):
        """
        The 'colorbar' property is an instance of ColorBar
        that may be specified as:
          - An instance of :class:`plotly.graph_objs.volume.ColorBar`
          - A dict of string/value properties that will be passed
            to the ColorBar constructor
    
            Supported dict properties:
                
                bgcolor
                    Sets the color of padded area.
                bordercolor
                    Sets the axis line color.
                borderwidth
                    Sets the width (in px) or the border enclosing
                    this color bar.
                dtick
                    Sets the step in-between ticks on this axis.
                    Use with `tick0`. Must be a positive number, or
                    special strings available to "log" and "date"
                    axes. If the axis `type` is "log", then ticks
                    are set every 10^(n*dtick) where n is the tick
                    number. For example, to set a tick mark at 1,
                    10, 100, 1000, ... set dtick to 1. To set tick
                    marks at 1, 100, 10000, ... set dtick to 2. To
                    set tick marks at 1, 5, 25, 125, 625, 3125, ...
                    set dtick to log_10(5), or 0.69897000433. "log"
                    has several special values; "L<f>", where `f`
                    is a positive number, gives ticks linearly
                    spaced in value (but not position). For example
                    `tick0` = 0.1, `dtick` = "L0.5" will put ticks
                    at 0.1, 0.6, 1.1, 1.6 etc. To show powers of 10
                    plus small digits between, use "D1" (all
                    digits) or "D2" (only 2 and 5). `tick0` is
                    ignored for "D1" and "D2". If the axis `type`
                    is "date", then you must convert the time to
                    milliseconds. For example, to set the interval
                    between ticks to one day, set `dtick` to
                    86400000.0. "date" also has special values
                    "M<n>" gives ticks spaced by a number of
                    months. `n` must be a positive integer. To set
                    ticks on the 15th of every third month, set
                    `tick0` to "2000-01-15" and `dtick` to "M3". To
                    set ticks every 4 years, set `dtick` to "M48"
                exponentformat
                    Determines a formatting rule for the tick
                    exponents. For example, consider the number
                    1,000,000,000. If "none", it appears as
                    1,000,000,000. If "e", 1e+9. If "E", 1E+9. If
                    "power", 1x10^9 (with 9 in a super script). If
                    "SI", 1G. If "B", 1B.
                labelalias
                    Replacement text for specific tick or hover
                    labels. For example using {US: 'USA', CA:
                    'Canada'} changes US to USA and CA to Canada.
                    The labels we would have shown must match the
                    keys exactly, after adding any tickprefix or
                    ticksuffix. For negative numbers the minus sign
                    symbol used (U+2212) is wider than the regular
                    ascii dash. That means you need to use −1
                    instead of -1. labelalias can be used with any
                    axis type, and both keys (if needed) and values
                    (if desired) can include html-like tags or
                    MathJax.
                len
                    Sets the length of the color bar This measure
                    excludes the padding of both ends. That is, the
                    color bar length is this length minus the
                    padding on both ends.
                lenmode
                    Determines whether this color bar's length
                    (i.e. the measure in the color variation
                    direction) is set in units of plot "fraction"
                    or in *pixels. Use `len` to set the value.
                minexponent
                    Hide SI prefix for 10^n if |n| is below this
                    number. This only has an effect when
                    `tickformat` is "SI" or "B".
                nticks
                    Specifies the maximum number of ticks for the
                    particular axis. The actual number of ticks
                    will be chosen automatically to be less than or
                    equal to `nticks`. Has an effect only if
                    `tickmode` is set to "auto".
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
                    significands. If "first", only the exponent of
                    the first tick is shown. If "last", only the
                    exponent of the last tick is shown. If "none",
                    no exponents appear.
                showticklabels
                    Determines whether or not the tick labels are
                    drawn.
                showtickprefix
                    If "all", all tick labels are displayed with a
                    prefix. If "first", only the first tick is
                    displayed with a prefix. If "last", only the
                    last tick is displayed with a suffix. If
                    "none", tick prefixes are hidden.
                showticksuffix
                    Same as `showtickprefix` but for tick suffixes.
                thickness
                    Sets the thickness of the color bar This
                    measure excludes the size of the padding, ticks
                    and labels.
                thicknessmode
                    Determines whether this color bar's thickness
                    (i.e. the measure in the constant color
                    direction) is set in units of plot "fraction"
                    or in "pixels". Use `thickness` to set the
                    value.
                tick0
                    Sets the placement of the first tick on this
                    axis. Use with `dtick`. If the axis `type` is
                    "log", then you must take the log of your
                    starting tick (e.g. to set the starting tick to
                    100, set the `tick0` to 2) except when
                    `dtick`=*L<f>* (see `dtick` for more info). If
                    the axis `type` is "date", it should be a date
                    string, like date data. If the axis `type` is
                    "category", it should be a number, using the
                    scale where each category is assigned a serial
                    number from zero in the order it appears.
                tickangle
                    Sets the angle of the tick labels with respect
                    to the horizontal. For example, a `tickangle`
                    of -90 draws the tick labels vertically.
                tickcolor
                    Sets the tick color.
                tickfont
                    Sets the color bar's tick label font
                tickformat
                    Sets the tick label formatting rule using d3
                    formatting mini-languages which are very
                    similar to those in Python. For numbers, see: h
                    ttps://github.com/d3/d3-format/tree/v1.4.5#d3-
                    format. And for dates see:
                    https://github.com/d3/d3-time-
                    format/tree/v2.2.3#locale_format. We add two
                    items to d3's date formatter: "%h" for half of
                    the year as a decimal number as well as "%{n}f"
                    for fractional seconds with n digits. For
                    example, *2016-10-13 09:15:23.456* with
                    tickformat "%H~%M~%S.%2f" would display
                    "09~15~23.46"
                tickformatstops
                    A tuple of :class:`plotly.graph_objects.volume.
                    colorbar.Tickformatstop` instances or dicts
                    with compatible properties
                tickformatstopdefaults
                    When used in a template (as layout.template.dat
                    a.volume.colorbar.tickformatstopdefaults), sets
                    the default property values to use for elements
                    of volume.colorbar.tickformatstops
                ticklabeloverflow
                    Determines how we handle tick labels that would
                    overflow either the graph div or the domain of
                    the axis. The default value for inside tick
                    labels is *hide past domain*. In other cases
                    the default is *hide past div*.
                ticklabelposition
                    Determines where tick labels are drawn relative
                    to the ticks. Left and right options are used
                    when `orientation` is "h", top and bottom when
                    `orientation` is "v".
                ticklabelstep
                    Sets the spacing between tick labels as
                    compared to the spacing between ticks. A value
                    of 1 (default) means each tick gets a label. A
                    value of 2 means shows every 2nd label. A
                    larger value n means only every nth tick is
                    labeled. `tick0` determines which labels are
                    shown. Not implemented for axes with `type`
                    "log" or "multicategory", or when `tickmode` is
                    "array".
                ticklen
                    Sets the tick length (in px).
                tickmode
                    Sets the tick mode for this axis. If "auto",
                    the number of ticks is set via `nticks`. If
                    "linear", the placement of the ticks is
                    determined by a starting position `tick0` and a
                    tick step `dtick` ("linear" is the default
                    value if `tick0` and `dtick` are provided). If
                    "array", the placement of the ticks is set via
                    `tickvals` and the tick text is `ticktext`.
                    ("array" is the default value if `tickvals` is
                    provided).
                tickprefix
                    Sets a tick label prefix.
                ticks
                    Determines whether ticks are drawn or not. If
                    "", this axis' ticks are not drawn. If
                    "outside" ("inside"), this axis' are drawn
                    outside (inside) the axis lines.
                ticksuffix
                    Sets a tick label suffix.
                ticktext
                    Sets the text displayed at the ticks position
                    via `tickvals`. Only has an effect if
                    `tickmode` is set to "array". Used with
                    `tickvals`.
                ticktextsrc
                    Sets the source reference on Chart Studio Cloud
                    for `ticktext`.
                tickvals
                    Sets the values at which ticks on this axis
                    appear. Only has an effect if `tickmode` is set
                    to "array". Used with `ticktext`.
                tickvalssrc
                    Sets the source reference on Chart Studio Cloud
                    for `tickvals`.
                tickwidth
                    Sets the tick width (in px).
                title
                    :class:`plotly.graph_objects.volume.colorbar.Ti
                    tle` instance or dict with compatible
                    properties
                x
                    Sets the x position with respect to `xref` of
                    the color bar (in plot fraction). When `xref`
                    is "paper", defaults to 1.02 when `orientation`
                    is "v" and 0.5 when `orientation` is "h". When
                    `xref` is "container", defaults to 1 when
                    `orientation` is "v" and 0.5 when `orientation`
                    is "h". Must be between 0 and 1 if `xref` is
                    "container" and between "-2" and 3 if `xref` is
                    "paper".
                xanchor
                    Sets this color bar's horizontal position
                    anchor. This anchor binds the `x` position to
                    the "left", "center" or "right" of the color
                    bar. Defaults to "left" when `orientation` is
                    "v" and "center" when `orientation` is "h".
                xpad
                    Sets the amount of padding (in px) along the x
                    direction.
                xref
                    Sets the container `x` refers to. "container"
                    spans the entire `width` of the plot. "paper"
                    refers to the width of the plotting area only.
                y
                    Sets the y position with respect to `yref` of
                    the color bar (in plot fraction). When `yref`
                    is "paper", defaults to 0.5 when `orientation`
                    is "v" and 1.02 when `orientation` is "h". When
                    `yref` is "container", defaults to 0.5 when
                    `orientation` is "v" and 1 when `orientation`
                    is "h". Must be between 0 and 1 if `yref` is
                    "container" and between "-2" and 3 if `yref` is
                    "paper".
                yanchor
                    Sets this color bar's vertical position anchor
                    This anchor binds the `y` position to the
                    "top", "middle" or "bottom" of the color bar.
                    Defaults to "middle" when `orientation` is "v"
                    and "bottom" when `orientation` is "h".
                ypad
                    Sets the amount of padding (in px) along the y
                    direction.
                yref
                    Sets the container `y` refers to. "container"
                    spans the entire `height` of the plot. "paper"
                    refers to the height of the plotting area only.

        Returns
        -------
        plotly.graph_objs.volume.ColorBar
        """
        return self['colorbar']

    @colorbar.setter
    def colorbar(self, val):
        self['colorbar'] = val

    # colorscale
    # ----------
    @property
    def colorscale(self):
        """
        Sets the colorscale. The colorscale must be an array containing
        arrays mapping a normalized value to an rgb, rgba, hex, hsl,
        hsv, or named color string. At minimum, a mapping for the
        lowest (0) and highest (1) values are required. For example,
        `[[0, 'rgb(0,0,255)'], [1, 'rgb(255,0,0)']]`. To control the
        bounds of the colorscale in color space, use `cmin` and `cmax`.
        Alternatively, `colorscale` may be a palette name string of the
        following list: Blackbody,Bluered,Blues,Cividis,Earth,Electric,
        Greens,Greys,Hot,Jet,Picnic,Portland,Rainbow,RdBu,Reds,Viridis,
        YlGnBu,YlOrRd.

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
        return self['colorscale']

    @colorscale.setter
    def colorscale(self, val):
        self['colorscale'] = val

    # contour
    # -------
    @property
    def contour(self):
        """
        The 'contour' property is an instance of Contour
        that may be specified as:
          - An instance of :class:`plotly.graph_objs.volume.Contour`
          - A dict of string/value properties that will be passed
            to the Contour constructor
    
            Supported dict properties:
                
                color
                    Sets the color of the contour lines.
                show
                    Sets whether or not dynamic contours are shown
                    on hover
                width
                    Sets the width of the contour lines.

        Returns
        -------
        plotly.graph_objs.volume.Contour
        """
        return self['contour']

    @contour.setter
    def contour(self, val):
        self['contour'] = val

    # customdata
    # ----------
    @property
    def customdata(self):
        """
        Assigns extra data each datum. This may be useful when
        listening to hover, click and selection events. Note that,
        "scatter" traces also appends customdata items in the markers
        DOM elements

        The 'customdata' property is an array that may be specified as a tuple,
        list, numpy array, or pandas Series

        Returns
        -------
        numpy.ndarray
        """
        return self['customdata']

    @customdata.setter
    def customdata(self, val):
        self['customdata'] = val

    # customdatasrc
    # -------------
    @property
    def customdatasrc(self):
        """
        Sets the source reference on Chart Studio Cloud for
        `customdata`.

        The 'customdatasrc' property must be specified as a string or
        as a plotly.grid_objs.Column object

        Returns
        -------
        str
        """
        return self['customdatasrc']

    @customdatasrc.setter
    def customdatasrc(self, val):
        self['customdatasrc'] = val

    # flatshading
    # -----------
    @property
    def flatshading(self):
        """
        Determines whether or not normal smoothing is applied to the
        meshes, creating meshes with an angular, low-poly look via flat
        reflections.

        The 'flatshading' property must be specified as a bool
        (either True, or False)

        Returns
        -------
        bool
        """
        return self['flatshading']

    @flatshading.setter
    def flatshading(self, val):
        self['flatshading'] = val

    # hoverinfo
    # ---------
    @property
    def hoverinfo(self):
        """
        Determines which trace information appear on hover. If `none`
        or `skip` are set, no information is displayed upon hovering.
        But, if `none` is set, click and hover events are still fired.

        The 'hoverinfo' property is a flaglist and may be specified
        as a string containing:
          - Any combination of ['x', 'y', 'z', 'text', 'name'] joined with '+' characters
            (e.g. 'x+y')
            OR exactly one of ['all', 'none', 'skip'] (e.g. 'skip')
          - A list or array of the above

        Returns
        -------
        Any|numpy.ndarray
        """
        return self['hoverinfo']

    @hoverinfo.setter
    def hoverinfo(self, val):
        self['hoverinfo'] = val

    # hoverinfosrc
    # ------------
    @property
    def hoverinfosrc(self):
        """
        Sets the source reference on Chart Studio Cloud for
        `hoverinfo`.

        The 'hoverinfosrc' property must be specified as a string or
        as a plotly.grid_objs.Column object

        Returns
        -------
        str
        """
        return self['hoverinfosrc']

    @hoverinfosrc.setter
    def hoverinfosrc(self, val):
        self['hoverinfosrc'] = val

    # hoverlabel
    # ----------
    @property
    def hoverlabel(self):
        """
        The 'hoverlabel' property is an instance of Hoverlabel
        that may be specified as:
          - An instance of :class:`plotly.graph_objs.volume.Hoverlabel`
          - A dict of string/value properties that will be passed
            to the Hoverlabel constructor
    
            Supported dict properties:
                
                align
                    Sets the horizontal alignment of the text
                    content within hover label box. Has an effect
                    only if the hover label text spans more two or
                    more lines
                alignsrc
                    Sets the source reference on Chart Studio Cloud
                    for `align`.
                bgcolor
                    Sets the background color of the hover labels
                    for this trace
                bgcolorsrc
                    Sets the source reference on Chart Studio Cloud
                    for `bgcolor`.
                bordercolor
                    Sets the border color of the hover labels for
                    this trace.
                bordercolorsrc
                    Sets the source reference on Chart Studio Cloud
                    for `bordercolor`.
                font
                    Sets the font used in hover labels.
                namelength
                    Sets the default length (in number of
                    characters) of the trace name in the hover
                    labels for all traces. -1 shows the whole name
                    regardless of length. 0-3 shows the first 0-3
                    characters, and an integer >3 will show the
                    whole name if it is less than that many
                    characters, but if it is longer, will truncate
                    to `namelength - 3` characters and add an
                    ellipsis.
                namelengthsrc
                    Sets the source reference on Chart Studio Cloud
                    for `namelength`.

        Returns
        -------
        plotly.graph_objs.volume.Hoverlabel
        """
        return self['hoverlabel']

    @hoverlabel.setter
    def hoverlabel(self, val):
        self['hoverlabel'] = val

    # hovertemplate
    # -------------
    @property
    def hovertemplate(self):
        """
        Template string used for rendering the information that appear
        on hover box. Note that this will override `hoverinfo`.
        Variables are inserted using %{variable}, for example "y: %{y}"
        as well as %{xother}, {%_xother}, {%_xother_}, {%xother_}. When
        showing info for several points, "xother" will be added to
        those with different x positions from the first point. An
        underscore before or after "(x|y)other" will add a space on
        that side, only when this field is shown. Numbers are formatted
        using d3-format's syntax %{variable:d3-format}, for example
        "Price: %{y:$.2f}".
        https://github.com/d3/d3-format/tree/v1.4.5#d3-format for
        details on the formatting syntax. Dates are formatted using
        d3-time-format's syntax %{variable|d3-time-format}, for example
        "Day: %{2019-01-01|%A}". https://github.com/d3/d3-time-
        format/tree/v2.2.3#locale_format for details on the date
        formatting syntax. The variables available in `hovertemplate`
        are the ones emitted as event data described at this link
        https://plotly.com/javascript/plotlyjs-events/#event-data.
        Additionally, every attributes that can be specified per-point
        (the ones that are `arrayOk: true`) are available.  Anything
        contained in tag `<extra>` is displayed in the secondary box,
        for example "<extra>{fullData.name}</extra>". To hide the
        secondary box completely, use an empty tag `<extra></extra>`.

        The 'hovertemplate' property is a string and must be specified as:
          - A string
          - A number that will be converted to a string
          - A tuple, list, or one-dimensional numpy array of the above

        Returns
        -------
        str|numpy.ndarray
        """
        return self['hovertemplate']

    @hovertemplate.setter
    def hovertemplate(self, val):
        self['hovertemplate'] = val

    # hovertemplatesrc
    # ----------------
    @property
    def hovertemplatesrc(self):
        """
        Sets the source reference on Chart Studio Cloud for
        `hovertemplate`.

        The 'hovertemplatesrc' property must be specified as a string or
        as a plotly.grid_objs.Column object

        Returns
        -------
        str
        """
        return self['hovertemplatesrc']

    @hovertemplatesrc.setter
    def hovertemplatesrc(self, val):
        self['hovertemplatesrc'] = val

    # hovertext
    # ---------
    @property
    def hovertext(self):
        """
        Same as `text`.

        The 'hovertext' property is a string and must be specified as:
          - A string
          - A number that will be converted to a string
          - A tuple, list, or one-dimensional numpy array of the above

        Returns
        -------
        str|numpy.ndarray
        """
        return self['hovertext']

    @hovertext.setter
    def hovertext(self, val):
        self['hovertext'] = val

    # hovertextsrc
    # ------------
    @property
    def hovertextsrc(self):
        """
        Sets the source reference on Chart Studio Cloud for
        `hovertext`.

        The 'hovertextsrc' property must be specified as a string or
        as a plotly.grid_objs.Column object

        Returns
        -------
        str
        """
        return self['hovertextsrc']

    @hovertextsrc.setter
    def hovertextsrc(self, val):
        self['hovertextsrc'] = val

    # ids
    # ---
    @property
    def ids(self):
        """
        Assigns id labels to each datum. These ids for object constancy
        of data points during animation. Should be an array of strings,
        not numbers or any other type.

        The 'ids' property is an array that may be specified as a tuple,
        list, numpy array, or pandas Series

        Returns
        -------
        numpy.ndarray
        """
        return self['ids']

    @ids.setter
    def ids(self, val):
        self['ids'] = val

    # idssrc
    # ------
    @property
    def idssrc(self):
        """
        Sets the source reference on Chart Studio Cloud for `ids`.

        The 'idssrc' property must be specified as a string or
        as a plotly.grid_objs.Column object

        Returns
        -------
        str
        """
        return self['idssrc']

    @idssrc.setter
    def idssrc(self, val):
        self['idssrc'] = val

    # isomax
    # ------
    @property
    def isomax(self):
        """
        Sets the maximum boundary for iso-surface plot.

        The 'isomax' property is a number and may be specified as:
          - An int or float

        Returns
        -------
        int|float
        """
        return self['isomax']

    @isomax.setter
    def isomax(self, val):
        self['isomax'] = val

    # isomin
    # ------
    @property
    def isomin(self):
        """
        Sets the minimum boundary for iso-surface plot.

        The 'isomin' property is a number and may be specified as:
          - An int or float

        Returns
        -------
        int|float
        """
        return self['isomin']

    @isomin.setter
    def isomin(self, val):
        self['isomin'] = val

    # legend
    # ------
    @property
    def legend(self):
        """
        Sets the reference to a legend to show this trace in.
        References to these legends are "legend", "legend2", "legend3",
        etc. Settings for these legends are set in the layout, under
        `layout.legend`, `layout.legend2`, etc.

        The 'legend' property is an identifier of a particular
        subplot, of type 'legend', that may be specified as the string 'legend'
        optionally followed by an integer >= 1
        (e.g. 'legend', 'legend1', 'legend2', 'legend3', etc.)

        Returns
        -------
        str
        """
        return self['legend']

    @legend.setter
    def legend(self, val):
        self['legend'] = val

    # legendgroup
    # -----------
    @property
    def legendgroup(self):
        """
        Sets the legend group for this trace. Traces and shapes part of
        the same legend group hide/show at the same time when toggling
        legend items.

        The 'legendgroup' property is a string and must be specified as:
          - A string
          - A number that will be converted to a string

        Returns
        -------
        str
        """
        return self['legendgroup']

    @legendgroup.setter
    def legendgroup(self, val):
        self['legendgroup'] = val

    # legendgrouptitle
    # ----------------
    @property
    def legendgrouptitle(self):
        """
        The 'legendgrouptitle' property is an instance of Legendgrouptitle
        that may be specified as:
          - An instance of :class:`plotly.graph_objs.volume.Legendgrouptitle`
          - A dict of string/value properties that will be passed
            to the Legendgrouptitle constructor
    
            Supported dict properties:
                
                font
                    Sets this legend group's title font.
                text
                    Sets the title of the legend group.

        Returns
        -------
        plotly.graph_objs.volume.Legendgrouptitle
        """
        return self['legendgrouptitle']

    @legendgrouptitle.setter
    def legendgrouptitle(self, val):
        self['legendgrouptitle'] = val

    # legendrank
    # ----------
    @property
    def legendrank(self):
        """
        Sets the legend rank for this trace. Items and groups with
        smaller ranks are presented on top/left side while with
        "reversed" `legend.traceorder` they are on bottom/right side.
        The default legendrank is 1000, so that you can use ranks less
        than 1000 to place certain items before all unranked items, and
        ranks greater than 1000 to go after all unranked items. When
        having unranked or equal rank items shapes would be displayed
        after traces i.e. according to their order in data and layout.

        The 'legendrank' property is a number and may be specified as:
          - An int or float

        Returns
        -------
        int|float
        """
        return self['legendrank']

    @legendrank.setter
    def legendrank(self, val):
        self['legendrank'] = val

    # legendwidth
    # -----------
    @property
    def legendwidth(self):
        """
        Sets the width (in px or fraction) of the legend for this
        trace.

        The 'legendwidth' property is a number and may be specified as:
          - An int or float in the interval [0, inf]

        Returns
        -------
        int|float
        """
        return self['legendwidth']

    @legendwidth.setter
    def legendwidth(self, val):
        self['legendwidth'] = val

    # lighting
    # --------
    @property
    def lighting(self):
        """
        The 'lighting' property is an instance of Lighting
        that may be specified as:
          - An instance of :class:`plotly.graph_objs.volume.Lighting`
          - A dict of string/value properties that will be passed
            to the Lighting constructor
    
            Supported dict properties:
                
                ambient
                    Ambient light increases overall color
                    visibility but can wash out the image.
                diffuse
                    Represents the extent that incident rays are
                    reflected in a range of angles.
                facenormalsepsilon
                    Epsilon for face normals calculation avoids
                    math issues arising from degenerate geometry.
                fresnel
                    Represents the reflectance as a dependency of
                    the viewing angle; e.g. paper is reflective
                    when viewing it from the edge of the paper
                    (almost 90 degrees), causing shine.
                roughness
                    Alters specular reflection; the rougher the
                    surface, the wider and less contrasty the
                    shine.
                specular
                    Represents the level that incident rays are
                    reflected in a single direction, causing shine.
                vertexnormalsepsilon
                    Epsilon for vertex normals calculation avoids
                    math issues arising from degenerate geometry.

        Returns
        -------
        plotly.graph_objs.volume.Lighting
        """
        return self['lighting']

    @lighting.setter
    def lighting(self, val):
        self['lighting'] = val

    # lightposition
    # -------------
    @property
    def lightposition(self):
        """
        The 'lightposition' property is an instance of Lightposition
        that may be specified as:
          - An instance of :class:`plotly.graph_objs.volume.Lightposition`
          - A dict of string/value properties that will be passed
            to the Lightposition constructor
    
            Supported dict properties:
                
                x
                    Numeric vector, representing the X coordinate
                    for each vertex.
                y
                    Numeric vector, representing the Y coordinate
                    for each vertex.
                z
                    Numeric vector, representing the Z coordinate
                    for each vertex.

        Returns
        -------
        plotly.graph_objs.volume.Lightposition
        """
        return self['lightposition']

    @lightposition.setter
    def lightposition(self, val):
        self['lightposition'] = val

    # meta
    # ----
    @property
    def meta(self):
        """
        Assigns extra meta information associated with this trace that
        can be used in various text attributes. Attributes such as
        trace `name`, graph, axis and colorbar `title.text`, annotation
        `text` `rangeselector`, `updatemenues` and `sliders` `label`
        text all support `meta`. To access the trace `meta` values in
        an attribute in the same trace, simply use `%{meta[i]}` where
        `i` is the index or key of the `meta` item in question. To
        access trace `meta` in layout attributes, use
        `%{data[n[.meta[i]}` where `i` is the index or key of the
        `meta` and `n` is the trace index.

        The 'meta' property accepts values of any type

        Returns
        -------
        Any|numpy.ndarray
        """
        return self['meta']

    @meta.setter
    def meta(self, val):
        self['meta'] = val

    # metasrc
    # -------
    @property
    def metasrc(self):
        """
        Sets the source reference on Chart Studio Cloud for `meta`.

        The 'metasrc' property must be specified as a string or
        as a plotly.grid_objs.Column object

        Returns
        -------
        str
        """
        return self['metasrc']

    @metasrc.setter
    def metasrc(self, val):
        self['metasrc'] = val

    # name
    # ----
    @property
    def name(self):
        """
        Sets the trace name. The trace name appears as the legend item
        and on hover.

        The 'name' property is a string and must be specified as:
          - A string
          - A number that will be converted to a string

        Returns
        -------
        str
        """
        return self['name']

    @name.setter
    def name(self, val):
        self['name'] = val

    # opacity
    # -------
    @property
    def opacity(self):
        """
        Sets the opacity of the surface. Please note that in the case
        of using high `opacity` values for example a value greater than
        or equal to 0.5 on two surfaces (and 0.25 with four surfaces),
        an overlay of multiple transparent surfaces may not perfectly
        be sorted in depth by the webgl API. This behavior may be
        improved in the near future and is subject to change.

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

    # opacityscale
    # ------------
    @property
    def opacityscale(self):
        """
        Sets the opacityscale. The opacityscale must be an array
        containing arrays mapping a normalized value to an opacity
        value. At minimum, a mapping for the lowest (0) and highest (1)
        values are required. For example, `[[0, 1], [0.5, 0.2], [1,
        1]]` means that higher/lower values would have higher opacity
        values and those in the middle would be more transparent
        Alternatively, `opacityscale` may be a palette name string of
        the following list: 'min', 'max', 'extremes' and 'uniform'. The
        default is 'uniform'.

        The 'opacityscale' property accepts values of any type

        Returns
        -------
        Any
        """
        return self['opacityscale']

    @opacityscale.setter
    def opacityscale(self, val):
        self['opacityscale'] = val

    # reversescale
    # ------------
    @property
    def reversescale(self):
        """
        Reverses the color mapping if true. If true, `cmin` will
        correspond to the last color in the array and `cmax` will
        correspond to the first color.

        The 'reversescale' property must be specified as a bool
        (either True, or False)

        Returns
        -------
        bool
        """
        return self['reversescale']

    @reversescale.setter
    def reversescale(self, val):
        self['reversescale'] = val

    # scene
    # -----
    @property
    def scene(self):
        """
        Sets a reference between this trace's 3D coordinate system and
        a 3D scene. If "scene" (the default value), the (x,y,z)
        coordinates refer to `layout.scene`. If "scene2", the (x,y,z)
        coordinates refer to `layout.scene2`, and so on.

        The 'scene' property is an identifier of a particular
        subplot, of type 'scene', that may be specified as the string 'scene'
        optionally followed by an integer >= 1
        (e.g. 'scene', 'scene1', 'scene2', 'scene3', etc.)

        Returns
        -------
        str
        """
        return self['scene']

    @scene.setter
    def scene(self, val):
        self['scene'] = val

    # showlegend
    # ----------
    @property
    def showlegend(self):
        """
        Determines whether or not an item corresponding to this trace
        is shown in the legend.

        The 'showlegend' property must be specified as a bool
        (either True, or False)

        Returns
        -------
        bool
        """
        return self['showlegend']

    @showlegend.setter
    def showlegend(self, val):
        self['showlegend'] = val

    # showscale
    # ---------
    @property
    def showscale(self):
        """
        Determines whether or not a colorbar is displayed for this
        trace.

        The 'showscale' property must be specified as a bool
        (either True, or False)

        Returns
        -------
        bool
        """
        return self['showscale']

    @showscale.setter
    def showscale(self, val):
        self['showscale'] = val

    # slices
    # ------
    @property
    def slices(self):
        """
        The 'slices' property is an instance of Slices
        that may be specified as:
          - An instance of :class:`plotly.graph_objs.volume.Slices`
          - A dict of string/value properties that will be passed
            to the Slices constructor
    
            Supported dict properties:
                
                x
                    :class:`plotly.graph_objects.volume.slices.X`
                    instance or dict with compatible properties
                y
                    :class:`plotly.graph_objects.volume.slices.Y`
                    instance or dict with compatible properties
                z
                    :class:`plotly.graph_objects.volume.slices.Z`
                    instance or dict with compatible properties

        Returns
        -------
        plotly.graph_objs.volume.Slices
        """
        return self['slices']

    @slices.setter
    def slices(self, val):
        self['slices'] = val

    # spaceframe
    # ----------
    @property
    def spaceframe(self):
        """
        The 'spaceframe' property is an instance of Spaceframe
        that may be specified as:
          - An instance of :class:`plotly.graph_objs.volume.Spaceframe`
          - A dict of string/value properties that will be passed
            to the Spaceframe constructor
    
            Supported dict properties:
                
                fill
                    Sets the fill ratio of the `spaceframe`
                    elements. The default fill value is 1 meaning
                    that they are entirely shaded. Applying a
                    `fill` ratio less than one would allow the
                    creation of openings parallel to the edges.
                show
                    Displays/hides tetrahedron shapes between
                    minimum and maximum iso-values. Often useful
                    when either caps or surfaces are disabled or
                    filled with values less than 1.

        Returns
        -------
        plotly.graph_objs.volume.Spaceframe
        """
        return self['spaceframe']

    @spaceframe.setter
    def spaceframe(self, val):
        self['spaceframe'] = val

    # stream
    # ------
    @property
    def stream(self):
        """
        The 'stream' property is an instance of Stream
        that may be specified as:
          - An instance of :class:`plotly.graph_objs.volume.Stream`
          - A dict of string/value properties that will be passed
            to the Stream constructor
    
            Supported dict properties:
                
                maxpoints
                    Sets the maximum number of points to keep on
                    the plots from an incoming stream. If
                    `maxpoints` is set to 50, only the newest 50
                    points will be displayed on the plot.
                token
                    The stream id number links a data trace on a
                    plot with a stream. See https://chart-
                    studio.plotly.com/settings for more details.

        Returns
        -------
        plotly.graph_objs.volume.Stream
        """
        return self['stream']

    @stream.setter
    def stream(self, val):
        self['stream'] = val

    # surface
    # -------
    @property
    def surface(self):
        """
        The 'surface' property is an instance of Surface
        that may be specified as:
          - An instance of :class:`plotly.graph_objs.volume.Surface`
          - A dict of string/value properties that will be passed
            to the Surface constructor
    
            Supported dict properties:
                
                count
                    Sets the number of iso-surfaces between minimum
                    and maximum iso-values. By default this value
                    is 2 meaning that only minimum and maximum
                    surfaces would be drawn.
                fill
                    Sets the fill ratio of the iso-surface. The
                    default fill value of the surface is 1 meaning
                    that they are entirely shaded. On the other
                    hand Applying a `fill` ratio less than one
                    would allow the creation of openings parallel
                    to the edges.
                pattern
                    Sets the surface pattern of the iso-surface 3-D
                    sections. The default pattern of the surface is
                    `all` meaning that the rest of surface elements
                    would be shaded. The check options (either 1 or
                    2) could be used to draw half of the squares on
                    the surface. Using various combinations of
                    capital `A`, `B`, `C`, `D` and `E` may also be
                    used to reduce the number of triangles on the
                    iso-surfaces and creating other patterns of
                    interest.
                show
                    Hides/displays surfaces between minimum and
                    maximum iso-values.

        Returns
        -------
        plotly.graph_objs.volume.Surface
        """
        return self['surface']

    @surface.setter
    def surface(self, val):
        self['surface'] = val

    # text
    # ----
    @property
    def text(self):
        """
        Sets the text elements associated with the vertices. If trace
        `hoverinfo` contains a "text" flag and "hovertext" is not set,
        these elements will be seen in the hover labels.

        The 'text' property is a string and must be specified as:
          - A string
          - A number that will be converted to a string
          - A tuple, list, or one-dimensional numpy array of the above

        Returns
        -------
        str|numpy.ndarray
        """
        return self['text']

    @text.setter
    def text(self, val):
        self['text'] = val

    # textsrc
    # -------
    @property
    def textsrc(self):
        """
        Sets the source reference on Chart Studio Cloud for `text`.

        The 'textsrc' property must be specified as a string or
        as a plotly.grid_objs.Column object

        Returns
        -------
        str
        """
        return self['textsrc']

    @textsrc.setter
    def textsrc(self, val):
        self['textsrc'] = val

    # uid
    # ---
    @property
    def uid(self):
        """
        Assign an id to this trace, Use this to provide object
        constancy between traces during animations and transitions.

        The 'uid' property is a string and must be specified as:
          - A string
          - A number that will be converted to a string

        Returns
        -------
        str
        """
        return self['uid']

    @uid.setter
    def uid(self, val):
        self['uid'] = val

    # uirevision
    # ----------
    @property
    def uirevision(self):
        """
        Controls persistence of some user-driven changes to the trace:
        `constraintrange` in `parcoords` traces, as well as some
        `editable: true` modifications such as `name` and
        `colorbar.title`. Defaults to `layout.uirevision`. Note that
        other user-driven trace attribute changes are controlled by
        `layout` attributes: `trace.visible` is controlled by
        `layout.legend.uirevision`, `selectedpoints` is controlled by
        `layout.selectionrevision`, and `colorbar.(x|y)` (accessible
        with `config: {editable: true}`) is controlled by
        `layout.editrevision`. Trace changes are tracked by `uid`,
        which only falls back on trace index if no `uid` is provided.
        So if your app can add/remove traces before the end of the
        `data` array, such that the same trace has a different index,
        you can still preserve user-driven changes if you give each
        trace a `uid` that stays with it as it moves.

        The 'uirevision' property accepts values of any type

        Returns
        -------
        Any
        """
        return self['uirevision']

    @uirevision.setter
    def uirevision(self, val):
        self['uirevision'] = val

    # value
    # -----
    @property
    def value(self):
        """
        Sets the 4th dimension (value) of the vertices.

        The 'value' property is an array that may be specified as a tuple,
        list, numpy array, or pandas Series

        Returns
        -------
        numpy.ndarray
        """
        return self['value']

    @value.setter
    def value(self, val):
        self['value'] = val

    # valuehoverformat
    # ----------------
    @property
    def valuehoverformat(self):
        """
        Sets the hover text formatting rulefor `value`  using d3
        formatting mini-languages which are very similar to those in
        Python. For numbers, see:
        https://github.com/d3/d3-format/tree/v1.4.5#d3-format.By
        default the values are formatted using generic number format.

        The 'valuehoverformat' property is a string and must be specified as:
          - A string
          - A number that will be converted to a string

        Returns
        -------
        str
        """
        return self['valuehoverformat']

    @valuehoverformat.setter
    def valuehoverformat(self, val):
        self['valuehoverformat'] = val

    # valuesrc
    # --------
    @property
    def valuesrc(self):
        """
        Sets the source reference on Chart Studio Cloud for `value`.

        The 'valuesrc' property must be specified as a string or
        as a plotly.grid_objs.Column object

        Returns
        -------
        str
        """
        return self['valuesrc']

    @valuesrc.setter
    def valuesrc(self, val):
        self['valuesrc'] = val

    # visible
    # -------
    @property
    def visible(self):
        """
        Determines whether or not this trace is visible. If
        "legendonly", the trace is not drawn, but can appear as a
        legend item (provided that the legend itself is visible).

        The 'visible' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                [True, False, 'legendonly']

        Returns
        -------
        Any
        """
        return self['visible']

    @visible.setter
    def visible(self, val):
        self['visible'] = val

    # x
    # -
    @property
    def x(self):
        """
        Sets the X coordinates of the vertices on X axis.

        The 'x' property is an array that may be specified as a tuple,
        list, numpy array, or pandas Series

        Returns
        -------
        numpy.ndarray
        """
        return self['x']

    @x.setter
    def x(self, val):
        self['x'] = val

    # xhoverformat
    # ------------
    @property
    def xhoverformat(self):
        """
        Sets the hover text formatting rulefor `x`  using d3 formatting
        mini-languages which are very similar to those in Python. For
        numbers, see:
        https://github.com/d3/d3-format/tree/v1.4.5#d3-format. And for
        dates see: https://github.com/d3/d3-time-
        format/tree/v2.2.3#locale_format. We add two items to d3's date
        formatter: "%h" for half of the year as a decimal number as
        well as "%{n}f" for fractional seconds with n digits. For
        example, *2016-10-13 09:15:23.456* with tickformat
        "%H~%M~%S.%2f" would display *09~15~23.46*By default the values
        are formatted using `xaxis.hoverformat`.

        The 'xhoverformat' property is a string and must be specified as:
          - A string
          - A number that will be converted to a string

        Returns
        -------
        str
        """
        return self['xhoverformat']

    @xhoverformat.setter
    def xhoverformat(self, val):
        self['xhoverformat'] = val

    # xsrc
    # ----
    @property
    def xsrc(self):
        """
        Sets the source reference on Chart Studio Cloud for `x`.

        The 'xsrc' property must be specified as a string or
        as a plotly.grid_objs.Column object

        Returns
        -------
        str
        """
        return self['xsrc']

    @xsrc.setter
    def xsrc(self, val):
        self['xsrc'] = val

    # y
    # -
    @property
    def y(self):
        """
        Sets the Y coordinates of the vertices on Y axis.

        The 'y' property is an array that may be specified as a tuple,
        list, numpy array, or pandas Series

        Returns
        -------
        numpy.ndarray
        """
        return self['y']

    @y.setter
    def y(self, val):
        self['y'] = val

    # yhoverformat
    # ------------
    @property
    def yhoverformat(self):
        """
        Sets the hover text formatting rulefor `y`  using d3 formatting
        mini-languages which are very similar to those in Python. For
        numbers, see:
        https://github.com/d3/d3-format/tree/v1.4.5#d3-format. And for
        dates see: https://github.com/d3/d3-time-
        format/tree/v2.2.3#locale_format. We add two items to d3's date
        formatter: "%h" for half of the year as a decimal number as
        well as "%{n}f" for fractional seconds with n digits. For
        example, *2016-10-13 09:15:23.456* with tickformat
        "%H~%M~%S.%2f" would display *09~15~23.46*By default the values
        are formatted using `yaxis.hoverformat`.

        The 'yhoverformat' property is a string and must be specified as:
          - A string
          - A number that will be converted to a string

        Returns
        -------
        str
        """
        return self['yhoverformat']

    @yhoverformat.setter
    def yhoverformat(self, val):
        self['yhoverformat'] = val

    # ysrc
    # ----
    @property
    def ysrc(self):
        """
        Sets the source reference on Chart Studio Cloud for `y`.

        The 'ysrc' property must be specified as a string or
        as a plotly.grid_objs.Column object

        Returns
        -------
        str
        """
        return self['ysrc']

    @ysrc.setter
    def ysrc(self, val):
        self['ysrc'] = val

    # z
    # -
    @property
    def z(self):
        """
        Sets the Z coordinates of the vertices on Z axis.

        The 'z' property is an array that may be specified as a tuple,
        list, numpy array, or pandas Series

        Returns
        -------
        numpy.ndarray
        """
        return self['z']

    @z.setter
    def z(self, val):
        self['z'] = val

    # zhoverformat
    # ------------
    @property
    def zhoverformat(self):
        """
        Sets the hover text formatting rulefor `z`  using d3 formatting
        mini-languages which are very similar to those in Python. For
        numbers, see:
        https://github.com/d3/d3-format/tree/v1.4.5#d3-format. And for
        dates see: https://github.com/d3/d3-time-
        format/tree/v2.2.3#locale_format. We add two items to d3's date
        formatter: "%h" for half of the year as a decimal number as
        well as "%{n}f" for fractional seconds with n digits. For
        example, *2016-10-13 09:15:23.456* with tickformat
        "%H~%M~%S.%2f" would display *09~15~23.46*By default the values
        are formatted using `zaxis.hoverformat`.

        The 'zhoverformat' property is a string and must be specified as:
          - A string
          - A number that will be converted to a string

        Returns
        -------
        str
        """
        return self['zhoverformat']

    @zhoverformat.setter
    def zhoverformat(self, val):
        self['zhoverformat'] = val

    # zsrc
    # ----
    @property
    def zsrc(self):
        """
        Sets the source reference on Chart Studio Cloud for `z`.

        The 'zsrc' property must be specified as a string or
        as a plotly.grid_objs.Column object

        Returns
        -------
        str
        """
        return self['zsrc']

    @zsrc.setter
    def zsrc(self, val):
        self['zsrc'] = val

    # type
    # ----
    @property
    def type(self):
        return self._props['type']

    # Self properties description
    # ---------------------------
    @property
    def _prop_descriptions(self):
        return """\
        autocolorscale
            Determines whether the colorscale is a default palette
            (`autocolorscale: true`) or the palette determined by
            `colorscale`. In case `colorscale` is unspecified or
            `autocolorscale` is true, the default palette will be
            chosen according to whether numbers in the `color`
            array are all positive, all negative or mixed.
        caps
            :class:`plotly.graph_objects.volume.Caps` instance or
            dict with compatible properties
        cauto
            Determines whether or not the color domain is computed
            with respect to the input data (here `value`) or the
            bounds set in `cmin` and `cmax` Defaults to `false`
            when `cmin` and `cmax` are set by the user.
        cmax
            Sets the upper bound of the color domain. Value should
            have the same units as `value` and if set, `cmin` must
            be set as well.
        cmid
            Sets the mid-point of the color domain by scaling
            `cmin` and/or `cmax` to be equidistant to this point.
            Value should have the same units as `value`. Has no
            effect when `cauto` is `false`.
        cmin
            Sets the lower bound of the color domain. Value should
            have the same units as `value` and if set, `cmax` must
            be set as well.
        coloraxis
            Sets a reference to a shared color axis. References to
            these shared color axes are "coloraxis", "coloraxis2",
            "coloraxis3", etc. Settings for these shared color axes
            are set in the layout, under `layout.coloraxis`,
            `layout.coloraxis2`, etc. Note that multiple color
            scales can be linked to the same color axis.
        colorbar
            :class:`plotly.graph_objects.volume.ColorBar` instance
            or dict with compatible properties
        colorscale
            Sets the colorscale. The colorscale must be an array
            containing arrays mapping a normalized value to an rgb,
            rgba, hex, hsl, hsv, or named color string. At minimum,
            a mapping for the lowest (0) and highest (1) values are
            required. For example, `[[0, 'rgb(0,0,255)'], [1,
            'rgb(255,0,0)']]`. To control the bounds of the
            colorscale in color space, use `cmin` and `cmax`.
            Alternatively, `colorscale` may be a palette name
            string of the following list: Blackbody,Bluered,Blues,C
            ividis,Earth,Electric,Greens,Greys,Hot,Jet,Picnic,Portl
            and,Rainbow,RdBu,Reds,Viridis,YlGnBu,YlOrRd.
        contour
            :class:`plotly.graph_objects.volume.Contour` instance
            or dict with compatible properties
        customdata
            Assigns extra data each datum. This may be useful when
            listening to hover, click and selection events. Note
            that, "scatter" traces also appends customdata items in
            the markers DOM elements
        customdatasrc
            Sets the source reference on Chart Studio Cloud for
            `customdata`.
        flatshading
            Determines whether or not normal smoothing is applied
            to the meshes, creating meshes with an angular, low-
            poly look via flat reflections.
        hoverinfo
            Determines which trace information appear on hover. If
            `none` or `skip` are set, no information is displayed
            upon hovering. But, if `none` is set, click and hover
            events are still fired.
        hoverinfosrc
            Sets the source reference on Chart Studio Cloud for
            `hoverinfo`.
        hoverlabel
            :class:`plotly.graph_objects.volume.Hoverlabel`
            instance or dict with compatible properties
        hovertemplate
            Template string used for rendering the information that
            appear on hover box. Note that this will override
            `hoverinfo`. Variables are inserted using %{variable},
            for example "y: %{y}" as well as %{xother}, {%_xother},
            {%_xother_}, {%xother_}. When showing info for several
            points, "xother" will be added to those with different
            x positions from the first point. An underscore before
            or after "(x|y)other" will add a space on that side,
            only when this field is shown. Numbers are formatted
            using d3-format's syntax %{variable:d3-format}, for
            example "Price: %{y:$.2f}".
            https://github.com/d3/d3-format/tree/v1.4.5#d3-format
            for details on the formatting syntax. Dates are
            formatted using d3-time-format's syntax
            %{variable|d3-time-format}, for example "Day:
            %{2019-01-01|%A}". https://github.com/d3/d3-time-
            format/tree/v2.2.3#locale_format for details on the
            date formatting syntax. The variables available in
            `hovertemplate` are the ones emitted as event data
            described at this link
            https://plotly.com/javascript/plotlyjs-events/#event-
            data. Additionally, every attributes that can be
            specified per-point (the ones that are `arrayOk: true`)
            are available.  Anything contained in tag `<extra>` is
            displayed in the secondary box, for example
            "<extra>{fullData.name}</extra>". To hide the secondary
            box completely, use an empty tag `<extra></extra>`.
        hovertemplatesrc
            Sets the source reference on Chart Studio Cloud for
            `hovertemplate`.
        hovertext
            Same as `text`.
        hovertextsrc
            Sets the source reference on Chart Studio Cloud for
            `hovertext`.
        ids
            Assigns id labels to each datum. These ids for object
            constancy of data points during animation. Should be an
            array of strings, not numbers or any other type.
        idssrc
            Sets the source reference on Chart Studio Cloud for
            `ids`.
        isomax
            Sets the maximum boundary for iso-surface plot.
        isomin
            Sets the minimum boundary for iso-surface plot.
        legend
            Sets the reference to a legend to show this trace in.
            References to these legends are "legend", "legend2",
            "legend3", etc. Settings for these legends are set in
            the layout, under `layout.legend`, `layout.legend2`,
            etc.
        legendgroup
            Sets the legend group for this trace. Traces and shapes
            part of the same legend group hide/show at the same
            time when toggling legend items.
        legendgrouptitle
            :class:`plotly.graph_objects.volume.Legendgrouptitle`
            instance or dict with compatible properties
        legendrank
            Sets the legend rank for this trace. Items and groups
            with smaller ranks are presented on top/left side while
            with "reversed" `legend.traceorder` they are on
            bottom/right side. The default legendrank is 1000, so
            that you can use ranks less than 1000 to place certain
            items before all unranked items, and ranks greater than
            1000 to go after all unranked items. When having
            unranked or equal rank items shapes would be displayed
            after traces i.e. according to their order in data and
            layout.
        legendwidth
            Sets the width (in px or fraction) of the legend for
            this trace.
        lighting
            :class:`plotly.graph_objects.volume.Lighting` instance
            or dict with compatible properties
        lightposition
            :class:`plotly.graph_objects.volume.Lightposition`
            instance or dict with compatible properties
        meta
            Assigns extra meta information associated with this
            trace that can be used in various text attributes.
            Attributes such as trace `name`, graph, axis and
            colorbar `title.text`, annotation `text`
            `rangeselector`, `updatemenues` and `sliders` `label`
            text all support `meta`. To access the trace `meta`
            values in an attribute in the same trace, simply use
            `%{meta[i]}` where `i` is the index or key of the
            `meta` item in question. To access trace `meta` in
            layout attributes, use `%{data[n[.meta[i]}` where `i`
            is the index or key of the `meta` and `n` is the trace
            index.
        metasrc
            Sets the source reference on Chart Studio Cloud for
            `meta`.
        name
            Sets the trace name. The trace name appears as the
            legend item and on hover.
        opacity
            Sets the opacity of the surface. Please note that in
            the case of using high `opacity` values for example a
            value greater than or equal to 0.5 on two surfaces (and
            0.25 with four surfaces), an overlay of multiple
            transparent surfaces may not perfectly be sorted in
            depth by the webgl API. This behavior may be improved
            in the near future and is subject to change.
        opacityscale
            Sets the opacityscale. The opacityscale must be an
            array containing arrays mapping a normalized value to
            an opacity value. At minimum, a mapping for the lowest
            (0) and highest (1) values are required. For example,
            `[[0, 1], [0.5, 0.2], [1, 1]]` means that higher/lower
            values would have higher opacity values and those in
            the middle would be more transparent Alternatively,
            `opacityscale` may be a palette name string of the
            following list: 'min', 'max', 'extremes' and 'uniform'.
            The default is 'uniform'.
        reversescale
            Reverses the color mapping if true. If true, `cmin`
            will correspond to the last color in the array and
            `cmax` will correspond to the first color.
        scene
            Sets a reference between this trace's 3D coordinate
            system and a 3D scene. If "scene" (the default value),
            the (x,y,z) coordinates refer to `layout.scene`. If
            "scene2", the (x,y,z) coordinates refer to
            `layout.scene2`, and so on.
        showlegend
            Determines whether or not an item corresponding to this
            trace is shown in the legend.
        showscale
            Determines whether or not a colorbar is displayed for
            this trace.
        slices
            :class:`plotly.graph_objects.volume.Slices` instance or
            dict with compatible properties
        spaceframe
            :class:`plotly.graph_objects.volume.Spaceframe`
            instance or dict with compatible properties
        stream
            :class:`plotly.graph_objects.volume.Stream` instance or
            dict with compatible properties
        surface
            :class:`plotly.graph_objects.volume.Surface` instance
            or dict with compatible properties
        text
            Sets the text elements associated with the vertices. If
            trace `hoverinfo` contains a "text" flag and
            "hovertext" is not set, these elements will be seen in
            the hover labels.
        textsrc
            Sets the source reference on Chart Studio Cloud for
            `text`.
        uid
            Assign an id to this trace, Use this to provide object
            constancy between traces during animations and
            transitions.
        uirevision
            Controls persistence of some user-driven changes to the
            trace: `constraintrange` in `parcoords` traces, as well
            as some `editable: true` modifications such as `name`
            and `colorbar.title`. Defaults to `layout.uirevision`.
            Note that other user-driven trace attribute changes are
            controlled by `layout` attributes: `trace.visible` is
            controlled by `layout.legend.uirevision`,
            `selectedpoints` is controlled by
            `layout.selectionrevision`, and `colorbar.(x|y)`
            (accessible with `config: {editable: true}`) is
            controlled by `layout.editrevision`. Trace changes are
            tracked by `uid`, which only falls back on trace index
            if no `uid` is provided. So if your app can add/remove
            traces before the end of the `data` array, such that
            the same trace has a different index, you can still
            preserve user-driven changes if you give each trace a
            `uid` that stays with it as it moves.
        value
            Sets the 4th dimension (value) of the vertices.
        valuehoverformat
            Sets the hover text formatting rulefor `value`  using
            d3 formatting mini-languages which are very similar to
            those in Python. For numbers, see: https://github.com/d
            3/d3-format/tree/v1.4.5#d3-format.By default the values
            are formatted using generic number format.
        valuesrc
            Sets the source reference on Chart Studio Cloud for
            `value`.
        visible
            Determines whether or not this trace is visible. If
            "legendonly", the trace is not drawn, but can appear as
            a legend item (provided that the legend itself is
            visible).
        x
            Sets the X coordinates of the vertices on X axis.
        xhoverformat
            Sets the hover text formatting rulefor `x`  using d3
            formatting mini-languages which are very similar to
            those in Python. For numbers, see:
            https://github.com/d3/d3-format/tree/v1.4.5#d3-format.
            And for dates see: https://github.com/d3/d3-time-
            format/tree/v2.2.3#locale_format. We add two items to
            d3's date formatter: "%h" for half of the year as a
            decimal number as well as "%{n}f" for fractional
            seconds with n digits. For example, *2016-10-13
            09:15:23.456* with tickformat "%H~%M~%S.%2f" would
            display *09~15~23.46*By default the values are
            formatted using `xaxis.hoverformat`.
        xsrc
            Sets the source reference on Chart Studio Cloud for
            `x`.
        y
            Sets the Y coordinates of the vertices on Y axis.
        yhoverformat
            Sets the hover text formatting rulefor `y`  using d3
            formatting mini-languages which are very similar to
            those in Python. For numbers, see:
            https://github.com/d3/d3-format/tree/v1.4.5#d3-format.
            And for dates see: https://github.com/d3/d3-time-
            format/tree/v2.2.3#locale_format. We add two items to
            d3's date formatter: "%h" for half of the year as a
            decimal number as well as "%{n}f" for fractional
            seconds with n digits. For example, *2016-10-13
            09:15:23.456* with tickformat "%H~%M~%S.%2f" would
            display *09~15~23.46*By default the values are
            formatted using `yaxis.hoverformat`.
        ysrc
            Sets the source reference on Chart Studio Cloud for
            `y`.
        z
            Sets the Z coordinates of the vertices on Z axis.
        zhoverformat
            Sets the hover text formatting rulefor `z`  using d3
            formatting mini-languages which are very similar to
            those in Python. For numbers, see:
            https://github.com/d3/d3-format/tree/v1.4.5#d3-format.
            And for dates see: https://github.com/d3/d3-time-
            format/tree/v2.2.3#locale_format. We add two items to
            d3's date formatter: "%h" for half of the year as a
            decimal number as well as "%{n}f" for fractional
            seconds with n digits. For example, *2016-10-13
            09:15:23.456* with tickformat "%H~%M~%S.%2f" would
            display *09~15~23.46*By default the values are
            formatted using `zaxis.hoverformat`.
        zsrc
            Sets the source reference on Chart Studio Cloud for
            `z`.
        """
    def __init__(self,
            arg=None,
            autocolorscale=None,
            caps=None,
            cauto=None,
            cmax=None,
            cmid=None,
            cmin=None,
            coloraxis=None,
            colorbar=None,
            colorscale=None,
            contour=None,
            customdata=None,
            customdatasrc=None,
            flatshading=None,
            hoverinfo=None,
            hoverinfosrc=None,
            hoverlabel=None,
            hovertemplate=None,
            hovertemplatesrc=None,
            hovertext=None,
            hovertextsrc=None,
            ids=None,
            idssrc=None,
            isomax=None,
            isomin=None,
            legend=None,
            legendgroup=None,
            legendgrouptitle=None,
            legendrank=None,
            legendwidth=None,
            lighting=None,
            lightposition=None,
            meta=None,
            metasrc=None,
            name=None,
            opacity=None,
            opacityscale=None,
            reversescale=None,
            scene=None,
            showlegend=None,
            showscale=None,
            slices=None,
            spaceframe=None,
            stream=None,
            surface=None,
            text=None,
            textsrc=None,
            uid=None,
            uirevision=None,
            value=None,
            valuehoverformat=None,
            valuesrc=None,
            visible=None,
            x=None,
            xhoverformat=None,
            xsrc=None,
            y=None,
            yhoverformat=None,
            ysrc=None,
            z=None,
            zhoverformat=None,
            zsrc=None,
            **kwargs
        ):
        """
        Construct a new Volume object

        Draws volume trace between iso-min and iso-max values with
        coordinates given by four 1-dimensional arrays containing the
        `value`, `x`, `y` and `z` of every vertex of a uniform or non-
        uniform 3-D grid. Horizontal or vertical slices, caps as well
        as spaceframe between iso-min and iso-max values could also be
        drawn using this trace.

        Parameters
        ----------
        arg
            dict of properties compatible with this constructor or
            an instance of :class:`plotly.graph_objs.Volume`
        autocolorscale
            Determines whether the colorscale is a default palette
            (`autocolorscale: true`) or the palette determined by
            `colorscale`. In case `colorscale` is unspecified or
            `autocolorscale` is true, the default palette will be
            chosen according to whether numbers in the `color`
            array are all positive, all negative or mixed.
        caps
            :class:`plotly.graph_objects.volume.Caps` instance or
            dict with compatible properties
        cauto
            Determines whether or not the color domain is computed
            with respect to the input data (here `value`) or the
            bounds set in `cmin` and `cmax` Defaults to `false`
            when `cmin` and `cmax` are set by the user.
        cmax
            Sets the upper bound of the color domain. Value should
            have the same units as `value` and if set, `cmin` must
            be set as well.
        cmid
            Sets the mid-point of the color domain by scaling
            `cmin` and/or `cmax` to be equidistant to this point.
            Value should have the same units as `value`. Has no
            effect when `cauto` is `false`.
        cmin
            Sets the lower bound of the color domain. Value should
            have the same units as `value` and if set, `cmax` must
            be set as well.
        coloraxis
            Sets a reference to a shared color axis. References to
            these shared color axes are "coloraxis", "coloraxis2",
            "coloraxis3", etc. Settings for these shared color axes
            are set in the layout, under `layout.coloraxis`,
            `layout.coloraxis2`, etc. Note that multiple color
            scales can be linked to the same color axis.
        colorbar
            :class:`plotly.graph_objects.volume.ColorBar` instance
            or dict with compatible properties
        colorscale
            Sets the colorscale. The colorscale must be an array
            containing arrays mapping a normalized value to an rgb,
            rgba, hex, hsl, hsv, or named color string. At minimum,
            a mapping for the lowest (0) and highest (1) values are
            required. For example, `[[0, 'rgb(0,0,255)'], [1,
            'rgb(255,0,0)']]`. To control the bounds of the
            colorscale in color space, use `cmin` and `cmax`.
            Alternatively, `colorscale` may be a palette name
            string of the following list: Blackbody,Bluered,Blues,C
            ividis,Earth,Electric,Greens,Greys,Hot,Jet,Picnic,Portl
            and,Rainbow,RdBu,Reds,Viridis,YlGnBu,YlOrRd.
        contour
            :class:`plotly.graph_objects.volume.Contour` instance
            or dict with compatible properties
        customdata
            Assigns extra data each datum. This may be useful when
            listening to hover, click and selection events. Note
            that, "scatter" traces also appends customdata items in
            the markers DOM elements
        customdatasrc
            Sets the source reference on Chart Studio Cloud for
            `customdata`.
        flatshading
            Determines whether or not normal smoothing is applied
            to the meshes, creating meshes with an angular, low-
            poly look via flat reflections.
        hoverinfo
            Determines which trace information appear on hover. If
            `none` or `skip` are set, no information is displayed
            upon hovering. But, if `none` is set, click and hover
            events are still fired.
        hoverinfosrc
            Sets the source reference on Chart Studio Cloud for
            `hoverinfo`.
        hoverlabel
            :class:`plotly.graph_objects.volume.Hoverlabel`
            instance or dict with compatible properties
        hovertemplate
            Template string used for rendering the information that
            appear on hover box. Note that this will override
            `hoverinfo`. Variables are inserted using %{variable},
            for example "y: %{y}" as well as %{xother}, {%_xother},
            {%_xother_}, {%xother_}. When showing info for several
            points, "xother" will be added to those with different
            x positions from the first point. An underscore before
            or after "(x|y)other" will add a space on that side,
            only when this field is shown. Numbers are formatted
            using d3-format's syntax %{variable:d3-format}, for
            example "Price: %{y:$.2f}".
            https://github.com/d3/d3-format/tree/v1.4.5#d3-format
            for details on the formatting syntax. Dates are
            formatted using d3-time-format's syntax
            %{variable|d3-time-format}, for example "Day:
            %{2019-01-01|%A}". https://github.com/d3/d3-time-
            format/tree/v2.2.3#locale_format for details on the
            date formatting syntax. The variables available in
            `hovertemplate` are the ones emitted as event data
            described at this link
            https://plotly.com/javascript/plotlyjs-events/#event-
            data. Additionally, every attributes that can be
            specified per-point (the ones that are `arrayOk: true`)
            are available.  Anything contained in tag `<extra>` is
            displayed in the secondary box, for example
            "<extra>{fullData.name}</extra>". To hide the secondary
            box completely, use an empty tag `<extra></extra>`.
        hovertemplatesrc
            Sets the source reference on Chart Studio Cloud for
            `hovertemplate`.
        hovertext
            Same as `text`.
        hovertextsrc
            Sets the source reference on Chart Studio Cloud for
            `hovertext`.
        ids
            Assigns id labels to each datum. These ids for object
            constancy of data points during animation. Should be an
            array of strings, not numbers or any other type.
        idssrc
            Sets the source reference on Chart Studio Cloud for
            `ids`.
        isomax
            Sets the maximum boundary for iso-surface plot.
        isomin
            Sets the minimum boundary for iso-surface plot.
        legend
            Sets the reference to a legend to show this trace in.
            References to these legends are "legend", "legend2",
            "legend3", etc. Settings for these legends are set in
            the layout, under `layout.legend`, `layout.legend2`,
            etc.
        legendgroup
            Sets the legend group for this trace. Traces and shapes
            part of the same legend group hide/show at the same
            time when toggling legend items.
        legendgrouptitle
            :class:`plotly.graph_objects.volume.Legendgrouptitle`
            instance or dict with compatible properties
        legendrank
            Sets the legend rank for this trace. Items and groups
            with smaller ranks are presented on top/left side while
            with "reversed" `legend.traceorder` they are on
            bottom/right side. The default legendrank is 1000, so
            that you can use ranks less than 1000 to place certain
            items before all unranked items, and ranks greater than
            1000 to go after all unranked items. When having
            unranked or equal rank items shapes would be displayed
            after traces i.e. according to their order in data and
            layout.
        legendwidth
            Sets the width (in px or fraction) of the legend for
            this trace.
        lighting
            :class:`plotly.graph_objects.volume.Lighting` instance
            or dict with compatible properties
        lightposition
            :class:`plotly.graph_objects.volume.Lightposition`
            instance or dict with compatible properties
        meta
            Assigns extra meta information associated with this
            trace that can be used in various text attributes.
            Attributes such as trace `name`, graph, axis and
            colorbar `title.text`, annotation `text`
            `rangeselector`, `updatemenues` and `sliders` `label`
            text all support `meta`. To access the trace `meta`
            values in an attribute in the same trace, simply use
            `%{meta[i]}` where `i` is the index or key of the
            `meta` item in question. To access trace `meta` in
            layout attributes, use `%{data[n[.meta[i]}` where `i`
            is the index or key of the `meta` and `n` is the trace
            index.
        metasrc
            Sets the source reference on Chart Studio Cloud for
            `meta`.
        name
            Sets the trace name. The trace name appears as the
            legend item and on hover.
        opacity
            Sets the opacity of the surface. Please note that in
            the case of using high `opacity` values for example a
            value greater than or equal to 0.5 on two surfaces (and
            0.25 with four surfaces), an overlay of multiple
            transparent surfaces may not perfectly be sorted in
            depth by the webgl API. This behavior may be improved
            in the near future and is subject to change.
        opacityscale
            Sets the opacityscale. The opacityscale must be an
            array containing arrays mapping a normalized value to
            an opacity value. At minimum, a mapping for the lowest
            (0) and highest (1) values are required. For example,
            `[[0, 1], [0.5, 0.2], [1, 1]]` means that higher/lower
            values would have higher opacity values and those in
            the middle would be more transparent Alternatively,
            `opacityscale` may be a palette name string of the
            following list: 'min', 'max', 'extremes' and 'uniform'.
            The default is 'uniform'.
        reversescale
            Reverses the color mapping if true. If true, `cmin`
            will correspond to the last color in the array and
            `cmax` will correspond to the first color.
        scene
            Sets a reference between this trace's 3D coordinate
            system and a 3D scene. If "scene" (the default value),
            the (x,y,z) coordinates refer to `layout.scene`. If
            "scene2", the (x,y,z) coordinates refer to
            `layout.scene2`, and so on.
        showlegend
            Determines whether or not an item corresponding to this
            trace is shown in the legend.
        showscale
            Determines whether or not a colorbar is displayed for
            this trace.
        slices
            :class:`plotly.graph_objects.volume.Slices` instance or
            dict with compatible properties
        spaceframe
            :class:`plotly.graph_objects.volume.Spaceframe`
            instance or dict with compatible properties
        stream
            :class:`plotly.graph_objects.volume.Stream` instance or
            dict with compatible properties
        surface
            :class:`plotly.graph_objects.volume.Surface` instance
            or dict with compatible properties
        text
            Sets the text elements associated with the vertices. If
            trace `hoverinfo` contains a "text" flag and
            "hovertext" is not set, these elements will be seen in
            the hover labels.
        textsrc
            Sets the source reference on Chart Studio Cloud for
            `text`.
        uid
            Assign an id to this trace, Use this to provide object
            constancy between traces during animations and
            transitions.
        uirevision
            Controls persistence of some user-driven changes to the
            trace: `constraintrange` in `parcoords` traces, as well
            as some `editable: true` modifications such as `name`
            and `colorbar.title`. Defaults to `layout.uirevision`.
            Note that other user-driven trace attribute changes are
            controlled by `layout` attributes: `trace.visible` is
            controlled by `layout.legend.uirevision`,
            `selectedpoints` is controlled by
            `layout.selectionrevision`, and `colorbar.(x|y)`
            (accessible with `config: {editable: true}`) is
            controlled by `layout.editrevision`. Trace changes are
            tracked by `uid`, which only falls back on trace index
            if no `uid` is provided. So if your app can add/remove
            traces before the end of the `data` array, such that
            the same trace has a different index, you can still
            preserve user-driven changes if you give each trace a
            `uid` that stays with it as it moves.
        value
            Sets the 4th dimension (value) of the vertices.
        valuehoverformat
            Sets the hover text formatting rulefor `value`  using
            d3 formatting mini-languages which are very similar to
            those in Python. For numbers, see: https://github.com/d
            3/d3-format/tree/v1.4.5#d3-format.By default the values
            are formatted using generic number format.
        valuesrc
            Sets the source reference on Chart Studio Cloud for
            `value`.
        visible
            Determines whether or not this trace is visible. If
            "legendonly", the trace is not drawn, but can appear as
            a legend item (provided that the legend itself is
            visible).
        x
            Sets the X coordinates of the vertices on X axis.
        xhoverformat
            Sets the hover text formatting rulefor `x`  using d3
            formatting mini-languages which are very similar to
            those in Python. For numbers, see:
            https://github.com/d3/d3-format/tree/v1.4.5#d3-format.
            And for dates see: https://github.com/d3/d3-time-
            format/tree/v2.2.3#locale_format. We add two items to
            d3's date formatter: "%h" for half of the year as a
            decimal number as well as "%{n}f" for fractional
            seconds with n digits. For example, *2016-10-13
            09:15:23.456* with tickformat "%H~%M~%S.%2f" would
            display *09~15~23.46*By default the values are
            formatted using `xaxis.hoverformat`.
        xsrc
            Sets the source reference on Chart Studio Cloud for
            `x`.
        y
            Sets the Y coordinates of the vertices on Y axis.
        yhoverformat
            Sets the hover text formatting rulefor `y`  using d3
            formatting mini-languages which are very similar to
            those in Python. For numbers, see:
            https://github.com/d3/d3-format/tree/v1.4.5#d3-format.
            And for dates see: https://github.com/d3/d3-time-
            format/tree/v2.2.3#locale_format. We add two items to
            d3's date formatter: "%h" for half of the year as a
            decimal number as well as "%{n}f" for fractional
            seconds with n digits. For example, *2016-10-13
            09:15:23.456* with tickformat "%H~%M~%S.%2f" would
            display *09~15~23.46*By default the values are
            formatted using `yaxis.hoverformat`.
        ysrc
            Sets the source reference on Chart Studio Cloud for
            `y`.
        z
            Sets the Z coordinates of the vertices on Z axis.
        zhoverformat
            Sets the hover text formatting rulefor `z`  using d3
            formatting mini-languages which are very similar to
            those in Python. For numbers, see:
            https://github.com/d3/d3-format/tree/v1.4.5#d3-format.
            And for dates see: https://github.com/d3/d3-time-
            format/tree/v2.2.3#locale_format. We add two items to
            d3's date formatter: "%h" for half of the year as a
            decimal number as well as "%{n}f" for fractional
            seconds with n digits. For example, *2016-10-13
            09:15:23.456* with tickformat "%H~%M~%S.%2f" would
            display *09~15~23.46*By default the values are
            formatted using `zaxis.hoverformat`.
        zsrc
            Sets the source reference on Chart Studio Cloud for
            `z`.

        Returns
        -------
        Volume
        """
        super(Volume, self).__init__('volume')

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
The first argument to the plotly.graph_objs.Volume
constructor must be a dict or
an instance of :class:`plotly.graph_objs.Volume`""")

        # Handle skip_invalid
        # -------------------
        self._skip_invalid = kwargs.pop('skip_invalid', False)
        self._validate = kwargs.pop('_validate', True)
        

        # Populate data dict with properties
        # ----------------------------------
        self._init_provided('autocolorscale', arg, autocolorscale)
        self._init_provided('caps', arg, caps)
        self._init_provided('cauto', arg, cauto)
        self._init_provided('cmax', arg, cmax)
        self._init_provided('cmid', arg, cmid)
        self._init_provided('cmin', arg, cmin)
        self._init_provided('coloraxis', arg, coloraxis)
        self._init_provided('colorbar', arg, colorbar)
        self._init_provided('colorscale', arg, colorscale)
        self._init_provided('contour', arg, contour)
        self._init_provided('customdata', arg, customdata)
        self._init_provided('customdatasrc', arg, customdatasrc)
        self._init_provided('flatshading', arg, flatshading)
        self._init_provided('hoverinfo', arg, hoverinfo)
        self._init_provided('hoverinfosrc', arg, hoverinfosrc)
        self._init_provided('hoverlabel', arg, hoverlabel)
        self._init_provided('hovertemplate', arg, hovertemplate)
        self._init_provided('hovertemplatesrc', arg, hovertemplatesrc)
        self._init_provided('hovertext', arg, hovertext)
        self._init_provided('hovertextsrc', arg, hovertextsrc)
        self._init_provided('ids', arg, ids)
        self._init_provided('idssrc', arg, idssrc)
        self._init_provided('isomax', arg, isomax)
        self._init_provided('isomin', arg, isomin)
        self._init_provided('legend', arg, legend)
        self._init_provided('legendgroup', arg, legendgroup)
        self._init_provided('legendgrouptitle', arg, legendgrouptitle)
        self._init_provided('legendrank', arg, legendrank)
        self._init_provided('legendwidth', arg, legendwidth)
        self._init_provided('lighting', arg, lighting)
        self._init_provided('lightposition', arg, lightposition)
        self._init_provided('meta', arg, meta)
        self._init_provided('metasrc', arg, metasrc)
        self._init_provided('name', arg, name)
        self._init_provided('opacity', arg, opacity)
        self._init_provided('opacityscale', arg, opacityscale)
        self._init_provided('reversescale', arg, reversescale)
        self._init_provided('scene', arg, scene)
        self._init_provided('showlegend', arg, showlegend)
        self._init_provided('showscale', arg, showscale)
        self._init_provided('slices', arg, slices)
        self._init_provided('spaceframe', arg, spaceframe)
        self._init_provided('stream', arg, stream)
        self._init_provided('surface', arg, surface)
        self._init_provided('text', arg, text)
        self._init_provided('textsrc', arg, textsrc)
        self._init_provided('uid', arg, uid)
        self._init_provided('uirevision', arg, uirevision)
        self._init_provided('value', arg, value)
        self._init_provided('valuehoverformat', arg, valuehoverformat)
        self._init_provided('valuesrc', arg, valuesrc)
        self._init_provided('visible', arg, visible)
        self._init_provided('x', arg, x)
        self._init_provided('xhoverformat', arg, xhoverformat)
        self._init_provided('xsrc', arg, xsrc)
        self._init_provided('y', arg, y)
        self._init_provided('yhoverformat', arg, yhoverformat)
        self._init_provided('ysrc', arg, ysrc)
        self._init_provided('z', arg, z)
        self._init_provided('zhoverformat', arg, zhoverformat)
        self._init_provided('zsrc', arg, zsrc)

        # Read-only literals
        # ------------------

        self._props['type'] = 'volume'
        arg.pop('type', None)

        # Process unknown kwargs
        # ----------------------
        self._process_kwargs(**dict(arg, **kwargs))

        # Reset skip_invalid
        # ------------------
        self._skip_invalid = False
