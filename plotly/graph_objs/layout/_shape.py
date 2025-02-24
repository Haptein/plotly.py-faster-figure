from __future__ import annotations
from typing import Any
from numpy.typing import NDArray
from plotly.basedatatypes import BaseLayoutHierarchyType as _BaseLayoutHierarchyType
import copy as _copy


class Shape(_BaseLayoutHierarchyType):

    _parent_path_str = "layout"
    _path_str = "layout.shape"
    _valid_props = {
        "editable",
        "fillcolor",
        "fillrule",
        "label",
        "layer",
        "legend",
        "legendgroup",
        "legendgrouptitle",
        "legendrank",
        "legendwidth",
        "line",
        "name",
        "opacity",
        "path",
        "showlegend",
        "templateitemname",
        "type",
        "visible",
        "x0",
        "x0shift",
        "x1",
        "x1shift",
        "xanchor",
        "xref",
        "xsizemode",
        "y0",
        "y0shift",
        "y1",
        "y1shift",
        "yanchor",
        "yref",
        "ysizemode",
    }

    @property
    def editable(self):
        """
        Determines whether the shape could be activated for edit or
        not. Has no effect when the older editable shapes mode is
        enabled via `config.editable` or `config.edits.shapePosition`.

        The 'editable' property must be specified as a bool
        (either True, or False)

        Returns
        -------
        bool
        """
        return self["editable"]

    @editable.setter
    def editable(self, val):
        self["editable"] = val

    @property
    def fillcolor(self):
        """
        Sets the color filling the shape's interior. Only applies to
        closed shapes.

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
    def fillrule(self):
        """
        Determines which regions of complex paths constitute the
        interior. For more info please visit
        https://developer.mozilla.org/en-
        US/docs/Web/SVG/Attribute/fill-rule

        The 'fillrule' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['evenodd', 'nonzero']

        Returns
        -------
        Any
        """
        return self["fillrule"]

    @fillrule.setter
    def fillrule(self, val):
        self["fillrule"] = val

    @property
    def label(self):
        """
        The 'label' property is an instance of Label
        that may be specified as:
          - An instance of :class:`plotly.graph_objs.layout.shape.Label`
          - A dict of string/value properties that will be passed
            to the Label constructor

        Returns
        -------
        plotly.graph_objs.layout.shape.Label
        """
        return self["label"]

    @label.setter
    def label(self, val):
        self["label"] = val

    @property
    def layer(self):
        """
        Specifies whether shapes are drawn below gridlines ("below"),
        between gridlines and traces ("between") or above traces
        ("above").

        The 'layer' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['below', 'above', 'between']

        Returns
        -------
        Any
        """
        return self["layer"]

    @layer.setter
    def layer(self, val):
        self["layer"] = val

    @property
    def legend(self):
        """
        Sets the reference to a legend to show this shape in.
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
        Sets the legend group for this shape. Traces and shapes part of
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
          - An instance of :class:`plotly.graph_objs.layout.shape.Legendgrouptitle`
          - A dict of string/value properties that will be passed
            to the Legendgrouptitle constructor

        Returns
        -------
        plotly.graph_objs.layout.shape.Legendgrouptitle
        """
        return self["legendgrouptitle"]

    @legendgrouptitle.setter
    def legendgrouptitle(self, val):
        self["legendgrouptitle"] = val

    @property
    def legendrank(self):
        """
        Sets the legend rank for this shape. Items and groups with
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
        shape.

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
          - An instance of :class:`plotly.graph_objs.layout.shape.Line`
          - A dict of string/value properties that will be passed
            to the Line constructor

        Returns
        -------
        plotly.graph_objs.layout.shape.Line
        """
        return self["line"]

    @line.setter
    def line(self, val):
        self["line"] = val

    @property
    def name(self):
        """
        When used in a template, named items are created in the output
        figure in addition to any items the figure already has in this
        array. You can modify these items in the output figure by
        making your own item with `templateitemname` matching this
        `name` alongside your modifications (including `visible: false`
        or `enabled: false` to hide it). Has no effect outside of a
        template.

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
        Sets the opacity of the shape.

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
    def path(self):
        """
        For `type` "path" - a valid SVG path with the pixel values
        replaced by data values in `xsizemode`/`ysizemode` being
        "scaled" and taken unmodified as pixels relative to `xanchor`
        and `yanchor` in case of "pixel" size mode. There are a few
        restrictions / quirks only absolute instructions, not relative.
        So the allowed segments are: M, L, H, V, Q, C, T, S, and Z arcs
        (A) are not allowed because radius rx and ry are relative. In
        the future we could consider supporting relative commands, but
        we would have to decide on how to handle date and log axes.
        Note that even as is, Q and C Bezier paths that are smooth on
        linear axes may not be smooth on log, and vice versa. no
        chained "polybezier" commands - specify the segment type for
        each one. On category axes, values are numbers scaled to the
        serial numbers of categories because using the categories
        themselves there would be no way to describe fractional
        positions On data axes: because space and T are both normal
        components of path strings, we can't use either to separate
        date from time parts. Therefore we'll use underscore for this
        purpose: 2015-02-21_13:45:56.789

        The 'path' property is a string and must be specified as:
          - A string
          - A number that will be converted to a string

        Returns
        -------
        str
        """
        return self["path"]

    @path.setter
    def path(self, val):
        self["path"] = val

    @property
    def showlegend(self):
        """
        Determines whether or not this shape is shown in the legend.

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
    def templateitemname(self):
        """
        Used to refer to a named item in this array in the template.
        Named items from the template will be created even without a
        matching item in the input figure, but you can modify one by
        making an item with `templateitemname` matching its `name`,
        alongside your modifications (including `visible: false` or
        `enabled: false` to hide it). If there is no template or no
        matching item, this item will be hidden unless you explicitly
        show it with `visible: true`.

        The 'templateitemname' property is a string and must be specified as:
          - A string
          - A number that will be converted to a string

        Returns
        -------
        str
        """
        return self["templateitemname"]

    @templateitemname.setter
    def templateitemname(self, val):
        self["templateitemname"] = val

    @property
    def type(self):
        """
        Specifies the shape type to be drawn. If "line", a line is
        drawn from (`x0`,`y0`) to (`x1`,`y1`) with respect to the axes'
        sizing mode. If "circle", a circle is drawn from
        ((`x0`+`x1`)/2, (`y0`+`y1`)/2)) with radius (|(`x0`+`x1`)/2 -
        `x0`|, |(`y0`+`y1`)/2 -`y0`)|) with respect to the axes' sizing
        mode. If "rect", a rectangle is drawn linking (`x0`,`y0`),
        (`x1`,`y0`), (`x1`,`y1`), (`x0`,`y1`), (`x0`,`y0`) with respect
        to the axes' sizing mode. If "path", draw a custom SVG path
        using `path`. with respect to the axes' sizing mode.

        The 'type' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['circle', 'rect', 'path', 'line']

        Returns
        -------
        Any
        """
        return self["type"]

    @type.setter
    def type(self, val):
        self["type"] = val

    @property
    def visible(self):
        """
        Determines whether or not this shape is visible. If
        "legendonly", the shape is not drawn, but can appear as a
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
    def x0(self):
        """
        Sets the shape's starting x position. See `type` and
        `xsizemode` for more info.

        The 'x0' property accepts values of any type

        Returns
        -------
        Any
        """
        return self["x0"]

    @x0.setter
    def x0(self, val):
        self["x0"] = val

    @property
    def x0shift(self):
        """
        Shifts `x0` away from the center of the category when `xref` is
        a "category" or "multicategory" axis. -0.5 corresponds to the
        start of the category and 0.5 corresponds to the end of the
        category.

        The 'x0shift' property is a number and may be specified as:
          - An int or float in the interval [-1, 1]

        Returns
        -------
        int|float
        """
        return self["x0shift"]

    @x0shift.setter
    def x0shift(self, val):
        self["x0shift"] = val

    @property
    def x1(self):
        """
        Sets the shape's end x position. See `type` and `xsizemode` for
        more info.

        The 'x1' property accepts values of any type

        Returns
        -------
        Any
        """
        return self["x1"]

    @x1.setter
    def x1(self, val):
        self["x1"] = val

    @property
    def x1shift(self):
        """
        Shifts `x1` away from the center of the category when `xref` is
        a "category" or "multicategory" axis. -0.5 corresponds to the
        start of the category and 0.5 corresponds to the end of the
        category.

        The 'x1shift' property is a number and may be specified as:
          - An int or float in the interval [-1, 1]

        Returns
        -------
        int|float
        """
        return self["x1shift"]

    @x1shift.setter
    def x1shift(self, val):
        self["x1shift"] = val

    @property
    def xanchor(self):
        """
        Only relevant in conjunction with `xsizemode` set to "pixel".
        Specifies the anchor point on the x axis to which `x0`, `x1`
        and x coordinates within `path` are relative to. E.g. useful to
        attach a pixel sized shape to a certain data value. No effect
        when `xsizemode` not set to "pixel".

        The 'xanchor' property accepts values of any type

        Returns
        -------
        Any
        """
        return self["xanchor"]

    @xanchor.setter
    def xanchor(self, val):
        self["xanchor"] = val

    @property
    def xref(self):
        """
        Sets the shape's x coordinate axis. If set to a x axis id (e.g.
        "x" or "x2"), the `x` position refers to a x coordinate. If set
        to "paper", the `x` position refers to the distance from the
        left of the plotting area in normalized coordinates where 0 (1)
        corresponds to the left (right). If set to a x axis ID followed
        by "domain" (separated by a space), the position behaves like
        for "paper", but refers to the distance in fractions of the
        domain length from the left of the domain of that axis: e.g.,
        *x2 domain* refers to the domain of the second x  axis and a x
        position of 0.5 refers to the point between the left and the
        right of the domain of the second x axis.

        The 'xref' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['paper']
          - A string that matches one of the following regular expressions:
                ['^x([2-9]|[1-9][0-9]+)?( domain)?$']

        Returns
        -------
        Any
        """
        return self["xref"]

    @xref.setter
    def xref(self, val):
        self["xref"] = val

    @property
    def xsizemode(self):
        """
        Sets the shapes's sizing mode along the x axis. If set to
        "scaled", `x0`, `x1` and x coordinates within `path` refer to
        data values on the x axis or a fraction of the plot area's
        width (`xref` set to "paper"). If set to "pixel", `xanchor`
        specifies the x position in terms of data or plot fraction but
        `x0`, `x1` and x coordinates within `path` are pixels relative
        to `xanchor`. This way, the shape can have a fixed width while
        maintaining a position relative to data or plot fraction.

        The 'xsizemode' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['scaled', 'pixel']

        Returns
        -------
        Any
        """
        return self["xsizemode"]

    @xsizemode.setter
    def xsizemode(self, val):
        self["xsizemode"] = val

    @property
    def y0(self):
        """
        Sets the shape's starting y position. See `type` and
        `ysizemode` for more info.

        The 'y0' property accepts values of any type

        Returns
        -------
        Any
        """
        return self["y0"]

    @y0.setter
    def y0(self, val):
        self["y0"] = val

    @property
    def y0shift(self):
        """
        Shifts `y0` away from the center of the category when `yref` is
        a "category" or "multicategory" axis. -0.5 corresponds to the
        start of the category and 0.5 corresponds to the end of the
        category.

        The 'y0shift' property is a number and may be specified as:
          - An int or float in the interval [-1, 1]

        Returns
        -------
        int|float
        """
        return self["y0shift"]

    @y0shift.setter
    def y0shift(self, val):
        self["y0shift"] = val

    @property
    def y1(self):
        """
        Sets the shape's end y position. See `type` and `ysizemode` for
        more info.

        The 'y1' property accepts values of any type

        Returns
        -------
        Any
        """
        return self["y1"]

    @y1.setter
    def y1(self, val):
        self["y1"] = val

    @property
    def y1shift(self):
        """
        Shifts `y1` away from the center of the category when `yref` is
        a "category" or "multicategory" axis. -0.5 corresponds to the
        start of the category and 0.5 corresponds to the end of the
        category.

        The 'y1shift' property is a number and may be specified as:
          - An int or float in the interval [-1, 1]

        Returns
        -------
        int|float
        """
        return self["y1shift"]

    @y1shift.setter
    def y1shift(self, val):
        self["y1shift"] = val

    @property
    def yanchor(self):
        """
        Only relevant in conjunction with `ysizemode` set to "pixel".
        Specifies the anchor point on the y axis to which `y0`, `y1`
        and y coordinates within `path` are relative to. E.g. useful to
        attach a pixel sized shape to a certain data value. No effect
        when `ysizemode` not set to "pixel".

        The 'yanchor' property accepts values of any type

        Returns
        -------
        Any
        """
        return self["yanchor"]

    @yanchor.setter
    def yanchor(self, val):
        self["yanchor"] = val

    @property
    def yref(self):
        """
        Sets the shape's y coordinate axis. If set to a y axis id (e.g.
        "y" or "y2"), the `y` position refers to a y coordinate. If set
        to "paper", the `y` position refers to the distance from the
        bottom of the plotting area in normalized coordinates where 0
        (1) corresponds to the bottom (top). If set to a y axis ID
        followed by "domain" (separated by a space), the position
        behaves like for "paper", but refers to the distance in
        fractions of the domain length from the bottom of the domain of
        that axis: e.g., *y2 domain* refers to the domain of the second
        y  axis and a y position of 0.5 refers to the point between the
        bottom and the top of the domain of the second y axis.

        The 'yref' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['paper']
          - A string that matches one of the following regular expressions:
                ['^y([2-9]|[1-9][0-9]+)?( domain)?$']

        Returns
        -------
        Any
        """
        return self["yref"]

    @yref.setter
    def yref(self, val):
        self["yref"] = val

    @property
    def ysizemode(self):
        """
        Sets the shapes's sizing mode along the y axis. If set to
        "scaled", `y0`, `y1` and y coordinates within `path` refer to
        data values on the y axis or a fraction of the plot area's
        height (`yref` set to "paper"). If set to "pixel", `yanchor`
        specifies the y position in terms of data or plot fraction but
        `y0`, `y1` and y coordinates within `path` are pixels relative
        to `yanchor`. This way, the shape can have a fixed height while
        maintaining a position relative to data or plot fraction.

        The 'ysizemode' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['scaled', 'pixel']

        Returns
        -------
        Any
        """
        return self["ysizemode"]

    @ysizemode.setter
    def ysizemode(self, val):
        self["ysizemode"] = val

    @property
    def _prop_descriptions(self):
        return """\
        editable
            Determines whether the shape could be activated for
            edit or not. Has no effect when the older editable
            shapes mode is enabled via `config.editable` or
            `config.edits.shapePosition`.
        fillcolor
            Sets the color filling the shape's interior. Only
            applies to closed shapes.
        fillrule
            Determines which regions of complex paths constitute
            the interior. For more info please visit
            https://developer.mozilla.org/en-
            US/docs/Web/SVG/Attribute/fill-rule
        label
            :class:`plotly.graph_objects.layout.shape.Label`
            instance or dict with compatible properties
        layer
            Specifies whether shapes are drawn below gridlines
            ("below"), between gridlines and traces ("between") or
            above traces ("above").
        legend
            Sets the reference to a legend to show this shape in.
            References to these legends are "legend", "legend2",
            "legend3", etc. Settings for these legends are set in
            the layout, under `layout.legend`, `layout.legend2`,
            etc.
        legendgroup
            Sets the legend group for this shape. Traces and shapes
            part of the same legend group hide/show at the same
            time when toggling legend items.
        legendgrouptitle
            :class:`plotly.graph_objects.layout.shape.Legendgroupti
            tle` instance or dict with compatible properties
        legendrank
            Sets the legend rank for this shape. Items and groups
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
            this shape.
        line
            :class:`plotly.graph_objects.layout.shape.Line`
            instance or dict with compatible properties
        name
            When used in a template, named items are created in the
            output figure in addition to any items the figure
            already has in this array. You can modify these items
            in the output figure by making your own item with
            `templateitemname` matching this `name` alongside your
            modifications (including `visible: false` or `enabled:
            false` to hide it). Has no effect outside of a
            template.
        opacity
            Sets the opacity of the shape.
        path
            For `type` "path" - a valid SVG path with the pixel
            values replaced by data values in
            `xsizemode`/`ysizemode` being "scaled" and taken
            unmodified as pixels relative to `xanchor` and
            `yanchor` in case of "pixel" size mode. There are a few
            restrictions / quirks only absolute instructions, not
            relative. So the allowed segments are: M, L, H, V, Q,
            C, T, S, and Z arcs (A) are not allowed because radius
            rx and ry are relative. In the future we could consider
            supporting relative commands, but we would have to
            decide on how to handle date and log axes. Note that
            even as is, Q and C Bezier paths that are smooth on
            linear axes may not be smooth on log, and vice versa.
            no chained "polybezier" commands - specify the segment
            type for each one. On category axes, values are numbers
            scaled to the serial numbers of categories because
            using the categories themselves there would be no way
            to describe fractional positions On data axes: because
            space and T are both normal components of path strings,
            we can't use either to separate date from time parts.
            Therefore we'll use underscore for this purpose:
            2015-02-21_13:45:56.789
        showlegend
            Determines whether or not this shape is shown in the
            legend.
        templateitemname
            Used to refer to a named item in this array in the
            template. Named items from the template will be created
            even without a matching item in the input figure, but
            you can modify one by making an item with
            `templateitemname` matching its `name`, alongside your
            modifications (including `visible: false` or `enabled:
            false` to hide it). If there is no template or no
            matching item, this item will be hidden unless you
            explicitly show it with `visible: true`.
        type
            Specifies the shape type to be drawn. If "line", a line
            is drawn from (`x0`,`y0`) to (`x1`,`y1`) with respect
            to the axes' sizing mode. If "circle", a circle is
            drawn from ((`x0`+`x1`)/2, (`y0`+`y1`)/2)) with radius
            (|(`x0`+`x1`)/2 - `x0`|, |(`y0`+`y1`)/2 -`y0`)|) with
            respect to the axes' sizing mode. If "rect", a
            rectangle is drawn linking (`x0`,`y0`), (`x1`,`y0`),
            (`x1`,`y1`), (`x0`,`y1`), (`x0`,`y0`) with respect to
            the axes' sizing mode. If "path", draw a custom SVG
            path using `path`. with respect to the axes' sizing
            mode.
        visible
            Determines whether or not this shape is visible. If
            "legendonly", the shape is not drawn, but can appear as
            a legend item (provided that the legend itself is
            visible).
        x0
            Sets the shape's starting x position. See `type` and
            `xsizemode` for more info.
        x0shift
            Shifts `x0` away from the center of the category when
            `xref` is a "category" or "multicategory" axis. -0.5
            corresponds to the start of the category and 0.5
            corresponds to the end of the category.
        x1
            Sets the shape's end x position. See `type` and
            `xsizemode` for more info.
        x1shift
            Shifts `x1` away from the center of the category when
            `xref` is a "category" or "multicategory" axis. -0.5
            corresponds to the start of the category and 0.5
            corresponds to the end of the category.
        xanchor
            Only relevant in conjunction with `xsizemode` set to
            "pixel". Specifies the anchor point on the x axis to
            which `x0`, `x1` and x coordinates within `path` are
            relative to. E.g. useful to attach a pixel sized shape
            to a certain data value. No effect when `xsizemode` not
            set to "pixel".
        xref
            Sets the shape's x coordinate axis. If set to a x axis
            id (e.g. "x" or "x2"), the `x` position refers to a x
            coordinate. If set to "paper", the `x` position refers
            to the distance from the left of the plotting area in
            normalized coordinates where 0 (1) corresponds to the
            left (right). If set to a x axis ID followed by
            "domain" (separated by a space), the position behaves
            like for "paper", but refers to the distance in
            fractions of the domain length from the left of the
            domain of that axis: e.g., *x2 domain* refers to the
            domain of the second x  axis and a x position of 0.5
            refers to the point between the left and the right of
            the domain of the second x axis.
        xsizemode
            Sets the shapes's sizing mode along the x axis. If set
            to "scaled", `x0`, `x1` and x coordinates within `path`
            refer to data values on the x axis or a fraction of the
            plot area's width (`xref` set to "paper"). If set to
            "pixel", `xanchor` specifies the x position in terms of
            data or plot fraction but `x0`, `x1` and x coordinates
            within `path` are pixels relative to `xanchor`. This
            way, the shape can have a fixed width while maintaining
            a position relative to data or plot fraction.
        y0
            Sets the shape's starting y position. See `type` and
            `ysizemode` for more info.
        y0shift
            Shifts `y0` away from the center of the category when
            `yref` is a "category" or "multicategory" axis. -0.5
            corresponds to the start of the category and 0.5
            corresponds to the end of the category.
        y1
            Sets the shape's end y position. See `type` and
            `ysizemode` for more info.
        y1shift
            Shifts `y1` away from the center of the category when
            `yref` is a "category" or "multicategory" axis. -0.5
            corresponds to the start of the category and 0.5
            corresponds to the end of the category.
        yanchor
            Only relevant in conjunction with `ysizemode` set to
            "pixel". Specifies the anchor point on the y axis to
            which `y0`, `y1` and y coordinates within `path` are
            relative to. E.g. useful to attach a pixel sized shape
            to a certain data value. No effect when `ysizemode` not
            set to "pixel".
        yref
            Sets the shape's y coordinate axis. If set to a y axis
            id (e.g. "y" or "y2"), the `y` position refers to a y
            coordinate. If set to "paper", the `y` position refers
            to the distance from the bottom of the plotting area in
            normalized coordinates where 0 (1) corresponds to the
            bottom (top). If set to a y axis ID followed by
            "domain" (separated by a space), the position behaves
            like for "paper", but refers to the distance in
            fractions of the domain length from the bottom of the
            domain of that axis: e.g., *y2 domain* refers to the
            domain of the second y  axis and a y position of 0.5
            refers to the point between the bottom and the top of
            the domain of the second y axis.
        ysizemode
            Sets the shapes's sizing mode along the y axis. If set
            to "scaled", `y0`, `y1` and y coordinates within `path`
            refer to data values on the y axis or a fraction of the
            plot area's height (`yref` set to "paper"). If set to
            "pixel", `yanchor` specifies the y position in terms of
            data or plot fraction but `y0`, `y1` and y coordinates
            within `path` are pixels relative to `yanchor`. This
            way, the shape can have a fixed height while
            maintaining a position relative to data or plot
            fraction.
        """

    def __init__(
        self,
        arg=None,
        editable: bool | None = None,
        fillcolor: str | None = None,
        fillrule: Any | None = None,
        label: None | None = None,
        layer: Any | None = None,
        legend: str | None = None,
        legendgroup: str | None = None,
        legendgrouptitle: None | None = None,
        legendrank: int | float | None = None,
        legendwidth: int | float | None = None,
        line: None | None = None,
        name: str | None = None,
        opacity: int | float | None = None,
        path: str | None = None,
        showlegend: bool | None = None,
        templateitemname: str | None = None,
        type: Any | None = None,
        visible: Any | None = None,
        x0: Any | None = None,
        x0shift: int | float | None = None,
        x1: Any | None = None,
        x1shift: int | float | None = None,
        xanchor: Any | None = None,
        xref: Any | None = None,
        xsizemode: Any | None = None,
        y0: Any | None = None,
        y0shift: int | float | None = None,
        y1: Any | None = None,
        y1shift: int | float | None = None,
        yanchor: Any | None = None,
        yref: Any | None = None,
        ysizemode: Any | None = None,
        **kwargs,
    ):
        """
        Construct a new Shape object

        Parameters
        ----------
        arg
            dict of properties compatible with this constructor or
            an instance of :class:`plotly.graph_objs.layout.Shape`
        editable
            Determines whether the shape could be activated for
            edit or not. Has no effect when the older editable
            shapes mode is enabled via `config.editable` or
            `config.edits.shapePosition`.
        fillcolor
            Sets the color filling the shape's interior. Only
            applies to closed shapes.
        fillrule
            Determines which regions of complex paths constitute
            the interior. For more info please visit
            https://developer.mozilla.org/en-
            US/docs/Web/SVG/Attribute/fill-rule
        label
            :class:`plotly.graph_objects.layout.shape.Label`
            instance or dict with compatible properties
        layer
            Specifies whether shapes are drawn below gridlines
            ("below"), between gridlines and traces ("between") or
            above traces ("above").
        legend
            Sets the reference to a legend to show this shape in.
            References to these legends are "legend", "legend2",
            "legend3", etc. Settings for these legends are set in
            the layout, under `layout.legend`, `layout.legend2`,
            etc.
        legendgroup
            Sets the legend group for this shape. Traces and shapes
            part of the same legend group hide/show at the same
            time when toggling legend items.
        legendgrouptitle
            :class:`plotly.graph_objects.layout.shape.Legendgroupti
            tle` instance or dict with compatible properties
        legendrank
            Sets the legend rank for this shape. Items and groups
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
            this shape.
        line
            :class:`plotly.graph_objects.layout.shape.Line`
            instance or dict with compatible properties
        name
            When used in a template, named items are created in the
            output figure in addition to any items the figure
            already has in this array. You can modify these items
            in the output figure by making your own item with
            `templateitemname` matching this `name` alongside your
            modifications (including `visible: false` or `enabled:
            false` to hide it). Has no effect outside of a
            template.
        opacity
            Sets the opacity of the shape.
        path
            For `type` "path" - a valid SVG path with the pixel
            values replaced by data values in
            `xsizemode`/`ysizemode` being "scaled" and taken
            unmodified as pixels relative to `xanchor` and
            `yanchor` in case of "pixel" size mode. There are a few
            restrictions / quirks only absolute instructions, not
            relative. So the allowed segments are: M, L, H, V, Q,
            C, T, S, and Z arcs (A) are not allowed because radius
            rx and ry are relative. In the future we could consider
            supporting relative commands, but we would have to
            decide on how to handle date and log axes. Note that
            even as is, Q and C Bezier paths that are smooth on
            linear axes may not be smooth on log, and vice versa.
            no chained "polybezier" commands - specify the segment
            type for each one. On category axes, values are numbers
            scaled to the serial numbers of categories because
            using the categories themselves there would be no way
            to describe fractional positions On data axes: because
            space and T are both normal components of path strings,
            we can't use either to separate date from time parts.
            Therefore we'll use underscore for this purpose:
            2015-02-21_13:45:56.789
        showlegend
            Determines whether or not this shape is shown in the
            legend.
        templateitemname
            Used to refer to a named item in this array in the
            template. Named items from the template will be created
            even without a matching item in the input figure, but
            you can modify one by making an item with
            `templateitemname` matching its `name`, alongside your
            modifications (including `visible: false` or `enabled:
            false` to hide it). If there is no template or no
            matching item, this item will be hidden unless you
            explicitly show it with `visible: true`.
        type
            Specifies the shape type to be drawn. If "line", a line
            is drawn from (`x0`,`y0`) to (`x1`,`y1`) with respect
            to the axes' sizing mode. If "circle", a circle is
            drawn from ((`x0`+`x1`)/2, (`y0`+`y1`)/2)) with radius
            (|(`x0`+`x1`)/2 - `x0`|, |(`y0`+`y1`)/2 -`y0`)|) with
            respect to the axes' sizing mode. If "rect", a
            rectangle is drawn linking (`x0`,`y0`), (`x1`,`y0`),
            (`x1`,`y1`), (`x0`,`y1`), (`x0`,`y0`) with respect to
            the axes' sizing mode. If "path", draw a custom SVG
            path using `path`. with respect to the axes' sizing
            mode.
        visible
            Determines whether or not this shape is visible. If
            "legendonly", the shape is not drawn, but can appear as
            a legend item (provided that the legend itself is
            visible).
        x0
            Sets the shape's starting x position. See `type` and
            `xsizemode` for more info.
        x0shift
            Shifts `x0` away from the center of the category when
            `xref` is a "category" or "multicategory" axis. -0.5
            corresponds to the start of the category and 0.5
            corresponds to the end of the category.
        x1
            Sets the shape's end x position. See `type` and
            `xsizemode` for more info.
        x1shift
            Shifts `x1` away from the center of the category when
            `xref` is a "category" or "multicategory" axis. -0.5
            corresponds to the start of the category and 0.5
            corresponds to the end of the category.
        xanchor
            Only relevant in conjunction with `xsizemode` set to
            "pixel". Specifies the anchor point on the x axis to
            which `x0`, `x1` and x coordinates within `path` are
            relative to. E.g. useful to attach a pixel sized shape
            to a certain data value. No effect when `xsizemode` not
            set to "pixel".
        xref
            Sets the shape's x coordinate axis. If set to a x axis
            id (e.g. "x" or "x2"), the `x` position refers to a x
            coordinate. If set to "paper", the `x` position refers
            to the distance from the left of the plotting area in
            normalized coordinates where 0 (1) corresponds to the
            left (right). If set to a x axis ID followed by
            "domain" (separated by a space), the position behaves
            like for "paper", but refers to the distance in
            fractions of the domain length from the left of the
            domain of that axis: e.g., *x2 domain* refers to the
            domain of the second x  axis and a x position of 0.5
            refers to the point between the left and the right of
            the domain of the second x axis.
        xsizemode
            Sets the shapes's sizing mode along the x axis. If set
            to "scaled", `x0`, `x1` and x coordinates within `path`
            refer to data values on the x axis or a fraction of the
            plot area's width (`xref` set to "paper"). If set to
            "pixel", `xanchor` specifies the x position in terms of
            data or plot fraction but `x0`, `x1` and x coordinates
            within `path` are pixels relative to `xanchor`. This
            way, the shape can have a fixed width while maintaining
            a position relative to data or plot fraction.
        y0
            Sets the shape's starting y position. See `type` and
            `ysizemode` for more info.
        y0shift
            Shifts `y0` away from the center of the category when
            `yref` is a "category" or "multicategory" axis. -0.5
            corresponds to the start of the category and 0.5
            corresponds to the end of the category.
        y1
            Sets the shape's end y position. See `type` and
            `ysizemode` for more info.
        y1shift
            Shifts `y1` away from the center of the category when
            `yref` is a "category" or "multicategory" axis. -0.5
            corresponds to the start of the category and 0.5
            corresponds to the end of the category.
        yanchor
            Only relevant in conjunction with `ysizemode` set to
            "pixel". Specifies the anchor point on the y axis to
            which `y0`, `y1` and y coordinates within `path` are
            relative to. E.g. useful to attach a pixel sized shape
            to a certain data value. No effect when `ysizemode` not
            set to "pixel".
        yref
            Sets the shape's y coordinate axis. If set to a y axis
            id (e.g. "y" or "y2"), the `y` position refers to a y
            coordinate. If set to "paper", the `y` position refers
            to the distance from the bottom of the plotting area in
            normalized coordinates where 0 (1) corresponds to the
            bottom (top). If set to a y axis ID followed by
            "domain" (separated by a space), the position behaves
            like for "paper", but refers to the distance in
            fractions of the domain length from the bottom of the
            domain of that axis: e.g., *y2 domain* refers to the
            domain of the second y  axis and a y position of 0.5
            refers to the point between the bottom and the top of
            the domain of the second y axis.
        ysizemode
            Sets the shapes's sizing mode along the y axis. If set
            to "scaled", `y0`, `y1` and y coordinates within `path`
            refer to data values on the y axis or a fraction of the
            plot area's height (`yref` set to "paper"). If set to
            "pixel", `yanchor` specifies the y position in terms of
            data or plot fraction but `y0`, `y1` and y coordinates
            within `path` are pixels relative to `yanchor`. This
            way, the shape can have a fixed height while
            maintaining a position relative to data or plot
            fraction.

        Returns
        -------
        Shape
        """
        super().__init__("shapes")
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
The first argument to the plotly.graph_objs.layout.Shape
constructor must be a dict or
an instance of :class:`plotly.graph_objs.layout.Shape`"""
            )

        self._skip_invalid = kwargs.pop("skip_invalid", False)
        self._validate = kwargs.pop("_validate", True)

        self._init_provided("editable", arg, editable)
        self._init_provided("fillcolor", arg, fillcolor)
        self._init_provided("fillrule", arg, fillrule)
        self._init_provided("label", arg, label)
        self._init_provided("layer", arg, layer)
        self._init_provided("legend", arg, legend)
        self._init_provided("legendgroup", arg, legendgroup)
        self._init_provided("legendgrouptitle", arg, legendgrouptitle)
        self._init_provided("legendrank", arg, legendrank)
        self._init_provided("legendwidth", arg, legendwidth)
        self._init_provided("line", arg, line)
        self._init_provided("name", arg, name)
        self._init_provided("opacity", arg, opacity)
        self._init_provided("path", arg, path)
        self._init_provided("showlegend", arg, showlegend)
        self._init_provided("templateitemname", arg, templateitemname)
        self._init_provided("type", arg, type)
        self._init_provided("visible", arg, visible)
        self._init_provided("x0", arg, x0)
        self._init_provided("x0shift", arg, x0shift)
        self._init_provided("x1", arg, x1)
        self._init_provided("x1shift", arg, x1shift)
        self._init_provided("xanchor", arg, xanchor)
        self._init_provided("xref", arg, xref)
        self._init_provided("xsizemode", arg, xsizemode)
        self._init_provided("y0", arg, y0)
        self._init_provided("y0shift", arg, y0shift)
        self._init_provided("y1", arg, y1)
        self._init_provided("y1shift", arg, y1shift)
        self._init_provided("yanchor", arg, yanchor)
        self._init_provided("yref", arg, yref)
        self._init_provided("ysizemode", arg, ysizemode)
        self._process_kwargs(**dict(arg, **kwargs))
        self._skip_invalid = False
