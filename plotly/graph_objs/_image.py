

from __future__ import annotations
from typing import Any
from numpy.typing import NDArray
from plotly.basedatatypes import BaseTraceType as _BaseTraceType
import copy as _copy


class Image(_BaseTraceType):

    # class properties
    # --------------------
    _parent_path_str = ''
    _path_str = 'image'
    _valid_props = {"colormodel", "customdata", "customdatasrc", "dx", "dy", "hoverinfo", "hoverinfosrc", "hoverlabel", "hovertemplate", "hovertemplatesrc", "hovertext", "hovertextsrc", "ids", "idssrc", "legend", "legendgrouptitle", "legendrank", "legendwidth", "meta", "metasrc", "name", "opacity", "source", "stream", "text", "textsrc", "type", "uid", "uirevision", "visible", "x0", "xaxis", "y0", "yaxis", "z", "zmax", "zmin", "zorder", "zsmooth", "zsrc"}

    # colormodel
    # ----------
    @property
    def colormodel(self):
        """
        Color model used to map the numerical color components
        described in `z` into colors. If `source` is specified, this
        attribute will be set to `rgba256` otherwise it defaults to
        `rgb`.

        The 'colormodel' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['rgb', 'rgba', 'rgba256', 'hsl', 'hsla']

        Returns
        -------
        Any
        """
        return self['colormodel']

    @colormodel.setter
    def colormodel(self, val):
        self['colormodel'] = val

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
        NDArray
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

    # dx
    # --
    @property
    def dx(self):
        """
        Set the pixel's horizontal size.

        The 'dx' property is a number and may be specified as:
          - An int or float

        Returns
        -------
        int|float
        """
        return self['dx']

    @dx.setter
    def dx(self, val):
        self['dx'] = val

    # dy
    # --
    @property
    def dy(self):
        """
        Set the pixel's vertical size

        The 'dy' property is a number and may be specified as:
          - An int or float

        Returns
        -------
        int|float
        """
        return self['dy']

    @dy.setter
    def dy(self, val):
        self['dy'] = val

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
          - Any combination of ['x', 'y', 'z', 'color', 'name', 'text'] joined with '+' characters
            (e.g. 'x+y')
            OR exactly one of ['all', 'none', 'skip'] (e.g. 'skip')
          - A list or array of the above

        Returns
        -------
        Any|NDArray
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
          - An instance of :class:`plotly.graph_objs.image.Hoverlabel`
          - A dict of string/value properties that will be passed
            to the Hoverlabel constructor

        Returns
        -------
        plotly.graph_objs.image.Hoverlabel
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
        (the ones that are `arrayOk: true`) are available. Finally, the
        template string has access to variables `z`, `color` and
        `colormodel`. Anything contained in tag `<extra>` is displayed
        in the secondary box, for example
        "<extra>{fullData.name}</extra>". To hide the secondary box
        completely, use an empty tag `<extra></extra>`.

        The 'hovertemplate' property is a string and must be specified as:
          - A string
          - A number that will be converted to a string
          - A tuple, list, or one-dimensional numpy array of the above

        Returns
        -------
        str|NDArray
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

        The 'hovertext' property is an array that may be specified as a tuple,
        list, numpy array, or pandas Series

        Returns
        -------
        NDArray
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
        NDArray
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

    # legendgrouptitle
    # ----------------
    @property
    def legendgrouptitle(self):
        """
        The 'legendgrouptitle' property is an instance of Legendgrouptitle
        that may be specified as:
          - An instance of :class:`plotly.graph_objs.image.Legendgrouptitle`
          - A dict of string/value properties that will be passed
            to the Legendgrouptitle constructor

        Returns
        -------
        plotly.graph_objs.image.Legendgrouptitle
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
        Any|NDArray
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

    # source
    # ------
    @property
    def source(self):
        """
        Specifies the data URI of the image to be visualized. The URI
        consists of "data:image/[<media subtype>][;base64],<data>"

        The 'source' property is a string and must be specified as:
          - A string
          - A number that will be converted to a string

        Returns
        -------
        str
        """
        return self['source']

    @source.setter
    def source(self, val):
        self['source'] = val

    # stream
    # ------
    @property
    def stream(self):
        """
        The 'stream' property is an instance of Stream
        that may be specified as:
          - An instance of :class:`plotly.graph_objs.image.Stream`
          - A dict of string/value properties that will be passed
            to the Stream constructor

        Returns
        -------
        plotly.graph_objs.image.Stream
        """
        return self['stream']

    @stream.setter
    def stream(self, val):
        self['stream'] = val

    # text
    # ----
    @property
    def text(self):
        """
        Sets the text elements associated with each z value.

        The 'text' property is an array that may be specified as a tuple,
        list, numpy array, or pandas Series

        Returns
        -------
        NDArray
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

    # x0
    # --
    @property
    def x0(self):
        """
        Set the image's x position. The left edge of the image (or the
        right edge if the x axis is reversed or dx is negative) will be
        found at xmin=x0-dx/2

        The 'x0' property accepts values of any type

        Returns
        -------
        Any
        """
        return self['x0']

    @x0.setter
    def x0(self, val):
        self['x0'] = val

    # xaxis
    # -----
    @property
    def xaxis(self):
        """
        Sets a reference between this trace's x coordinates and a 2D
        cartesian x axis. If "x" (the default value), the x coordinates
        refer to `layout.xaxis`. If "x2", the x coordinates refer to
        `layout.xaxis2`, and so on.

        The 'xaxis' property is an identifier of a particular
        subplot, of type 'x', that may be specified as the string 'x'
        optionally followed by an integer >= 1
        (e.g. 'x', 'x1', 'x2', 'x3', etc.)

        Returns
        -------
        str
        """
        return self['xaxis']

    @xaxis.setter
    def xaxis(self, val):
        self['xaxis'] = val

    # y0
    # --
    @property
    def y0(self):
        """
        Set the image's y position. The top edge of the image (or the
        bottom edge if the y axis is NOT reversed or if dy is negative)
        will be found at ymin=y0-dy/2. By default when an image trace
        is included, the y axis will be reversed so that the image is
        right-side-up, but you can disable this by setting
        yaxis.autorange=true or by providing an explicit y axis range.

        The 'y0' property accepts values of any type

        Returns
        -------
        Any
        """
        return self['y0']

    @y0.setter
    def y0(self, val):
        self['y0'] = val

    # yaxis
    # -----
    @property
    def yaxis(self):
        """
        Sets a reference between this trace's y coordinates and a 2D
        cartesian y axis. If "y" (the default value), the y coordinates
        refer to `layout.yaxis`. If "y2", the y coordinates refer to
        `layout.yaxis2`, and so on.

        The 'yaxis' property is an identifier of a particular
        subplot, of type 'y', that may be specified as the string 'y'
        optionally followed by an integer >= 1
        (e.g. 'y', 'y1', 'y2', 'y3', etc.)

        Returns
        -------
        str
        """
        return self['yaxis']

    @yaxis.setter
    def yaxis(self, val):
        self['yaxis'] = val

    # z
    # -
    @property
    def z(self):
        """
        A 2-dimensional array in which each element is an array of 3 or
        4 numbers representing a color.

        The 'z' property is an array that may be specified as a tuple,
        list, numpy array, or pandas Series

        Returns
        -------
        NDArray
        """
        return self['z']

    @z.setter
    def z(self, val):
        self['z'] = val

    # zmax
    # ----
    @property
    def zmax(self):
        """
        Array defining the higher bound for each color component. Note
        that the default value will depend on the colormodel. For the
        `rgb` colormodel, it is [255, 255, 255]. For the `rgba`
        colormodel, it is [255, 255, 255, 1]. For the `rgba256`
        colormodel, it is [255, 255, 255, 255]. For the `hsl`
        colormodel, it is [360, 100, 100]. For the `hsla` colormodel,
        it is [360, 100, 100, 1].

        The 'zmax' property is an info array that may be specified as:
    
        * a list or tuple of 4 elements where:
    (0) The 'zmax[0]' property is a number and may be specified as:
          - An int or float
    (1) The 'zmax[1]' property is a number and may be specified as:
          - An int or float
    (2) The 'zmax[2]' property is a number and may be specified as:
          - An int or float
    (3) The 'zmax[3]' property is a number and may be specified as:
          - An int or float

        Returns
        -------
        list
        """
        return self['zmax']

    @zmax.setter
    def zmax(self, val):
        self['zmax'] = val

    # zmin
    # ----
    @property
    def zmin(self):
        """
        Array defining the lower bound for each color component. Note
        that the default value will depend on the colormodel. For the
        `rgb` colormodel, it is [0, 0, 0]. For the `rgba` colormodel,
        it is [0, 0, 0, 0]. For the `rgba256` colormodel, it is [0, 0,
        0, 0]. For the `hsl` colormodel, it is [0, 0, 0]. For the
        `hsla` colormodel, it is [0, 0, 0, 0].

        The 'zmin' property is an info array that may be specified as:
    
        * a list or tuple of 4 elements where:
    (0) The 'zmin[0]' property is a number and may be specified as:
          - An int or float
    (1) The 'zmin[1]' property is a number and may be specified as:
          - An int or float
    (2) The 'zmin[2]' property is a number and may be specified as:
          - An int or float
    (3) The 'zmin[3]' property is a number and may be specified as:
          - An int or float

        Returns
        -------
        list
        """
        return self['zmin']

    @zmin.setter
    def zmin(self, val):
        self['zmin'] = val

    # zorder
    # ------
    @property
    def zorder(self):
        """
        Sets the layer on which this trace is displayed, relative to
        other SVG traces on the same subplot. SVG traces with higher
        `zorder` appear in front of those with lower `zorder`.

        The 'zorder' property is a integer and may be specified as:
          - An int (or float that will be cast to an int)

        Returns
        -------
        int
        """
        return self['zorder']

    @zorder.setter
    def zorder(self, val):
        self['zorder'] = val

    # zsmooth
    # -------
    @property
    def zsmooth(self):
        """
        Picks a smoothing algorithm used to smooth `z` data. This only
        applies for image traces that use the `source` attribute.

        The 'zsmooth' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['fast', False]

        Returns
        -------
        Any
        """
        return self['zsmooth']

    @zsmooth.setter
    def zsmooth(self, val):
        self['zsmooth'] = val

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
        colormodel
            Color model used to map the numerical color components
            described in `z` into colors. If `source` is specified,
            this attribute will be set to `rgba256` otherwise it
            defaults to `rgb`.
        customdata
            Assigns extra data each datum. This may be useful when
            listening to hover, click and selection events. Note
            that, "scatter" traces also appends customdata items in
            the markers DOM elements
        customdatasrc
            Sets the source reference on Chart Studio Cloud for
            `customdata`.
        dx
            Set the pixel's horizontal size.
        dy
            Set the pixel's vertical size
        hoverinfo
            Determines which trace information appear on hover. If
            `none` or `skip` are set, no information is displayed
            upon hovering. But, if `none` is set, click and hover
            events are still fired.
        hoverinfosrc
            Sets the source reference on Chart Studio Cloud for
            `hoverinfo`.
        hoverlabel
            :class:`plotly.graph_objects.image.Hoverlabel` instance
            or dict with compatible properties
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
            are available. Finally, the template string has access
            to variables `z`, `color` and `colormodel`. Anything
            contained in tag `<extra>` is displayed in the
            secondary box, for example
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
        legend
            Sets the reference to a legend to show this trace in.
            References to these legends are "legend", "legend2",
            "legend3", etc. Settings for these legends are set in
            the layout, under `layout.legend`, `layout.legend2`,
            etc.
        legendgrouptitle
            :class:`plotly.graph_objects.image.Legendgrouptitle`
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
        source
            Specifies the data URI of the image to be visualized.
            The URI consists of "data:image/[<media
            subtype>][;base64],<data>"
        stream
            :class:`plotly.graph_objects.image.Stream` instance or
            dict with compatible properties
        text
            Sets the text elements associated with each z value.
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
        x0
            Set the image's x position. The left edge of the image
            (or the right edge if the x axis is reversed or dx is
            negative) will be found at xmin=x0-dx/2
        xaxis
            Sets a reference between this trace's x coordinates and
            a 2D cartesian x axis. If "x" (the default value), the
            x coordinates refer to `layout.xaxis`. If "x2", the x
            coordinates refer to `layout.xaxis2`, and so on.
        y0
            Set the image's y position. The top edge of the image
            (or the bottom edge if the y axis is NOT reversed or if
            dy is negative) will be found at ymin=y0-dy/2. By
            default when an image trace is included, the y axis
            will be reversed so that the image is right-side-up,
            but you can disable this by setting
            yaxis.autorange=true or by providing an explicit y axis
            range.
        yaxis
            Sets a reference between this trace's y coordinates and
            a 2D cartesian y axis. If "y" (the default value), the
            y coordinates refer to `layout.yaxis`. If "y2", the y
            coordinates refer to `layout.yaxis2`, and so on.
        z
            A 2-dimensional array in which each element is an array
            of 3 or 4 numbers representing a color.
        zmax
            Array defining the higher bound for each color
            component. Note that the default value will depend on
            the colormodel. For the `rgb` colormodel, it is [255,
            255, 255]. For the `rgba` colormodel, it is [255, 255,
            255, 1]. For the `rgba256` colormodel, it is [255, 255,
            255, 255]. For the `hsl` colormodel, it is [360, 100,
            100]. For the `hsla` colormodel, it is [360, 100, 100,
            1].
        zmin
            Array defining the lower bound for each color
            component. Note that the default value will depend on
            the colormodel. For the `rgb` colormodel, it is [0, 0,
            0]. For the `rgba` colormodel, it is [0, 0, 0, 0]. For
            the `rgba256` colormodel, it is [0, 0, 0, 0]. For the
            `hsl` colormodel, it is [0, 0, 0]. For the `hsla`
            colormodel, it is [0, 0, 0, 0].
        zorder
            Sets the layer on which this trace is displayed,
            relative to other SVG traces on the same subplot. SVG
            traces with higher `zorder` appear in front of those
            with lower `zorder`.
        zsmooth
            Picks a smoothing algorithm used to smooth `z` data.
            This only applies for image traces that use the
            `source` attribute.
        zsrc
            Sets the source reference on Chart Studio Cloud for
            `z`.
        """
    def __init__(self,
            arg=None,
            colormodel: Any|None = None,
            customdata: NDArray|None = None,
            customdatasrc: str|None = None,
            dx: int|float|None = None,
            dy: int|float|None = None,
            hoverinfo: Any|None = None,
            hoverinfosrc: str|None = None,
            hoverlabel: None|None = None,
            hovertemplate: str|None = None,
            hovertemplatesrc: str|None = None,
            hovertext: NDArray|None = None,
            hovertextsrc: str|None = None,
            ids: NDArray|None = None,
            idssrc: str|None = None,
            legend: str|None = None,
            legendgrouptitle: None|None = None,
            legendrank: int|float|None = None,
            legendwidth: int|float|None = None,
            meta: Any|None = None,
            metasrc: str|None = None,
            name: str|None = None,
            opacity: int|float|None = None,
            source: str|None = None,
            stream: None|None = None,
            text: NDArray|None = None,
            textsrc: str|None = None,
            uid: str|None = None,
            uirevision: Any|None = None,
            visible: Any|None = None,
            x0: Any|None = None,
            xaxis: str|None = None,
            y0: Any|None = None,
            yaxis: str|None = None,
            z: NDArray|None = None,
            zmax: list|None = None,
            zmin: list|None = None,
            zorder: int|None = None,
            zsmooth: Any|None = None,
            zsrc: str|None = None,
            **kwargs
        ):
        """
        Construct a new Image object

        Display an image, i.e. data on a 2D regular raster. By default,
        when an image is displayed in a subplot, its y axis will be
        reversed (ie. `autorange: 'reversed'`), constrained to the
        domain (ie. `constrain: 'domain'`) and it will have the same
        scale as its x axis (ie. `scaleanchor: 'x,`) in order for
        pixels to be rendered as squares.

        Parameters
        ----------
        arg
            dict of properties compatible with this constructor or
            an instance of :class:`plotly.graph_objs.Image`
        colormodel
            Color model used to map the numerical color components
            described in `z` into colors. If `source` is specified,
            this attribute will be set to `rgba256` otherwise it
            defaults to `rgb`.
        customdata
            Assigns extra data each datum. This may be useful when
            listening to hover, click and selection events. Note
            that, "scatter" traces also appends customdata items in
            the markers DOM elements
        customdatasrc
            Sets the source reference on Chart Studio Cloud for
            `customdata`.
        dx
            Set the pixel's horizontal size.
        dy
            Set the pixel's vertical size
        hoverinfo
            Determines which trace information appear on hover. If
            `none` or `skip` are set, no information is displayed
            upon hovering. But, if `none` is set, click and hover
            events are still fired.
        hoverinfosrc
            Sets the source reference on Chart Studio Cloud for
            `hoverinfo`.
        hoverlabel
            :class:`plotly.graph_objects.image.Hoverlabel` instance
            or dict with compatible properties
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
            are available. Finally, the template string has access
            to variables `z`, `color` and `colormodel`. Anything
            contained in tag `<extra>` is displayed in the
            secondary box, for example
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
        legend
            Sets the reference to a legend to show this trace in.
            References to these legends are "legend", "legend2",
            "legend3", etc. Settings for these legends are set in
            the layout, under `layout.legend`, `layout.legend2`,
            etc.
        legendgrouptitle
            :class:`plotly.graph_objects.image.Legendgrouptitle`
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
        source
            Specifies the data URI of the image to be visualized.
            The URI consists of "data:image/[<media
            subtype>][;base64],<data>"
        stream
            :class:`plotly.graph_objects.image.Stream` instance or
            dict with compatible properties
        text
            Sets the text elements associated with each z value.
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
        x0
            Set the image's x position. The left edge of the image
            (or the right edge if the x axis is reversed or dx is
            negative) will be found at xmin=x0-dx/2
        xaxis
            Sets a reference between this trace's x coordinates and
            a 2D cartesian x axis. If "x" (the default value), the
            x coordinates refer to `layout.xaxis`. If "x2", the x
            coordinates refer to `layout.xaxis2`, and so on.
        y0
            Set the image's y position. The top edge of the image
            (or the bottom edge if the y axis is NOT reversed or if
            dy is negative) will be found at ymin=y0-dy/2. By
            default when an image trace is included, the y axis
            will be reversed so that the image is right-side-up,
            but you can disable this by setting
            yaxis.autorange=true or by providing an explicit y axis
            range.
        yaxis
            Sets a reference between this trace's y coordinates and
            a 2D cartesian y axis. If "y" (the default value), the
            y coordinates refer to `layout.yaxis`. If "y2", the y
            coordinates refer to `layout.yaxis2`, and so on.
        z
            A 2-dimensional array in which each element is an array
            of 3 or 4 numbers representing a color.
        zmax
            Array defining the higher bound for each color
            component. Note that the default value will depend on
            the colormodel. For the `rgb` colormodel, it is [255,
            255, 255]. For the `rgba` colormodel, it is [255, 255,
            255, 1]. For the `rgba256` colormodel, it is [255, 255,
            255, 255]. For the `hsl` colormodel, it is [360, 100,
            100]. For the `hsla` colormodel, it is [360, 100, 100,
            1].
        zmin
            Array defining the lower bound for each color
            component. Note that the default value will depend on
            the colormodel. For the `rgb` colormodel, it is [0, 0,
            0]. For the `rgba` colormodel, it is [0, 0, 0, 0]. For
            the `rgba256` colormodel, it is [0, 0, 0, 0]. For the
            `hsl` colormodel, it is [0, 0, 0]. For the `hsla`
            colormodel, it is [0, 0, 0, 0].
        zorder
            Sets the layer on which this trace is displayed,
            relative to other SVG traces on the same subplot. SVG
            traces with higher `zorder` appear in front of those
            with lower `zorder`.
        zsmooth
            Picks a smoothing algorithm used to smooth `z` data.
            This only applies for image traces that use the
            `source` attribute.
        zsrc
            Sets the source reference on Chart Studio Cloud for
            `z`.

        Returns
        -------
        Image
        """
        super().__init__('image')
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
The first argument to the plotly.graph_objs.Image
constructor must be a dict or
an instance of :class:`plotly.graph_objs.Image`""")

        # Handle skip_invalid
        # -------------------
        self._skip_invalid = kwargs.pop('skip_invalid', False)
        self._validate = kwargs.pop('_validate', True)
        

        # Populate data dict with properties
        # ----------------------------------
        self._init_provided('colormodel', arg, colormodel)
        self._init_provided('customdata', arg, customdata)
        self._init_provided('customdatasrc', arg, customdatasrc)
        self._init_provided('dx', arg, dx)
        self._init_provided('dy', arg, dy)
        self._init_provided('hoverinfo', arg, hoverinfo)
        self._init_provided('hoverinfosrc', arg, hoverinfosrc)
        self._init_provided('hoverlabel', arg, hoverlabel)
        self._init_provided('hovertemplate', arg, hovertemplate)
        self._init_provided('hovertemplatesrc', arg, hovertemplatesrc)
        self._init_provided('hovertext', arg, hovertext)
        self._init_provided('hovertextsrc', arg, hovertextsrc)
        self._init_provided('ids', arg, ids)
        self._init_provided('idssrc', arg, idssrc)
        self._init_provided('legend', arg, legend)
        self._init_provided('legendgrouptitle', arg, legendgrouptitle)
        self._init_provided('legendrank', arg, legendrank)
        self._init_provided('legendwidth', arg, legendwidth)
        self._init_provided('meta', arg, meta)
        self._init_provided('metasrc', arg, metasrc)
        self._init_provided('name', arg, name)
        self._init_provided('opacity', arg, opacity)
        self._init_provided('source', arg, source)
        self._init_provided('stream', arg, stream)
        self._init_provided('text', arg, text)
        self._init_provided('textsrc', arg, textsrc)
        self._init_provided('uid', arg, uid)
        self._init_provided('uirevision', arg, uirevision)
        self._init_provided('visible', arg, visible)
        self._init_provided('x0', arg, x0)
        self._init_provided('xaxis', arg, xaxis)
        self._init_provided('y0', arg, y0)
        self._init_provided('yaxis', arg, yaxis)
        self._init_provided('z', arg, z)
        self._init_provided('zmax', arg, zmax)
        self._init_provided('zmin', arg, zmin)
        self._init_provided('zorder', arg, zorder)
        self._init_provided('zsmooth', arg, zsmooth)
        self._init_provided('zsrc', arg, zsrc)

        # Read-only literals
        # ------------------

        self._props['type'] = 'image'
        arg.pop('type', None)

        # Process unknown kwargs
        # ----------------------
        self._process_kwargs(**dict(arg, **kwargs))

        # Reset skip_invalid
        # ------------------
        self._skip_invalid = False
