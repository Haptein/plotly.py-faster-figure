from __future__ import annotations
from typing import Any
from numpy.typing import NDArray
from plotly.basedatatypes import BaseTraceType as _BaseTraceType
import copy as _copy


class Scatterpolar(_BaseTraceType):

    _parent_path_str = ""
    _path_str = "scatterpolar"
    _valid_props = {
        "cliponaxis",
        "connectgaps",
        "customdata",
        "customdatasrc",
        "dr",
        "dtheta",
        "fill",
        "fillcolor",
        "hoverinfo",
        "hoverinfosrc",
        "hoverlabel",
        "hoveron",
        "hovertemplate",
        "hovertemplatesrc",
        "hovertext",
        "hovertextsrc",
        "ids",
        "idssrc",
        "legend",
        "legendgroup",
        "legendgrouptitle",
        "legendrank",
        "legendwidth",
        "line",
        "marker",
        "meta",
        "metasrc",
        "mode",
        "name",
        "opacity",
        "r",
        "r0",
        "rsrc",
        "selected",
        "selectedpoints",
        "showlegend",
        "stream",
        "subplot",
        "text",
        "textfont",
        "textposition",
        "textpositionsrc",
        "textsrc",
        "texttemplate",
        "texttemplatesrc",
        "theta",
        "theta0",
        "thetasrc",
        "thetaunit",
        "type",
        "uid",
        "uirevision",
        "unselected",
        "visible",
    }

    @property
    def cliponaxis(self):
        """
        Determines whether or not markers and text nodes are clipped
        about the subplot axes. To show markers and text nodes above
        axis lines and tick labels, make sure to set `xaxis.layer` and
        `yaxis.layer` to *below traces*.

        The 'cliponaxis' property must be specified as a bool
        (either True, or False)

        Returns
        -------
        bool
        """
        return self["cliponaxis"]

    @cliponaxis.setter
    def cliponaxis(self, val):
        self["cliponaxis"] = val

    @property
    def connectgaps(self):
        """
        Determines whether or not gaps (i.e. {nan} or missing values)
        in the provided data arrays are connected.

        The 'connectgaps' property must be specified as a bool
        (either True, or False)

        Returns
        -------
        bool
        """
        return self["connectgaps"]

    @connectgaps.setter
    def connectgaps(self, val):
        self["connectgaps"] = val

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
        NDArray
        """
        return self["customdata"]

    @customdata.setter
    def customdata(self, val):
        self["customdata"] = val

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
        return self["customdatasrc"]

    @customdatasrc.setter
    def customdatasrc(self, val):
        self["customdatasrc"] = val

    @property
    def dr(self):
        """
        Sets the r coordinate step.

        The 'dr' property is a number and may be specified as:
          - An int or float

        Returns
        -------
        int|float
        """
        return self["dr"]

    @dr.setter
    def dr(self, val):
        self["dr"] = val

    @property
    def dtheta(self):
        """
        Sets the theta coordinate step. By default, the `dtheta` step
        equals the subplot's period divided by the length of the `r`
        coordinates.

        The 'dtheta' property is a number and may be specified as:
          - An int or float

        Returns
        -------
        int|float
        """
        return self["dtheta"]

    @dtheta.setter
    def dtheta(self, val):
        self["dtheta"] = val

    @property
    def fill(self):
        """
        Sets the area to fill with a solid color. Use with `fillcolor`
        if not "none". scatterpolar has a subset of the options
        available to scatter. "toself" connects the endpoints of the
        trace (or each segment of the trace if it has gaps) into a
        closed shape. "tonext" fills the space between two traces if
        one completely encloses the other (eg consecutive contour
        lines), and behaves like "toself" if there is no trace before
        it. "tonext" should not be used if one trace does not enclose
        the other.

        The 'fill' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['none', 'toself', 'tonext']

        Returns
        -------
        Any
        """
        return self["fill"]

    @fill.setter
    def fill(self, val):
        self["fill"] = val

    @property
    def fillcolor(self):
        """
        Sets the fill color. Defaults to a half-transparent variant of
        the line color, marker color, or marker line color, whichever
        is available.

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
        return self["fillcolor"]

    @fillcolor.setter
    def fillcolor(self, val):
        self["fillcolor"] = val

    @property
    def hoverinfo(self):
        """
        Determines which trace information appear on hover. If `none`
        or `skip` are set, no information is displayed upon hovering.
        But, if `none` is set, click and hover events are still fired.

        The 'hoverinfo' property is a flaglist and may be specified
        as a string containing:
          - Any combination of ['r', 'theta', 'text', 'name'] joined with '+' characters
            (e.g. 'r+theta')
            OR exactly one of ['all', 'none', 'skip'] (e.g. 'skip')
          - A list or array of the above

        Returns
        -------
        Any|NDArray
        """
        return self["hoverinfo"]

    @hoverinfo.setter
    def hoverinfo(self, val):
        self["hoverinfo"] = val

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
        return self["hoverinfosrc"]

    @hoverinfosrc.setter
    def hoverinfosrc(self, val):
        self["hoverinfosrc"] = val

    @property
    def hoverlabel(self):
        """
        The 'hoverlabel' property is an instance of Hoverlabel
        that may be specified as:
          - An instance of :class:`plotly.graph_objs.scatterpolar.Hoverlabel`
          - A dict of string/value properties that will be passed
            to the Hoverlabel constructor

        Returns
        -------
        plotly.graph_objs.scatterpolar.Hoverlabel
        """
        return self["hoverlabel"]

    @hoverlabel.setter
    def hoverlabel(self, val):
        self["hoverlabel"] = val

    @property
    def hoveron(self):
        """
        Do the hover effects highlight individual points (markers or
        line points) or do they highlight filled regions? If the fill
        is "toself" or "tonext" and there are no markers or text, then
        the default is "fills", otherwise it is "points".

        The 'hoveron' property is a flaglist and may be specified
        as a string containing:
          - Any combination of ['points', 'fills'] joined with '+' characters
            (e.g. 'points+fills')

        Returns
        -------
        Any
        """
        return self["hoveron"]

    @hoveron.setter
    def hoveron(self, val):
        self["hoveron"] = val

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
        str|NDArray
        """
        return self["hovertemplate"]

    @hovertemplate.setter
    def hovertemplate(self, val):
        self["hovertemplate"] = val

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
        return self["hovertemplatesrc"]

    @hovertemplatesrc.setter
    def hovertemplatesrc(self, val):
        self["hovertemplatesrc"] = val

    @property
    def hovertext(self):
        """
        Sets hover text elements associated with each (x,y) pair. If a
        single string, the same string appears over all the data
        points. If an array of string, the items are mapped in order to
        the this trace's (x,y) coordinates. To be seen, trace
        `hoverinfo` must contain a "text" flag.

        The 'hovertext' property is a string and must be specified as:
          - A string
          - A number that will be converted to a string
          - A tuple, list, or one-dimensional numpy array of the above

        Returns
        -------
        str|NDArray
        """
        return self["hovertext"]

    @hovertext.setter
    def hovertext(self, val):
        self["hovertext"] = val

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
        return self["hovertextsrc"]

    @hovertextsrc.setter
    def hovertextsrc(self, val):
        self["hovertextsrc"] = val

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
        NDArray
        """
        return self["ids"]

    @ids.setter
    def ids(self, val):
        self["ids"] = val

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
        return self["idssrc"]

    @idssrc.setter
    def idssrc(self, val):
        self["idssrc"] = val

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
        return self["legend"]

    @legend.setter
    def legend(self, val):
        self["legend"] = val

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
        return self["legendgroup"]

    @legendgroup.setter
    def legendgroup(self, val):
        self["legendgroup"] = val

    @property
    def legendgrouptitle(self):
        """
        The 'legendgrouptitle' property is an instance of Legendgrouptitle
        that may be specified as:
          - An instance of :class:`plotly.graph_objs.scatterpolar.Legendgrouptitle`
          - A dict of string/value properties that will be passed
            to the Legendgrouptitle constructor

        Returns
        -------
        plotly.graph_objs.scatterpolar.Legendgrouptitle
        """
        return self["legendgrouptitle"]

    @legendgrouptitle.setter
    def legendgrouptitle(self, val):
        self["legendgrouptitle"] = val

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
        return self["legendrank"]

    @legendrank.setter
    def legendrank(self, val):
        self["legendrank"] = val

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
        return self["legendwidth"]

    @legendwidth.setter
    def legendwidth(self, val):
        self["legendwidth"] = val

    @property
    def line(self):
        """
        The 'line' property is an instance of Line
        that may be specified as:
          - An instance of :class:`plotly.graph_objs.scatterpolar.Line`
          - A dict of string/value properties that will be passed
            to the Line constructor

        Returns
        -------
        plotly.graph_objs.scatterpolar.Line
        """
        return self["line"]

    @line.setter
    def line(self, val):
        self["line"] = val

    @property
    def marker(self):
        """
        The 'marker' property is an instance of Marker
        that may be specified as:
          - An instance of :class:`plotly.graph_objs.scatterpolar.Marker`
          - A dict of string/value properties that will be passed
            to the Marker constructor

        Returns
        -------
        plotly.graph_objs.scatterpolar.Marker
        """
        return self["marker"]

    @marker.setter
    def marker(self, val):
        self["marker"] = val

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
        Any|NDArray
        """
        return self["meta"]

    @meta.setter
    def meta(self, val):
        self["meta"] = val

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
        return self["metasrc"]

    @metasrc.setter
    def metasrc(self, val):
        self["metasrc"] = val

    @property
    def mode(self):
        """
        Determines the drawing mode for this scatter trace. If the
        provided `mode` includes "text" then the `text` elements appear
        at the coordinates. Otherwise, the `text` elements appear on
        hover. If there are less than 20 points and the trace is not
        stacked then the default is "lines+markers". Otherwise,
        "lines".

        The 'mode' property is a flaglist and may be specified
        as a string containing:
          - Any combination of ['lines', 'markers', 'text'] joined with '+' characters
            (e.g. 'lines+markers')
            OR exactly one of ['none'] (e.g. 'none')

        Returns
        -------
        Any
        """
        return self["mode"]

    @mode.setter
    def mode(self, val):
        self["mode"] = val

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
        return self["name"]

    @name.setter
    def name(self, val):
        self["name"] = val

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
        return self["opacity"]

    @opacity.setter
    def opacity(self, val):
        self["opacity"] = val

    @property
    def r(self):
        """
        Sets the radial coordinates

        The 'r' property is an array that may be specified as a tuple,
        list, numpy array, or pandas Series

        Returns
        -------
        NDArray
        """
        return self["r"]

    @r.setter
    def r(self, val):
        self["r"] = val

    @property
    def r0(self):
        """
        Alternate to `r`. Builds a linear space of r coordinates. Use
        with `dr` where `r0` is the starting coordinate and `dr` the
        step.

        The 'r0' property accepts values of any type

        Returns
        -------
        Any
        """
        return self["r0"]

    @r0.setter
    def r0(self, val):
        self["r0"] = val

    @property
    def rsrc(self):
        """
        Sets the source reference on Chart Studio Cloud for `r`.

        The 'rsrc' property must be specified as a string or
        as a plotly.grid_objs.Column object

        Returns
        -------
        str
        """
        return self["rsrc"]

    @rsrc.setter
    def rsrc(self, val):
        self["rsrc"] = val

    @property
    def selected(self):
        """
        The 'selected' property is an instance of Selected
        that may be specified as:
          - An instance of :class:`plotly.graph_objs.scatterpolar.Selected`
          - A dict of string/value properties that will be passed
            to the Selected constructor

        Returns
        -------
        plotly.graph_objs.scatterpolar.Selected
        """
        return self["selected"]

    @selected.setter
    def selected(self, val):
        self["selected"] = val

    @property
    def selectedpoints(self):
        """
        Array containing integer indices of selected points. Has an
        effect only for traces that support selections. Note that an
        empty array means an empty selection where the `unselected` are
        turned on for all points, whereas, any other non-array values
        means no selection all where the `selected` and `unselected`
        styles have no effect.

        The 'selectedpoints' property accepts values of any type

        Returns
        -------
        Any
        """
        return self["selectedpoints"]

    @selectedpoints.setter
    def selectedpoints(self, val):
        self["selectedpoints"] = val

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
        return self["showlegend"]

    @showlegend.setter
    def showlegend(self, val):
        self["showlegend"] = val

    @property
    def stream(self):
        """
        The 'stream' property is an instance of Stream
        that may be specified as:
          - An instance of :class:`plotly.graph_objs.scatterpolar.Stream`
          - A dict of string/value properties that will be passed
            to the Stream constructor

        Returns
        -------
        plotly.graph_objs.scatterpolar.Stream
        """
        return self["stream"]

    @stream.setter
    def stream(self, val):
        self["stream"] = val

    @property
    def subplot(self):
        """
        Sets a reference between this trace's data coordinates and a
        polar subplot. If "polar" (the default value), the data refer
        to `layout.polar`. If "polar2", the data refer to
        `layout.polar2`, and so on.

        The 'subplot' property is an identifier of a particular
        subplot, of type 'polar', that may be specified as the string 'polar'
        optionally followed by an integer >= 1
        (e.g. 'polar', 'polar1', 'polar2', 'polar3', etc.)

        Returns
        -------
        str
        """
        return self["subplot"]

    @subplot.setter
    def subplot(self, val):
        self["subplot"] = val

    @property
    def text(self):
        """
        Sets text elements associated with each (x,y) pair. If a single
        string, the same string appears over all the data points. If an
        array of string, the items are mapped in order to the this
        trace's (x,y) coordinates. If trace `hoverinfo` contains a
        "text" flag and "hovertext" is not set, these elements will be
        seen in the hover labels.

        The 'text' property is a string and must be specified as:
          - A string
          - A number that will be converted to a string
          - A tuple, list, or one-dimensional numpy array of the above

        Returns
        -------
        str|NDArray
        """
        return self["text"]

    @text.setter
    def text(self, val):
        self["text"] = val

    @property
    def textfont(self):
        """
        Sets the text font.

        The 'textfont' property is an instance of Textfont
        that may be specified as:
          - An instance of :class:`plotly.graph_objs.scatterpolar.Textfont`
          - A dict of string/value properties that will be passed
            to the Textfont constructor

        Returns
        -------
        plotly.graph_objs.scatterpolar.Textfont
        """
        return self["textfont"]

    @textfont.setter
    def textfont(self, val):
        self["textfont"] = val

    @property
    def textposition(self):
        """
        Sets the positions of the `text` elements with respects to the
        (x,y) coordinates.

        The 'textposition' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['top left', 'top center', 'top right', 'middle left',
                'middle center', 'middle right', 'bottom left', 'bottom
                center', 'bottom right']
          - A tuple, list, or one-dimensional numpy array of the above

        Returns
        -------
        Any|NDArray
        """
        return self["textposition"]

    @textposition.setter
    def textposition(self, val):
        self["textposition"] = val

    @property
    def textpositionsrc(self):
        """
        Sets the source reference on Chart Studio Cloud for
        `textposition`.

        The 'textpositionsrc' property must be specified as a string or
        as a plotly.grid_objs.Column object

        Returns
        -------
        str
        """
        return self["textpositionsrc"]

    @textpositionsrc.setter
    def textpositionsrc(self, val):
        self["textpositionsrc"] = val

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
        return self["textsrc"]

    @textsrc.setter
    def textsrc(self, val):
        self["textsrc"] = val

    @property
    def texttemplate(self):
        """
        Template string used for rendering the information text that
        appear on points. Note that this will override `textinfo`.
        Variables are inserted using %{variable}, for example "y:
        %{y}". Numbers are formatted using d3-format's syntax
        %{variable:d3-format}, for example "Price: %{y:$.2f}".
        https://github.com/d3/d3-format/tree/v1.4.5#d3-format for
        details on the formatting syntax. Dates are formatted using
        d3-time-format's syntax %{variable|d3-time-format}, for example
        "Day: %{2019-01-01|%A}". https://github.com/d3/d3-time-
        format/tree/v2.2.3#locale_format for details on the date
        formatting syntax. Every attributes that can be specified per-
        point (the ones that are `arrayOk: true`) are available.
        Finally, the template string has access to variables `r`,
        `theta` and `text`.

        The 'texttemplate' property is a string and must be specified as:
          - A string
          - A number that will be converted to a string
          - A tuple, list, or one-dimensional numpy array of the above

        Returns
        -------
        str|NDArray
        """
        return self["texttemplate"]

    @texttemplate.setter
    def texttemplate(self, val):
        self["texttemplate"] = val

    @property
    def texttemplatesrc(self):
        """
        Sets the source reference on Chart Studio Cloud for
        `texttemplate`.

        The 'texttemplatesrc' property must be specified as a string or
        as a plotly.grid_objs.Column object

        Returns
        -------
        str
        """
        return self["texttemplatesrc"]

    @texttemplatesrc.setter
    def texttemplatesrc(self, val):
        self["texttemplatesrc"] = val

    @property
    def theta(self):
        """
        Sets the angular coordinates

        The 'theta' property is an array that may be specified as a tuple,
        list, numpy array, or pandas Series

        Returns
        -------
        NDArray
        """
        return self["theta"]

    @theta.setter
    def theta(self, val):
        self["theta"] = val

    @property
    def theta0(self):
        """
        Alternate to `theta`. Builds a linear space of theta
        coordinates. Use with `dtheta` where `theta0` is the starting
        coordinate and `dtheta` the step.

        The 'theta0' property accepts values of any type

        Returns
        -------
        Any
        """
        return self["theta0"]

    @theta0.setter
    def theta0(self, val):
        self["theta0"] = val

    @property
    def thetasrc(self):
        """
        Sets the source reference on Chart Studio Cloud for `theta`.

        The 'thetasrc' property must be specified as a string or
        as a plotly.grid_objs.Column object

        Returns
        -------
        str
        """
        return self["thetasrc"]

    @thetasrc.setter
    def thetasrc(self, val):
        self["thetasrc"] = val

    @property
    def thetaunit(self):
        """
        Sets the unit of input "theta" values. Has an effect only when
        on "linear" angular axes.

        The 'thetaunit' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['radians', 'degrees', 'gradians']

        Returns
        -------
        Any
        """
        return self["thetaunit"]

    @thetaunit.setter
    def thetaunit(self, val):
        self["thetaunit"] = val

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
        return self["uid"]

    @uid.setter
    def uid(self, val):
        self["uid"] = val

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
        return self["uirevision"]

    @uirevision.setter
    def uirevision(self, val):
        self["uirevision"] = val

    @property
    def unselected(self):
        """
        The 'unselected' property is an instance of Unselected
        that may be specified as:
          - An instance of :class:`plotly.graph_objs.scatterpolar.Unselected`
          - A dict of string/value properties that will be passed
            to the Unselected constructor

        Returns
        -------
        plotly.graph_objs.scatterpolar.Unselected
        """
        return self["unselected"]

    @unselected.setter
    def unselected(self, val):
        self["unselected"] = val

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
        return self["visible"]

    @visible.setter
    def visible(self, val):
        self["visible"] = val

    @property
    def type(self):
        return self._props["type"]

    @property
    def _prop_descriptions(self):
        return """\
        cliponaxis
            Determines whether or not markers and text nodes are
            clipped about the subplot axes. To show markers and
            text nodes above axis lines and tick labels, make sure
            to set `xaxis.layer` and `yaxis.layer` to *below
            traces*.
        connectgaps
            Determines whether or not gaps (i.e. {nan} or missing
            values) in the provided data arrays are connected.
        customdata
            Assigns extra data each datum. This may be useful when
            listening to hover, click and selection events. Note
            that, "scatter" traces also appends customdata items in
            the markers DOM elements
        customdatasrc
            Sets the source reference on Chart Studio Cloud for
            `customdata`.
        dr
            Sets the r coordinate step.
        dtheta
            Sets the theta coordinate step. By default, the
            `dtheta` step equals the subplot's period divided by
            the length of the `r` coordinates.
        fill
            Sets the area to fill with a solid color. Use with
            `fillcolor` if not "none". scatterpolar has a subset of
            the options available to scatter. "toself" connects the
            endpoints of the trace (or each segment of the trace if
            it has gaps) into a closed shape. "tonext" fills the
            space between two traces if one completely encloses the
            other (eg consecutive contour lines), and behaves like
            "toself" if there is no trace before it. "tonext"
            should not be used if one trace does not enclose the
            other.
        fillcolor
            Sets the fill color. Defaults to a half-transparent
            variant of the line color, marker color, or marker line
            color, whichever is available.
        hoverinfo
            Determines which trace information appear on hover. If
            `none` or `skip` are set, no information is displayed
            upon hovering. But, if `none` is set, click and hover
            events are still fired.
        hoverinfosrc
            Sets the source reference on Chart Studio Cloud for
            `hoverinfo`.
        hoverlabel
            :class:`plotly.graph_objects.scatterpolar.Hoverlabel`
            instance or dict with compatible properties
        hoveron
            Do the hover effects highlight individual points
            (markers or line points) or do they highlight filled
            regions? If the fill is "toself" or "tonext" and there
            are no markers or text, then the default is "fills",
            otherwise it is "points".
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
            Sets hover text elements associated with each (x,y)
            pair. If a single string, the same string appears over
            all the data points. If an array of string, the items
            are mapped in order to the this trace's (x,y)
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
            :class:`plotly.graph_objects.scatterpolar.Legendgroupti
            tle` instance or dict with compatible properties
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
        line
            :class:`plotly.graph_objects.scatterpolar.Line`
            instance or dict with compatible properties
        marker
            :class:`plotly.graph_objects.scatterpolar.Marker`
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
        mode
            Determines the drawing mode for this scatter trace. If
            the provided `mode` includes "text" then the `text`
            elements appear at the coordinates. Otherwise, the
            `text` elements appear on hover. If there are less than
            20 points and the trace is not stacked then the default
            is "lines+markers". Otherwise, "lines".
        name
            Sets the trace name. The trace name appears as the
            legend item and on hover.
        opacity
            Sets the opacity of the trace.
        r
            Sets the radial coordinates
        r0
            Alternate to `r`. Builds a linear space of r
            coordinates. Use with `dr` where `r0` is the starting
            coordinate and `dr` the step.
        rsrc
            Sets the source reference on Chart Studio Cloud for
            `r`.
        selected
            :class:`plotly.graph_objects.scatterpolar.Selected`
            instance or dict with compatible properties
        selectedpoints
            Array containing integer indices of selected points.
            Has an effect only for traces that support selections.
            Note that an empty array means an empty selection where
            the `unselected` are turned on for all points, whereas,
            any other non-array values means no selection all where
            the `selected` and `unselected` styles have no effect.
        showlegend
            Determines whether or not an item corresponding to this
            trace is shown in the legend.
        stream
            :class:`plotly.graph_objects.scatterpolar.Stream`
            instance or dict with compatible properties
        subplot
            Sets a reference between this trace's data coordinates
            and a polar subplot. If "polar" (the default value),
            the data refer to `layout.polar`. If "polar2", the data
            refer to `layout.polar2`, and so on.
        text
            Sets text elements associated with each (x,y) pair. If
            a single string, the same string appears over all the
            data points. If an array of string, the items are
            mapped in order to the this trace's (x,y) coordinates.
            If trace `hoverinfo` contains a "text" flag and
            "hovertext" is not set, these elements will be seen in
            the hover labels.
        textfont
            Sets the text font.
        textposition
            Sets the positions of the `text` elements with respects
            to the (x,y) coordinates.
        textpositionsrc
            Sets the source reference on Chart Studio Cloud for
            `textposition`.
        textsrc
            Sets the source reference on Chart Studio Cloud for
            `text`.
        texttemplate
            Template string used for rendering the information text
            that appear on points. Note that this will override
            `textinfo`. Variables are inserted using %{variable},
            for example "y: %{y}". Numbers are formatted using
            d3-format's syntax %{variable:d3-format}, for example
            "Price: %{y:$.2f}".
            https://github.com/d3/d3-format/tree/v1.4.5#d3-format
            for details on the formatting syntax. Dates are
            formatted using d3-time-format's syntax
            %{variable|d3-time-format}, for example "Day:
            %{2019-01-01|%A}". https://github.com/d3/d3-time-
            format/tree/v2.2.3#locale_format for details on the
            date formatting syntax. Every attributes that can be
            specified per-point (the ones that are `arrayOk: true`)
            are available. Finally, the template string has access
            to variables `r`, `theta` and `text`.
        texttemplatesrc
            Sets the source reference on Chart Studio Cloud for
            `texttemplate`.
        theta
            Sets the angular coordinates
        theta0
            Alternate to `theta`. Builds a linear space of theta
            coordinates. Use with `dtheta` where `theta0` is the
            starting coordinate and `dtheta` the step.
        thetasrc
            Sets the source reference on Chart Studio Cloud for
            `theta`.
        thetaunit
            Sets the unit of input "theta" values. Has an effect
            only when on "linear" angular axes.
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
        unselected
            :class:`plotly.graph_objects.scatterpolar.Unselected`
            instance or dict with compatible properties
        visible
            Determines whether or not this trace is visible. If
            "legendonly", the trace is not drawn, but can appear as
            a legend item (provided that the legend itself is
            visible).
        """

    def __init__(
        self,
        arg=None,
        cliponaxis: bool | None = None,
        connectgaps: bool | None = None,
        customdata: NDArray | None = None,
        customdatasrc: str | None = None,
        dr: int | float | None = None,
        dtheta: int | float | None = None,
        fill: Any | None = None,
        fillcolor: str | None = None,
        hoverinfo: Any | None = None,
        hoverinfosrc: str | None = None,
        hoverlabel: None | None = None,
        hoveron: Any | None = None,
        hovertemplate: str | None = None,
        hovertemplatesrc: str | None = None,
        hovertext: str | None = None,
        hovertextsrc: str | None = None,
        ids: NDArray | None = None,
        idssrc: str | None = None,
        legend: str | None = None,
        legendgroup: str | None = None,
        legendgrouptitle: None | None = None,
        legendrank: int | float | None = None,
        legendwidth: int | float | None = None,
        line: None | None = None,
        marker: None | None = None,
        meta: Any | None = None,
        metasrc: str | None = None,
        mode: Any | None = None,
        name: str | None = None,
        opacity: int | float | None = None,
        r: NDArray | None = None,
        r0: Any | None = None,
        rsrc: str | None = None,
        selected: None | None = None,
        selectedpoints: Any | None = None,
        showlegend: bool | None = None,
        stream: None | None = None,
        subplot: str | None = None,
        text: str | None = None,
        textfont: None | None = None,
        textposition: Any | None = None,
        textpositionsrc: str | None = None,
        textsrc: str | None = None,
        texttemplate: str | None = None,
        texttemplatesrc: str | None = None,
        theta: NDArray | None = None,
        theta0: Any | None = None,
        thetasrc: str | None = None,
        thetaunit: Any | None = None,
        uid: str | None = None,
        uirevision: Any | None = None,
        unselected: None | None = None,
        visible: Any | None = None,
        **kwargs,
    ):
        """
        Construct a new Scatterpolar object

        The scatterpolar trace type encompasses line charts, scatter
        charts, text charts, and bubble charts in polar coordinates.
        The data visualized as scatter point or lines is set in `r`
        (radial) and `theta` (angular) coordinates Text (appearing
        either on the chart or on hover only) is via `text`. Bubble
        charts are achieved by setting `marker.size` and/or
        `marker.color` to numerical arrays.

        Parameters
        ----------
        arg
            dict of properties compatible with this constructor or
            an instance of :class:`plotly.graph_objs.Scatterpolar`
        cliponaxis
            Determines whether or not markers and text nodes are
            clipped about the subplot axes. To show markers and
            text nodes above axis lines and tick labels, make sure
            to set `xaxis.layer` and `yaxis.layer` to *below
            traces*.
        connectgaps
            Determines whether or not gaps (i.e. {nan} or missing
            values) in the provided data arrays are connected.
        customdata
            Assigns extra data each datum. This may be useful when
            listening to hover, click and selection events. Note
            that, "scatter" traces also appends customdata items in
            the markers DOM elements
        customdatasrc
            Sets the source reference on Chart Studio Cloud for
            `customdata`.
        dr
            Sets the r coordinate step.
        dtheta
            Sets the theta coordinate step. By default, the
            `dtheta` step equals the subplot's period divided by
            the length of the `r` coordinates.
        fill
            Sets the area to fill with a solid color. Use with
            `fillcolor` if not "none". scatterpolar has a subset of
            the options available to scatter. "toself" connects the
            endpoints of the trace (or each segment of the trace if
            it has gaps) into a closed shape. "tonext" fills the
            space between two traces if one completely encloses the
            other (eg consecutive contour lines), and behaves like
            "toself" if there is no trace before it. "tonext"
            should not be used if one trace does not enclose the
            other.
        fillcolor
            Sets the fill color. Defaults to a half-transparent
            variant of the line color, marker color, or marker line
            color, whichever is available.
        hoverinfo
            Determines which trace information appear on hover. If
            `none` or `skip` are set, no information is displayed
            upon hovering. But, if `none` is set, click and hover
            events are still fired.
        hoverinfosrc
            Sets the source reference on Chart Studio Cloud for
            `hoverinfo`.
        hoverlabel
            :class:`plotly.graph_objects.scatterpolar.Hoverlabel`
            instance or dict with compatible properties
        hoveron
            Do the hover effects highlight individual points
            (markers or line points) or do they highlight filled
            regions? If the fill is "toself" or "tonext" and there
            are no markers or text, then the default is "fills",
            otherwise it is "points".
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
            Sets hover text elements associated with each (x,y)
            pair. If a single string, the same string appears over
            all the data points. If an array of string, the items
            are mapped in order to the this trace's (x,y)
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
            :class:`plotly.graph_objects.scatterpolar.Legendgroupti
            tle` instance or dict with compatible properties
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
        line
            :class:`plotly.graph_objects.scatterpolar.Line`
            instance or dict with compatible properties
        marker
            :class:`plotly.graph_objects.scatterpolar.Marker`
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
        mode
            Determines the drawing mode for this scatter trace. If
            the provided `mode` includes "text" then the `text`
            elements appear at the coordinates. Otherwise, the
            `text` elements appear on hover. If there are less than
            20 points and the trace is not stacked then the default
            is "lines+markers". Otherwise, "lines".
        name
            Sets the trace name. The trace name appears as the
            legend item and on hover.
        opacity
            Sets the opacity of the trace.
        r
            Sets the radial coordinates
        r0
            Alternate to `r`. Builds a linear space of r
            coordinates. Use with `dr` where `r0` is the starting
            coordinate and `dr` the step.
        rsrc
            Sets the source reference on Chart Studio Cloud for
            `r`.
        selected
            :class:`plotly.graph_objects.scatterpolar.Selected`
            instance or dict with compatible properties
        selectedpoints
            Array containing integer indices of selected points.
            Has an effect only for traces that support selections.
            Note that an empty array means an empty selection where
            the `unselected` are turned on for all points, whereas,
            any other non-array values means no selection all where
            the `selected` and `unselected` styles have no effect.
        showlegend
            Determines whether or not an item corresponding to this
            trace is shown in the legend.
        stream
            :class:`plotly.graph_objects.scatterpolar.Stream`
            instance or dict with compatible properties
        subplot
            Sets a reference between this trace's data coordinates
            and a polar subplot. If "polar" (the default value),
            the data refer to `layout.polar`. If "polar2", the data
            refer to `layout.polar2`, and so on.
        text
            Sets text elements associated with each (x,y) pair. If
            a single string, the same string appears over all the
            data points. If an array of string, the items are
            mapped in order to the this trace's (x,y) coordinates.
            If trace `hoverinfo` contains a "text" flag and
            "hovertext" is not set, these elements will be seen in
            the hover labels.
        textfont
            Sets the text font.
        textposition
            Sets the positions of the `text` elements with respects
            to the (x,y) coordinates.
        textpositionsrc
            Sets the source reference on Chart Studio Cloud for
            `textposition`.
        textsrc
            Sets the source reference on Chart Studio Cloud for
            `text`.
        texttemplate
            Template string used for rendering the information text
            that appear on points. Note that this will override
            `textinfo`. Variables are inserted using %{variable},
            for example "y: %{y}". Numbers are formatted using
            d3-format's syntax %{variable:d3-format}, for example
            "Price: %{y:$.2f}".
            https://github.com/d3/d3-format/tree/v1.4.5#d3-format
            for details on the formatting syntax. Dates are
            formatted using d3-time-format's syntax
            %{variable|d3-time-format}, for example "Day:
            %{2019-01-01|%A}". https://github.com/d3/d3-time-
            format/tree/v2.2.3#locale_format for details on the
            date formatting syntax. Every attributes that can be
            specified per-point (the ones that are `arrayOk: true`)
            are available. Finally, the template string has access
            to variables `r`, `theta` and `text`.
        texttemplatesrc
            Sets the source reference on Chart Studio Cloud for
            `texttemplate`.
        theta
            Sets the angular coordinates
        theta0
            Alternate to `theta`. Builds a linear space of theta
            coordinates. Use with `dtheta` where `theta0` is the
            starting coordinate and `dtheta` the step.
        thetasrc
            Sets the source reference on Chart Studio Cloud for
            `theta`.
        thetaunit
            Sets the unit of input "theta" values. Has an effect
            only when on "linear" angular axes.
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
        unselected
            :class:`plotly.graph_objects.scatterpolar.Unselected`
            instance or dict with compatible properties
        visible
            Determines whether or not this trace is visible. If
            "legendonly", the trace is not drawn, but can appear as
            a legend item (provided that the legend itself is
            visible).

        Returns
        -------
        Scatterpolar
        """
        super().__init__("scatterpolar")
        if "_parent" in kwargs:
            self._parent = kwargs["_parent"]
            return

        if arg is None:
            arg = {}
        elif isinstance(arg, self.__class__):
            arg = arg.to_plotly_json()
        elif isinstance(arg, dict):
            arg = _copy.copy(arg)
        else:
            raise ValueError(
                """\
The first argument to the plotly.graph_objs.Scatterpolar
constructor must be a dict or
an instance of :class:`plotly.graph_objs.Scatterpolar`"""
            )

        self._skip_invalid = kwargs.pop("skip_invalid", False)
        self._validate = kwargs.pop("_validate", True)

        self._init_provided("cliponaxis", arg, cliponaxis)
        self._init_provided("connectgaps", arg, connectgaps)
        self._init_provided("customdata", arg, customdata)
        self._init_provided("customdatasrc", arg, customdatasrc)
        self._init_provided("dr", arg, dr)
        self._init_provided("dtheta", arg, dtheta)
        self._init_provided("fill", arg, fill)
        self._init_provided("fillcolor", arg, fillcolor)
        self._init_provided("hoverinfo", arg, hoverinfo)
        self._init_provided("hoverinfosrc", arg, hoverinfosrc)
        self._init_provided("hoverlabel", arg, hoverlabel)
        self._init_provided("hoveron", arg, hoveron)
        self._init_provided("hovertemplate", arg, hovertemplate)
        self._init_provided("hovertemplatesrc", arg, hovertemplatesrc)
        self._init_provided("hovertext", arg, hovertext)
        self._init_provided("hovertextsrc", arg, hovertextsrc)
        self._init_provided("ids", arg, ids)
        self._init_provided("idssrc", arg, idssrc)
        self._init_provided("legend", arg, legend)
        self._init_provided("legendgroup", arg, legendgroup)
        self._init_provided("legendgrouptitle", arg, legendgrouptitle)
        self._init_provided("legendrank", arg, legendrank)
        self._init_provided("legendwidth", arg, legendwidth)
        self._init_provided("line", arg, line)
        self._init_provided("marker", arg, marker)
        self._init_provided("meta", arg, meta)
        self._init_provided("metasrc", arg, metasrc)
        self._init_provided("mode", arg, mode)
        self._init_provided("name", arg, name)
        self._init_provided("opacity", arg, opacity)
        self._init_provided("r", arg, r)
        self._init_provided("r0", arg, r0)
        self._init_provided("rsrc", arg, rsrc)
        self._init_provided("selected", arg, selected)
        self._init_provided("selectedpoints", arg, selectedpoints)
        self._init_provided("showlegend", arg, showlegend)
        self._init_provided("stream", arg, stream)
        self._init_provided("subplot", arg, subplot)
        self._init_provided("text", arg, text)
        self._init_provided("textfont", arg, textfont)
        self._init_provided("textposition", arg, textposition)
        self._init_provided("textpositionsrc", arg, textpositionsrc)
        self._init_provided("textsrc", arg, textsrc)
        self._init_provided("texttemplate", arg, texttemplate)
        self._init_provided("texttemplatesrc", arg, texttemplatesrc)
        self._init_provided("theta", arg, theta)
        self._init_provided("theta0", arg, theta0)
        self._init_provided("thetasrc", arg, thetasrc)
        self._init_provided("thetaunit", arg, thetaunit)
        self._init_provided("uid", arg, uid)
        self._init_provided("uirevision", arg, uirevision)
        self._init_provided("unselected", arg, unselected)
        self._init_provided("visible", arg, visible)

        self._props["type"] = "scatterpolar"
        arg.pop("type", None)
        self._process_kwargs(**dict(arg, **kwargs))
        self._skip_invalid = False
