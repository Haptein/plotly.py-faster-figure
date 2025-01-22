

from plotly.basedatatypes import BaseTraceType as _BaseTraceType
import copy as _copy
from warnings import warn


class Densitymapbox(_BaseTraceType):

    # class properties
    # --------------------
    _parent_path_str = ''
    _path_str = 'densitymapbox'
    _valid_props = {"autocolorscale", "below", "coloraxis", "colorbar", "colorscale", "customdata", "customdatasrc", "hoverinfo", "hoverinfosrc", "hoverlabel", "hovertemplate", "hovertemplatesrc", "hovertext", "hovertextsrc", "ids", "idssrc", "lat", "latsrc", "legend", "legendgroup", "legendgrouptitle", "legendrank", "legendwidth", "lon", "lonsrc", "meta", "metasrc", "name", "opacity", "radius", "radiussrc", "reversescale", "showlegend", "showscale", "stream", "subplot", "text", "textsrc", "type", "uid", "uirevision", "visible", "z", "zauto", "zmax", "zmid", "zmin", "zsrc"}

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

    # below
    # -----
    @property
    def below(self):
        """
        Determines if the densitymapbox trace will be inserted before
        the layer with the specified ID. By default, densitymapbox
        traces are placed below the first layer of type symbol If set
        to '', the layer will be inserted above every existing layer.

        The 'below' property is a string and must be specified as:
          - A string
          - A number that will be converted to a string

        Returns
        -------
        str
        """
        return self['below']

    @below.setter
    def below(self, val):
        self['below'] = val

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
          - An instance of :class:`plotly.graph_objs.densitymapbox.ColorBar`
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
                    A tuple of :class:`plotly.graph_objects.density
                    mapbox.colorbar.Tickformatstop` instances or
                    dicts with compatible properties
                tickformatstopdefaults
                    When used in a template (as layout.template.dat
                    a.densitymapbox.colorbar.tickformatstopdefaults
                    ), sets the default property values to use for
                    elements of
                    densitymapbox.colorbar.tickformatstops
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
                    :class:`plotly.graph_objects.densitymapbox.colo
                    rbar.Title` instance or dict with compatible
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
        plotly.graph_objs.densitymapbox.ColorBar
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
        bounds of the colorscale in color space, use `zmin` and `zmax`.
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
          - Any combination of ['lon', 'lat', 'z', 'text', 'name'] joined with '+' characters
            (e.g. 'lon+lat')
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
          - An instance of :class:`plotly.graph_objs.densitymapbox.Hoverlabel`
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
        plotly.graph_objs.densitymapbox.Hoverlabel
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
        Sets hover text elements associated with each (lon,lat) pair If
        a single string, the same string appears over all the data
        points. If an array of string, the items are mapped in order to
        the this trace's (lon,lat) coordinates. To be seen, trace
        `hoverinfo` must contain a "text" flag.

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

    # lat
    # ---
    @property
    def lat(self):
        """
        Sets the latitude coordinates (in degrees North).

        The 'lat' property is an array that may be specified as a tuple,
        list, numpy array, or pandas Series

        Returns
        -------
        numpy.ndarray
        """
        return self['lat']

    @lat.setter
    def lat(self, val):
        self['lat'] = val

    # latsrc
    # ------
    @property
    def latsrc(self):
        """
        Sets the source reference on Chart Studio Cloud for `lat`.

        The 'latsrc' property must be specified as a string or
        as a plotly.grid_objs.Column object

        Returns
        -------
        str
        """
        return self['latsrc']

    @latsrc.setter
    def latsrc(self, val):
        self['latsrc'] = val

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
          - An instance of :class:`plotly.graph_objs.densitymapbox.Legendgrouptitle`
          - A dict of string/value properties that will be passed
            to the Legendgrouptitle constructor
    
            Supported dict properties:
                
                font
                    Sets this legend group's title font.
                text
                    Sets the title of the legend group.

        Returns
        -------
        plotly.graph_objs.densitymapbox.Legendgrouptitle
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

    # lon
    # ---
    @property
    def lon(self):
        """
        Sets the longitude coordinates (in degrees East).

        The 'lon' property is an array that may be specified as a tuple,
        list, numpy array, or pandas Series

        Returns
        -------
        numpy.ndarray
        """
        return self['lon']

    @lon.setter
    def lon(self, val):
        self['lon'] = val

    # lonsrc
    # ------
    @property
    def lonsrc(self):
        """
        Sets the source reference on Chart Studio Cloud for `lon`.

        The 'lonsrc' property must be specified as a string or
        as a plotly.grid_objs.Column object

        Returns
        -------
        str
        """
        return self['lonsrc']

    @lonsrc.setter
    def lonsrc(self, val):
        self['lonsrc'] = val

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
        Sets the opacity of the trace.

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

    # radius
    # ------
    @property
    def radius(self):
        """
        Sets the radius of influence of one `lon` / `lat` point in
        pixels. Increasing the value makes the densitymapbox trace
        smoother, but less detailed.

        The 'radius' property is a number and may be specified as:
          - An int or float in the interval [1, inf]
          - A tuple, list, or one-dimensional numpy array of the above

        Returns
        -------
        int|float|numpy.ndarray
        """
        return self['radius']

    @radius.setter
    def radius(self, val):
        self['radius'] = val

    # radiussrc
    # ---------
    @property
    def radiussrc(self):
        """
        Sets the source reference on Chart Studio Cloud for `radius`.

        The 'radiussrc' property must be specified as a string or
        as a plotly.grid_objs.Column object

        Returns
        -------
        str
        """
        return self['radiussrc']

    @radiussrc.setter
    def radiussrc(self, val):
        self['radiussrc'] = val

    # reversescale
    # ------------
    @property
    def reversescale(self):
        """
        Reverses the color mapping if true. If true, `zmin` will
        correspond to the last color in the array and `zmax` will
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

    # stream
    # ------
    @property
    def stream(self):
        """
        The 'stream' property is an instance of Stream
        that may be specified as:
          - An instance of :class:`plotly.graph_objs.densitymapbox.Stream`
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
        plotly.graph_objs.densitymapbox.Stream
        """
        return self['stream']

    @stream.setter
    def stream(self, val):
        self['stream'] = val

    # subplot
    # -------
    @property
    def subplot(self):
        """
        mapbox subplots and traces are deprecated! Please consider
        switching to `map` subplots and traces. Learn more at:
        https://plotly.com/python/maplibre-migration/ as well as
        https://plotly.com/javascript/maplibre-migration/ Sets a
        reference between this trace's data coordinates and a mapbox
        subplot. If "mapbox" (the default value), the data refer to
        `layout.mapbox`. If "mapbox2", the data refer to
        `layout.mapbox2`, and so on.

        The 'subplot' property is an identifier of a particular
        subplot, of type 'mapbox', that may be specified as the string 'mapbox'
        optionally followed by an integer >= 1
        (e.g. 'mapbox', 'mapbox1', 'mapbox2', 'mapbox3', etc.)

        Returns
        -------
        str
        """
        return self['subplot']

    @subplot.setter
    def subplot(self, val):
        self['subplot'] = val

    # text
    # ----
    @property
    def text(self):
        """
        Sets text elements associated with each (lon,lat) pair If a
        single string, the same string appears over all the data
        points. If an array of string, the items are mapped in order to
        the this trace's (lon,lat) coordinates. If trace `hoverinfo`
        contains a "text" flag and "hovertext" is not set, these
        elements will be seen in the hover labels.

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

    # z
    # -
    @property
    def z(self):
        """
        Sets the points' weight. For example, a value of 10 would be
        equivalent to having 10 points of weight 1 in the same spot

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

    # zauto
    # -----
    @property
    def zauto(self):
        """
        Determines whether or not the color domain is computed with
        respect to the input data (here in `z`) or the bounds set in
        `zmin` and `zmax` Defaults to `false` when `zmin` and `zmax`
        are set by the user.

        The 'zauto' property must be specified as a bool
        (either True, or False)

        Returns
        -------
        bool
        """
        return self['zauto']

    @zauto.setter
    def zauto(self, val):
        self['zauto'] = val

    # zmax
    # ----
    @property
    def zmax(self):
        """
        Sets the upper bound of the color domain. Value should have the
        same units as in `z` and if set, `zmin` must be set as well.

        The 'zmax' property is a number and may be specified as:
          - An int or float

        Returns
        -------
        int|float
        """
        return self['zmax']

    @zmax.setter
    def zmax(self, val):
        self['zmax'] = val

    # zmid
    # ----
    @property
    def zmid(self):
        """
        Sets the mid-point of the color domain by scaling `zmin` and/or
        `zmax` to be equidistant to this point. Value should have the
        same units as in `z`. Has no effect when `zauto` is `false`.

        The 'zmid' property is a number and may be specified as:
          - An int or float

        Returns
        -------
        int|float
        """
        return self['zmid']

    @zmid.setter
    def zmid(self, val):
        self['zmid'] = val

    # zmin
    # ----
    @property
    def zmin(self):
        """
        Sets the lower bound of the color domain. Value should have the
        same units as in `z` and if set, `zmax` must be set as well.

        The 'zmin' property is a number and may be specified as:
          - An int or float

        Returns
        -------
        int|float
        """
        return self['zmin']

    @zmin.setter
    def zmin(self, val):
        self['zmin'] = val

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
        below
            Determines if the densitymapbox trace will be inserted
            before the layer with the specified ID. By default,
            densitymapbox traces are placed below the first layer
            of type symbol If set to '', the layer will be inserted
            above every existing layer.
        coloraxis
            Sets a reference to a shared color axis. References to
            these shared color axes are "coloraxis", "coloraxis2",
            "coloraxis3", etc. Settings for these shared color axes
            are set in the layout, under `layout.coloraxis`,
            `layout.coloraxis2`, etc. Note that multiple color
            scales can be linked to the same color axis.
        colorbar
            :class:`plotly.graph_objects.densitymapbox.ColorBar`
            instance or dict with compatible properties
        colorscale
            Sets the colorscale. The colorscale must be an array
            containing arrays mapping a normalized value to an rgb,
            rgba, hex, hsl, hsv, or named color string. At minimum,
            a mapping for the lowest (0) and highest (1) values are
            required. For example, `[[0, 'rgb(0,0,255)'], [1,
            'rgb(255,0,0)']]`. To control the bounds of the
            colorscale in color space, use `zmin` and `zmax`.
            Alternatively, `colorscale` may be a palette name
            string of the following list: Blackbody,Bluered,Blues,C
            ividis,Earth,Electric,Greens,Greys,Hot,Jet,Picnic,Portl
            and,Rainbow,RdBu,Reds,Viridis,YlGnBu,YlOrRd.
        customdata
            Assigns extra data each datum. This may be useful when
            listening to hover, click and selection events. Note
            that, "scatter" traces also appends customdata items in
            the markers DOM elements
        customdatasrc
            Sets the source reference on Chart Studio Cloud for
            `customdata`.
        hoverinfo
            Determines which trace information appear on hover. If
            `none` or `skip` are set, no information is displayed
            upon hovering. But, if `none` is set, click and hover
            events are still fired.
        hoverinfosrc
            Sets the source reference on Chart Studio Cloud for
            `hoverinfo`.
        hoverlabel
            :class:`plotly.graph_objects.densitymapbox.Hoverlabel`
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
            Sets hover text elements associated with each (lon,lat)
            pair If a single string, the same string appears over
            all the data points. If an array of string, the items
            are mapped in order to the this trace's (lon,lat)
            coordinates. To be seen, trace `hoverinfo` must contain
            a "text" flag.
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
        lat
            Sets the latitude coordinates (in degrees North).
        latsrc
            Sets the source reference on Chart Studio Cloud for
            `lat`.
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
            :class:`plotly.graph_objects.densitymapbox.Legendgroupt
            itle` instance or dict with compatible properties
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
        lon
            Sets the longitude coordinates (in degrees East).
        lonsrc
            Sets the source reference on Chart Studio Cloud for
            `lon`.
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
            Sets the opacity of the trace.
        radius
            Sets the radius of influence of one `lon` / `lat` point
            in pixels. Increasing the value makes the densitymapbox
            trace smoother, but less detailed.
        radiussrc
            Sets the source reference on Chart Studio Cloud for
            `radius`.
        reversescale
            Reverses the color mapping if true. If true, `zmin`
            will correspond to the last color in the array and
            `zmax` will correspond to the first color.
        showlegend
            Determines whether or not an item corresponding to this
            trace is shown in the legend.
        showscale
            Determines whether or not a colorbar is displayed for
            this trace.
        stream
            :class:`plotly.graph_objects.densitymapbox.Stream`
            instance or dict with compatible properties
        subplot
            mapbox subplots and traces are deprecated! Please
            consider switching to `map` subplots and traces. Learn
            more at: https://plotly.com/python/maplibre-migration/
            as well as https://plotly.com/javascript/maplibre-
            migration/ Sets a reference between this trace's data
            coordinates and a mapbox subplot. If "mapbox" (the
            default value), the data refer to `layout.mapbox`. If
            "mapbox2", the data refer to `layout.mapbox2`, and so
            on.
        text
            Sets text elements associated with each (lon,lat) pair
            If a single string, the same string appears over all
            the data points. If an array of string, the items are
            mapped in order to the this trace's (lon,lat)
            coordinates. If trace `hoverinfo` contains a "text"
            flag and "hovertext" is not set, these elements will be
            seen in the hover labels.
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
        visible
            Determines whether or not this trace is visible. If
            "legendonly", the trace is not drawn, but can appear as
            a legend item (provided that the legend itself is
            visible).
        z
            Sets the points' weight. For example, a value of 10
            would be equivalent to having 10 points of weight 1 in
            the same spot
        zauto
            Determines whether or not the color domain is computed
            with respect to the input data (here in `z`) or the
            bounds set in `zmin` and `zmax` Defaults to `false`
            when `zmin` and `zmax` are set by the user.
        zmax
            Sets the upper bound of the color domain. Value should
            have the same units as in `z` and if set, `zmin` must
            be set as well.
        zmid
            Sets the mid-point of the color domain by scaling
            `zmin` and/or `zmax` to be equidistant to this point.
            Value should have the same units as in `z`. Has no
            effect when `zauto` is `false`.
        zmin
            Sets the lower bound of the color domain. Value should
            have the same units as in `z` and if set, `zmax` must
            be set as well.
        zsrc
            Sets the source reference on Chart Studio Cloud for
            `z`.
        """
    def __init__(self,
            arg=None,
            autocolorscale=None,
            below=None,
            coloraxis=None,
            colorbar=None,
            colorscale=None,
            customdata=None,
            customdatasrc=None,
            hoverinfo=None,
            hoverinfosrc=None,
            hoverlabel=None,
            hovertemplate=None,
            hovertemplatesrc=None,
            hovertext=None,
            hovertextsrc=None,
            ids=None,
            idssrc=None,
            lat=None,
            latsrc=None,
            legend=None,
            legendgroup=None,
            legendgrouptitle=None,
            legendrank=None,
            legendwidth=None,
            lon=None,
            lonsrc=None,
            meta=None,
            metasrc=None,
            name=None,
            opacity=None,
            radius=None,
            radiussrc=None,
            reversescale=None,
            showlegend=None,
            showscale=None,
            stream=None,
            subplot=None,
            text=None,
            textsrc=None,
            uid=None,
            uirevision=None,
            visible=None,
            z=None,
            zauto=None,
            zmax=None,
            zmid=None,
            zmin=None,
            zsrc=None,
            **kwargs
        ):
        """
        Construct a new Densitymapbox object

        "densitymapbox" trace is deprecated! Please consider switching
        to the "densitymap" trace type and `map` subplots. Learn more
        at: https://plotly.com/python/maplibre-migration/ as well as
        https://plotly.com/javascript/maplibre-migration/ Draws a
        bivariate kernel density estimation with a Gaussian kernel from
        `lon` and `lat` coordinates and optional `z` values using a
        colorscale.

        Parameters
        ----------
        arg
            dict of properties compatible with this constructor or
            an instance of :class:`plotly.graph_objs.Densitymapbox`
        autocolorscale
            Determines whether the colorscale is a default palette
            (`autocolorscale: true`) or the palette determined by
            `colorscale`. In case `colorscale` is unspecified or
            `autocolorscale` is true, the default palette will be
            chosen according to whether numbers in the `color`
            array are all positive, all negative or mixed.
        below
            Determines if the densitymapbox trace will be inserted
            before the layer with the specified ID. By default,
            densitymapbox traces are placed below the first layer
            of type symbol If set to '', the layer will be inserted
            above every existing layer.
        coloraxis
            Sets a reference to a shared color axis. References to
            these shared color axes are "coloraxis", "coloraxis2",
            "coloraxis3", etc. Settings for these shared color axes
            are set in the layout, under `layout.coloraxis`,
            `layout.coloraxis2`, etc. Note that multiple color
            scales can be linked to the same color axis.
        colorbar
            :class:`plotly.graph_objects.densitymapbox.ColorBar`
            instance or dict with compatible properties
        colorscale
            Sets the colorscale. The colorscale must be an array
            containing arrays mapping a normalized value to an rgb,
            rgba, hex, hsl, hsv, or named color string. At minimum,
            a mapping for the lowest (0) and highest (1) values are
            required. For example, `[[0, 'rgb(0,0,255)'], [1,
            'rgb(255,0,0)']]`. To control the bounds of the
            colorscale in color space, use `zmin` and `zmax`.
            Alternatively, `colorscale` may be a palette name
            string of the following list: Blackbody,Bluered,Blues,C
            ividis,Earth,Electric,Greens,Greys,Hot,Jet,Picnic,Portl
            and,Rainbow,RdBu,Reds,Viridis,YlGnBu,YlOrRd.
        customdata
            Assigns extra data each datum. This may be useful when
            listening to hover, click and selection events. Note
            that, "scatter" traces also appends customdata items in
            the markers DOM elements
        customdatasrc
            Sets the source reference on Chart Studio Cloud for
            `customdata`.
        hoverinfo
            Determines which trace information appear on hover. If
            `none` or `skip` are set, no information is displayed
            upon hovering. But, if `none` is set, click and hover
            events are still fired.
        hoverinfosrc
            Sets the source reference on Chart Studio Cloud for
            `hoverinfo`.
        hoverlabel
            :class:`plotly.graph_objects.densitymapbox.Hoverlabel`
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
            Sets hover text elements associated with each (lon,lat)
            pair If a single string, the same string appears over
            all the data points. If an array of string, the items
            are mapped in order to the this trace's (lon,lat)
            coordinates. To be seen, trace `hoverinfo` must contain
            a "text" flag.
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
        lat
            Sets the latitude coordinates (in degrees North).
        latsrc
            Sets the source reference on Chart Studio Cloud for
            `lat`.
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
            :class:`plotly.graph_objects.densitymapbox.Legendgroupt
            itle` instance or dict with compatible properties
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
        lon
            Sets the longitude coordinates (in degrees East).
        lonsrc
            Sets the source reference on Chart Studio Cloud for
            `lon`.
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
            Sets the opacity of the trace.
        radius
            Sets the radius of influence of one `lon` / `lat` point
            in pixels. Increasing the value makes the densitymapbox
            trace smoother, but less detailed.
        radiussrc
            Sets the source reference on Chart Studio Cloud for
            `radius`.
        reversescale
            Reverses the color mapping if true. If true, `zmin`
            will correspond to the last color in the array and
            `zmax` will correspond to the first color.
        showlegend
            Determines whether or not an item corresponding to this
            trace is shown in the legend.
        showscale
            Determines whether or not a colorbar is displayed for
            this trace.
        stream
            :class:`plotly.graph_objects.densitymapbox.Stream`
            instance or dict with compatible properties
        subplot
            mapbox subplots and traces are deprecated! Please
            consider switching to `map` subplots and traces. Learn
            more at: https://plotly.com/python/maplibre-migration/
            as well as https://plotly.com/javascript/maplibre-
            migration/ Sets a reference between this trace's data
            coordinates and a mapbox subplot. If "mapbox" (the
            default value), the data refer to `layout.mapbox`. If
            "mapbox2", the data refer to `layout.mapbox2`, and so
            on.
        text
            Sets text elements associated with each (lon,lat) pair
            If a single string, the same string appears over all
            the data points. If an array of string, the items are
            mapped in order to the this trace's (lon,lat)
            coordinates. If trace `hoverinfo` contains a "text"
            flag and "hovertext" is not set, these elements will be
            seen in the hover labels.
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
        visible
            Determines whether or not this trace is visible. If
            "legendonly", the trace is not drawn, but can appear as
            a legend item (provided that the legend itself is
            visible).
        z
            Sets the points' weight. For example, a value of 10
            would be equivalent to having 10 points of weight 1 in
            the same spot
        zauto
            Determines whether or not the color domain is computed
            with respect to the input data (here in `z`) or the
            bounds set in `zmin` and `zmax` Defaults to `false`
            when `zmin` and `zmax` are set by the user.
        zmax
            Sets the upper bound of the color domain. Value should
            have the same units as in `z` and if set, `zmin` must
            be set as well.
        zmid
            Sets the mid-point of the color domain by scaling
            `zmin` and/or `zmax` to be equidistant to this point.
            Value should have the same units as in `z`. Has no
            effect when `zauto` is `false`.
        zmin
            Sets the lower bound of the color domain. Value should
            have the same units as in `z` and if set, `zmax` must
            be set as well.
        zsrc
            Sets the source reference on Chart Studio Cloud for
            `z`.

        Returns
        -------
        Densitymapbox
        """
        super(Densitymapbox, self).__init__('densitymapbox')

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
The first argument to the plotly.graph_objs.Densitymapbox
constructor must be a dict or
an instance of :class:`plotly.graph_objs.Densitymapbox`""")

        # Handle skip_invalid
        # -------------------
        self._skip_invalid = kwargs.pop('skip_invalid', False)
        self._validate = kwargs.pop('_validate', True)
        

        # Populate data dict with properties
        # ----------------------------------
        self._init_provided('autocolorscale', arg, autocolorscale)
        self._init_provided('below', arg, below)
        self._init_provided('coloraxis', arg, coloraxis)
        self._init_provided('colorbar', arg, colorbar)
        self._init_provided('colorscale', arg, colorscale)
        self._init_provided('customdata', arg, customdata)
        self._init_provided('customdatasrc', arg, customdatasrc)
        self._init_provided('hoverinfo', arg, hoverinfo)
        self._init_provided('hoverinfosrc', arg, hoverinfosrc)
        self._init_provided('hoverlabel', arg, hoverlabel)
        self._init_provided('hovertemplate', arg, hovertemplate)
        self._init_provided('hovertemplatesrc', arg, hovertemplatesrc)
        self._init_provided('hovertext', arg, hovertext)
        self._init_provided('hovertextsrc', arg, hovertextsrc)
        self._init_provided('ids', arg, ids)
        self._init_provided('idssrc', arg, idssrc)
        self._init_provided('lat', arg, lat)
        self._init_provided('latsrc', arg, latsrc)
        self._init_provided('legend', arg, legend)
        self._init_provided('legendgroup', arg, legendgroup)
        self._init_provided('legendgrouptitle', arg, legendgrouptitle)
        self._init_provided('legendrank', arg, legendrank)
        self._init_provided('legendwidth', arg, legendwidth)
        self._init_provided('lon', arg, lon)
        self._init_provided('lonsrc', arg, lonsrc)
        self._init_provided('meta', arg, meta)
        self._init_provided('metasrc', arg, metasrc)
        self._init_provided('name', arg, name)
        self._init_provided('opacity', arg, opacity)
        self._init_provided('radius', arg, radius)
        self._init_provided('radiussrc', arg, radiussrc)
        self._init_provided('reversescale', arg, reversescale)
        self._init_provided('showlegend', arg, showlegend)
        self._init_provided('showscale', arg, showscale)
        self._init_provided('stream', arg, stream)
        self._init_provided('subplot', arg, subplot)
        self._init_provided('text', arg, text)
        self._init_provided('textsrc', arg, textsrc)
        self._init_provided('uid', arg, uid)
        self._init_provided('uirevision', arg, uirevision)
        self._init_provided('visible', arg, visible)
        self._init_provided('z', arg, z)
        self._init_provided('zauto', arg, zauto)
        self._init_provided('zmax', arg, zmax)
        self._init_provided('zmid', arg, zmid)
        self._init_provided('zmin', arg, zmin)
        self._init_provided('zsrc', arg, zsrc)

        # Read-only literals
        # ------------------

        self._props['type'] = 'densitymapbox'
        arg.pop('type', None)

        # Process unknown kwargs
        # ----------------------
        self._process_kwargs(**dict(arg, **kwargs))

        # Reset skip_invalid
        # ------------------
        self._skip_invalid = False

        warn(
            "*densitymapbox* is deprecated!"
            + " Use *densitymap* instead."
            + " Learn more at: https://plotly.com/python/mapbox-to-maplibre/",
            stacklevel=2,
            category=DeprecationWarning,
        )
