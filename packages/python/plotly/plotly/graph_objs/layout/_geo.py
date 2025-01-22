

from plotly.basedatatypes import BaseLayoutHierarchyType as _BaseLayoutHierarchyType
import copy as _copy


class Geo(_BaseLayoutHierarchyType):

    # class properties
    # --------------------
    _parent_path_str = 'layout'
    _path_str = 'layout.geo'
    _valid_props = {"bgcolor", "center", "coastlinecolor", "coastlinewidth", "countrycolor", "countrywidth", "domain", "fitbounds", "framecolor", "framewidth", "lakecolor", "landcolor", "lataxis", "lonaxis", "oceancolor", "projection", "resolution", "rivercolor", "riverwidth", "scope", "showcoastlines", "showcountries", "showframe", "showlakes", "showland", "showocean", "showrivers", "showsubunits", "subunitcolor", "subunitwidth", "uirevision", "visible"}

    # bgcolor
    # -------
    @property
    def bgcolor(self):
        """
        Set the background color of the map

        The 'bgcolor' property is a color and may be specified as:
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

        Returns
        -------
        str
        """
        return self['bgcolor']

    @bgcolor.setter
    def bgcolor(self, val):
        self['bgcolor'] = val

    # center
    # ------
    @property
    def center(self):
        """
        The 'center' property is an instance of Center
        that may be specified as:
          - An instance of :class:`plotly.graph_objs.layout.geo.Center`
          - A dict of string/value properties that will be passed
            to the Center constructor
    
            Supported dict properties:
                
                lat
                    Sets the latitude of the map's center. For all
                    projection types, the map's latitude center
                    lies at the middle of the latitude range by
                    default.
                lon
                    Sets the longitude of the map's center. By
                    default, the map's longitude center lies at the
                    middle of the longitude range for scoped
                    projection and above `projection.rotation.lon`
                    otherwise.

        Returns
        -------
        plotly.graph_objs.layout.geo.Center
        """
        return self['center']

    @center.setter
    def center(self, val):
        self['center'] = val

    # coastlinecolor
    # --------------
    @property
    def coastlinecolor(self):
        """
        Sets the coastline color.

        The 'coastlinecolor' property is a color and may be specified as:
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

        Returns
        -------
        str
        """
        return self['coastlinecolor']

    @coastlinecolor.setter
    def coastlinecolor(self, val):
        self['coastlinecolor'] = val

    # coastlinewidth
    # --------------
    @property
    def coastlinewidth(self):
        """
        Sets the coastline stroke width (in px).

        The 'coastlinewidth' property is a number and may be specified as:
          - An int or float in the interval [0, inf]

        Returns
        -------
        int|float
        """
        return self['coastlinewidth']

    @coastlinewidth.setter
    def coastlinewidth(self, val):
        self['coastlinewidth'] = val

    # countrycolor
    # ------------
    @property
    def countrycolor(self):
        """
        Sets line color of the country boundaries.

        The 'countrycolor' property is a color and may be specified as:
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

        Returns
        -------
        str
        """
        return self['countrycolor']

    @countrycolor.setter
    def countrycolor(self, val):
        self['countrycolor'] = val

    # countrywidth
    # ------------
    @property
    def countrywidth(self):
        """
        Sets line width (in px) of the country boundaries.

        The 'countrywidth' property is a number and may be specified as:
          - An int or float in the interval [0, inf]

        Returns
        -------
        int|float
        """
        return self['countrywidth']

    @countrywidth.setter
    def countrywidth(self, val):
        self['countrywidth'] = val

    # domain
    # ------
    @property
    def domain(self):
        """
        The 'domain' property is an instance of Domain
        that may be specified as:
          - An instance of :class:`plotly.graph_objs.layout.geo.Domain`
          - A dict of string/value properties that will be passed
            to the Domain constructor
    
            Supported dict properties:
                
                column
                    If there is a layout grid, use the domain for
                    this column in the grid for this geo subplot .
                    Note that geo subplots are constrained by
                    domain. In general, when `projection.scale` is
                    set to 1. a map will fit either its x or y
                    domain, but not both.
                row
                    If there is a layout grid, use the domain for
                    this row in the grid for this geo subplot .
                    Note that geo subplots are constrained by
                    domain. In general, when `projection.scale` is
                    set to 1. a map will fit either its x or y
                    domain, but not both.
                x
                    Sets the horizontal domain of this geo subplot
                    (in plot fraction). Note that geo subplots are
                    constrained by domain. In general, when
                    `projection.scale` is set to 1. a map will fit
                    either its x or y domain, but not both.
                y
                    Sets the vertical domain of this geo subplot
                    (in plot fraction). Note that geo subplots are
                    constrained by domain. In general, when
                    `projection.scale` is set to 1. a map will fit
                    either its x or y domain, but not both.

        Returns
        -------
        plotly.graph_objs.layout.geo.Domain
        """
        return self['domain']

    @domain.setter
    def domain(self, val):
        self['domain'] = val

    # fitbounds
    # ---------
    @property
    def fitbounds(self):
        """
        Determines if this subplot's view settings are auto-computed to
        fit trace data. On scoped maps, setting `fitbounds` leads to
        `center.lon` and `center.lat` getting auto-filled. On maps with
        a non-clipped projection, setting `fitbounds` leads to
        `center.lon`, `center.lat`, and `projection.rotation.lon`
        getting auto-filled. On maps with a clipped projection, setting
        `fitbounds` leads to `center.lon`, `center.lat`,
        `projection.rotation.lon`, `projection.rotation.lat`,
        `lonaxis.range` and `lataxis.range` getting auto-filled. If
        "locations", only the trace's visible locations are considered
        in the `fitbounds` computations. If "geojson", the entire trace
        input `geojson` (if provided) is considered in the `fitbounds`
        computations, Defaults to False.

        The 'fitbounds' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                [False, 'locations', 'geojson']

        Returns
        -------
        Any
        """
        return self['fitbounds']

    @fitbounds.setter
    def fitbounds(self, val):
        self['fitbounds'] = val

    # framecolor
    # ----------
    @property
    def framecolor(self):
        """
        Sets the color the frame.

        The 'framecolor' property is a color and may be specified as:
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

        Returns
        -------
        str
        """
        return self['framecolor']

    @framecolor.setter
    def framecolor(self, val):
        self['framecolor'] = val

    # framewidth
    # ----------
    @property
    def framewidth(self):
        """
        Sets the stroke width (in px) of the frame.

        The 'framewidth' property is a number and may be specified as:
          - An int or float in the interval [0, inf]

        Returns
        -------
        int|float
        """
        return self['framewidth']

    @framewidth.setter
    def framewidth(self, val):
        self['framewidth'] = val

    # lakecolor
    # ---------
    @property
    def lakecolor(self):
        """
        Sets the color of the lakes.

        The 'lakecolor' property is a color and may be specified as:
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

        Returns
        -------
        str
        """
        return self['lakecolor']

    @lakecolor.setter
    def lakecolor(self, val):
        self['lakecolor'] = val

    # landcolor
    # ---------
    @property
    def landcolor(self):
        """
        Sets the land mass color.

        The 'landcolor' property is a color and may be specified as:
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

        Returns
        -------
        str
        """
        return self['landcolor']

    @landcolor.setter
    def landcolor(self, val):
        self['landcolor'] = val

    # lataxis
    # -------
    @property
    def lataxis(self):
        """
        The 'lataxis' property is an instance of Lataxis
        that may be specified as:
          - An instance of :class:`plotly.graph_objs.layout.geo.Lataxis`
          - A dict of string/value properties that will be passed
            to the Lataxis constructor
    
            Supported dict properties:
                
                dtick
                    Sets the graticule's longitude/latitude tick
                    step.
                gridcolor
                    Sets the graticule's stroke color.
                griddash
                    Sets the dash style of lines. Set to a dash
                    type string ("solid", "dot", "dash",
                    "longdash", "dashdot", or "longdashdot") or a
                    dash length list in px (eg "5px,10px,2px,2px").
                gridwidth
                    Sets the graticule's stroke width (in px).
                range
                    Sets the range of this axis (in degrees), sets
                    the map's clipped coordinates.
                showgrid
                    Sets whether or not graticule are shown on the
                    map.
                tick0
                    Sets the graticule's starting tick
                    longitude/latitude.

        Returns
        -------
        plotly.graph_objs.layout.geo.Lataxis
        """
        return self['lataxis']

    @lataxis.setter
    def lataxis(self, val):
        self['lataxis'] = val

    # lonaxis
    # -------
    @property
    def lonaxis(self):
        """
        The 'lonaxis' property is an instance of Lonaxis
        that may be specified as:
          - An instance of :class:`plotly.graph_objs.layout.geo.Lonaxis`
          - A dict of string/value properties that will be passed
            to the Lonaxis constructor
    
            Supported dict properties:
                
                dtick
                    Sets the graticule's longitude/latitude tick
                    step.
                gridcolor
                    Sets the graticule's stroke color.
                griddash
                    Sets the dash style of lines. Set to a dash
                    type string ("solid", "dot", "dash",
                    "longdash", "dashdot", or "longdashdot") or a
                    dash length list in px (eg "5px,10px,2px,2px").
                gridwidth
                    Sets the graticule's stroke width (in px).
                range
                    Sets the range of this axis (in degrees), sets
                    the map's clipped coordinates.
                showgrid
                    Sets whether or not graticule are shown on the
                    map.
                tick0
                    Sets the graticule's starting tick
                    longitude/latitude.

        Returns
        -------
        plotly.graph_objs.layout.geo.Lonaxis
        """
        return self['lonaxis']

    @lonaxis.setter
    def lonaxis(self, val):
        self['lonaxis'] = val

    # oceancolor
    # ----------
    @property
    def oceancolor(self):
        """
        Sets the ocean color

        The 'oceancolor' property is a color and may be specified as:
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

        Returns
        -------
        str
        """
        return self['oceancolor']

    @oceancolor.setter
    def oceancolor(self, val):
        self['oceancolor'] = val

    # projection
    # ----------
    @property
    def projection(self):
        """
        The 'projection' property is an instance of Projection
        that may be specified as:
          - An instance of :class:`plotly.graph_objs.layout.geo.Projection`
          - A dict of string/value properties that will be passed
            to the Projection constructor
    
            Supported dict properties:
                
                distance
                    For satellite projection type only. Sets the
                    distance from the center of the sphere to the
                    point of view as a proportion of the sphere’s
                    radius.
                parallels
                    For conic projection types only. Sets the
                    parallels (tangent, secant) where the cone
                    intersects the sphere.
                rotation
                    :class:`plotly.graph_objects.layout.geo.project
                    ion.Rotation` instance or dict with compatible
                    properties
                scale
                    Zooms in or out on the map view. A scale of 1
                    corresponds to the largest zoom level that fits
                    the map's lon and lat ranges.
                tilt
                    For satellite projection type only. Sets the
                    tilt angle of perspective projection.
                type
                    Sets the projection type.

        Returns
        -------
        plotly.graph_objs.layout.geo.Projection
        """
        return self['projection']

    @projection.setter
    def projection(self, val):
        self['projection'] = val

    # resolution
    # ----------
    @property
    def resolution(self):
        """
        Sets the resolution of the base layers. The values have units
        of km/mm e.g. 110 corresponds to a scale ratio of
        1:110,000,000.

        The 'resolution' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                [110, 50]

        Returns
        -------
        Any
        """
        return self['resolution']

    @resolution.setter
    def resolution(self, val):
        self['resolution'] = val

    # rivercolor
    # ----------
    @property
    def rivercolor(self):
        """
        Sets color of the rivers.

        The 'rivercolor' property is a color and may be specified as:
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

        Returns
        -------
        str
        """
        return self['rivercolor']

    @rivercolor.setter
    def rivercolor(self, val):
        self['rivercolor'] = val

    # riverwidth
    # ----------
    @property
    def riverwidth(self):
        """
        Sets the stroke width (in px) of the rivers.

        The 'riverwidth' property is a number and may be specified as:
          - An int or float in the interval [0, inf]

        Returns
        -------
        int|float
        """
        return self['riverwidth']

    @riverwidth.setter
    def riverwidth(self, val):
        self['riverwidth'] = val

    # scope
    # -----
    @property
    def scope(self):
        """
        Set the scope of the map.

        The 'scope' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['africa', 'asia', 'europe', 'north america', 'south
                america', 'usa', 'world']

        Returns
        -------
        Any
        """
        return self['scope']

    @scope.setter
    def scope(self, val):
        self['scope'] = val

    # showcoastlines
    # --------------
    @property
    def showcoastlines(self):
        """
        Sets whether or not the coastlines are drawn.

        The 'showcoastlines' property must be specified as a bool
        (either True, or False)

        Returns
        -------
        bool
        """
        return self['showcoastlines']

    @showcoastlines.setter
    def showcoastlines(self, val):
        self['showcoastlines'] = val

    # showcountries
    # -------------
    @property
    def showcountries(self):
        """
        Sets whether or not country boundaries are drawn.

        The 'showcountries' property must be specified as a bool
        (either True, or False)

        Returns
        -------
        bool
        """
        return self['showcountries']

    @showcountries.setter
    def showcountries(self, val):
        self['showcountries'] = val

    # showframe
    # ---------
    @property
    def showframe(self):
        """
        Sets whether or not a frame is drawn around the map.

        The 'showframe' property must be specified as a bool
        (either True, or False)

        Returns
        -------
        bool
        """
        return self['showframe']

    @showframe.setter
    def showframe(self, val):
        self['showframe'] = val

    # showlakes
    # ---------
    @property
    def showlakes(self):
        """
        Sets whether or not lakes are drawn.

        The 'showlakes' property must be specified as a bool
        (either True, or False)

        Returns
        -------
        bool
        """
        return self['showlakes']

    @showlakes.setter
    def showlakes(self, val):
        self['showlakes'] = val

    # showland
    # --------
    @property
    def showland(self):
        """
        Sets whether or not land masses are filled in color.

        The 'showland' property must be specified as a bool
        (either True, or False)

        Returns
        -------
        bool
        """
        return self['showland']

    @showland.setter
    def showland(self, val):
        self['showland'] = val

    # showocean
    # ---------
    @property
    def showocean(self):
        """
        Sets whether or not oceans are filled in color.

        The 'showocean' property must be specified as a bool
        (either True, or False)

        Returns
        -------
        bool
        """
        return self['showocean']

    @showocean.setter
    def showocean(self, val):
        self['showocean'] = val

    # showrivers
    # ----------
    @property
    def showrivers(self):
        """
        Sets whether or not rivers are drawn.

        The 'showrivers' property must be specified as a bool
        (either True, or False)

        Returns
        -------
        bool
        """
        return self['showrivers']

    @showrivers.setter
    def showrivers(self, val):
        self['showrivers'] = val

    # showsubunits
    # ------------
    @property
    def showsubunits(self):
        """
        Sets whether or not boundaries of subunits within countries
        (e.g. states, provinces) are drawn.

        The 'showsubunits' property must be specified as a bool
        (either True, or False)

        Returns
        -------
        bool
        """
        return self['showsubunits']

    @showsubunits.setter
    def showsubunits(self, val):
        self['showsubunits'] = val

    # subunitcolor
    # ------------
    @property
    def subunitcolor(self):
        """
        Sets the color of the subunits boundaries.

        The 'subunitcolor' property is a color and may be specified as:
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

        Returns
        -------
        str
        """
        return self['subunitcolor']

    @subunitcolor.setter
    def subunitcolor(self, val):
        self['subunitcolor'] = val

    # subunitwidth
    # ------------
    @property
    def subunitwidth(self):
        """
        Sets the stroke width (in px) of the subunits boundaries.

        The 'subunitwidth' property is a number and may be specified as:
          - An int or float in the interval [0, inf]

        Returns
        -------
        int|float
        """
        return self['subunitwidth']

    @subunitwidth.setter
    def subunitwidth(self, val):
        self['subunitwidth'] = val

    # uirevision
    # ----------
    @property
    def uirevision(self):
        """
        Controls persistence of user-driven changes in the view
        (projection and center). Defaults to `layout.uirevision`.

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
        Sets the default visibility of the base layers.

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

    # Self properties description
    # ---------------------------
    @property
    def _prop_descriptions(self):
        return """\
        bgcolor
            Set the background color of the map
        center
            :class:`plotly.graph_objects.layout.geo.Center`
            instance or dict with compatible properties
        coastlinecolor
            Sets the coastline color.
        coastlinewidth
            Sets the coastline stroke width (in px).
        countrycolor
            Sets line color of the country boundaries.
        countrywidth
            Sets line width (in px) of the country boundaries.
        domain
            :class:`plotly.graph_objects.layout.geo.Domain`
            instance or dict with compatible properties
        fitbounds
            Determines if this subplot's view settings are auto-
            computed to fit trace data. On scoped maps, setting
            `fitbounds` leads to `center.lon` and `center.lat`
            getting auto-filled. On maps with a non-clipped
            projection, setting `fitbounds` leads to `center.lon`,
            `center.lat`, and `projection.rotation.lon` getting
            auto-filled. On maps with a clipped projection, setting
            `fitbounds` leads to `center.lon`, `center.lat`,
            `projection.rotation.lon`, `projection.rotation.lat`,
            `lonaxis.range` and `lataxis.range` getting auto-
            filled. If "locations", only the trace's visible
            locations are considered in the `fitbounds`
            computations. If "geojson", the entire trace input
            `geojson` (if provided) is considered in the
            `fitbounds` computations, Defaults to False.
        framecolor
            Sets the color the frame.
        framewidth
            Sets the stroke width (in px) of the frame.
        lakecolor
            Sets the color of the lakes.
        landcolor
            Sets the land mass color.
        lataxis
            :class:`plotly.graph_objects.layout.geo.Lataxis`
            instance or dict with compatible properties
        lonaxis
            :class:`plotly.graph_objects.layout.geo.Lonaxis`
            instance or dict with compatible properties
        oceancolor
            Sets the ocean color
        projection
            :class:`plotly.graph_objects.layout.geo.Projection`
            instance or dict with compatible properties
        resolution
            Sets the resolution of the base layers. The values have
            units of km/mm e.g. 110 corresponds to a scale ratio of
            1:110,000,000.
        rivercolor
            Sets color of the rivers.
        riverwidth
            Sets the stroke width (in px) of the rivers.
        scope
            Set the scope of the map.
        showcoastlines
            Sets whether or not the coastlines are drawn.
        showcountries
            Sets whether or not country boundaries are drawn.
        showframe
            Sets whether or not a frame is drawn around the map.
        showlakes
            Sets whether or not lakes are drawn.
        showland
            Sets whether or not land masses are filled in color.
        showocean
            Sets whether or not oceans are filled in color.
        showrivers
            Sets whether or not rivers are drawn.
        showsubunits
            Sets whether or not boundaries of subunits within
            countries (e.g. states, provinces) are drawn.
        subunitcolor
            Sets the color of the subunits boundaries.
        subunitwidth
            Sets the stroke width (in px) of the subunits
            boundaries.
        uirevision
            Controls persistence of user-driven changes in the view
            (projection and center). Defaults to
            `layout.uirevision`.
        visible
            Sets the default visibility of the base layers.
        """
    def __init__(self,
            arg=None,
            bgcolor=None,
            center=None,
            coastlinecolor=None,
            coastlinewidth=None,
            countrycolor=None,
            countrywidth=None,
            domain=None,
            fitbounds=None,
            framecolor=None,
            framewidth=None,
            lakecolor=None,
            landcolor=None,
            lataxis=None,
            lonaxis=None,
            oceancolor=None,
            projection=None,
            resolution=None,
            rivercolor=None,
            riverwidth=None,
            scope=None,
            showcoastlines=None,
            showcountries=None,
            showframe=None,
            showlakes=None,
            showland=None,
            showocean=None,
            showrivers=None,
            showsubunits=None,
            subunitcolor=None,
            subunitwidth=None,
            uirevision=None,
            visible=None,
            **kwargs
        ):
        """
        Construct a new Geo object

        Parameters
        ----------
        arg
            dict of properties compatible with this constructor or
            an instance of :class:`plotly.graph_objs.layout.Geo`
        bgcolor
            Set the background color of the map
        center
            :class:`plotly.graph_objects.layout.geo.Center`
            instance or dict with compatible properties
        coastlinecolor
            Sets the coastline color.
        coastlinewidth
            Sets the coastline stroke width (in px).
        countrycolor
            Sets line color of the country boundaries.
        countrywidth
            Sets line width (in px) of the country boundaries.
        domain
            :class:`plotly.graph_objects.layout.geo.Domain`
            instance or dict with compatible properties
        fitbounds
            Determines if this subplot's view settings are auto-
            computed to fit trace data. On scoped maps, setting
            `fitbounds` leads to `center.lon` and `center.lat`
            getting auto-filled. On maps with a non-clipped
            projection, setting `fitbounds` leads to `center.lon`,
            `center.lat`, and `projection.rotation.lon` getting
            auto-filled. On maps with a clipped projection, setting
            `fitbounds` leads to `center.lon`, `center.lat`,
            `projection.rotation.lon`, `projection.rotation.lat`,
            `lonaxis.range` and `lataxis.range` getting auto-
            filled. If "locations", only the trace's visible
            locations are considered in the `fitbounds`
            computations. If "geojson", the entire trace input
            `geojson` (if provided) is considered in the
            `fitbounds` computations, Defaults to False.
        framecolor
            Sets the color the frame.
        framewidth
            Sets the stroke width (in px) of the frame.
        lakecolor
            Sets the color of the lakes.
        landcolor
            Sets the land mass color.
        lataxis
            :class:`plotly.graph_objects.layout.geo.Lataxis`
            instance or dict with compatible properties
        lonaxis
            :class:`plotly.graph_objects.layout.geo.Lonaxis`
            instance or dict with compatible properties
        oceancolor
            Sets the ocean color
        projection
            :class:`plotly.graph_objects.layout.geo.Projection`
            instance or dict with compatible properties
        resolution
            Sets the resolution of the base layers. The values have
            units of km/mm e.g. 110 corresponds to a scale ratio of
            1:110,000,000.
        rivercolor
            Sets color of the rivers.
        riverwidth
            Sets the stroke width (in px) of the rivers.
        scope
            Set the scope of the map.
        showcoastlines
            Sets whether or not the coastlines are drawn.
        showcountries
            Sets whether or not country boundaries are drawn.
        showframe
            Sets whether or not a frame is drawn around the map.
        showlakes
            Sets whether or not lakes are drawn.
        showland
            Sets whether or not land masses are filled in color.
        showocean
            Sets whether or not oceans are filled in color.
        showrivers
            Sets whether or not rivers are drawn.
        showsubunits
            Sets whether or not boundaries of subunits within
            countries (e.g. states, provinces) are drawn.
        subunitcolor
            Sets the color of the subunits boundaries.
        subunitwidth
            Sets the stroke width (in px) of the subunits
            boundaries.
        uirevision
            Controls persistence of user-driven changes in the view
            (projection and center). Defaults to
            `layout.uirevision`.
        visible
            Sets the default visibility of the base layers.

        Returns
        -------
        Geo
        """
        super(Geo, self).__init__('geo')

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
The first argument to the plotly.graph_objs.layout.Geo
constructor must be a dict or
an instance of :class:`plotly.graph_objs.layout.Geo`""")

        # Handle skip_invalid
        # -------------------
        self._skip_invalid = kwargs.pop('skip_invalid', False)
        self._validate = kwargs.pop('_validate', True)
        

        # Populate data dict with properties
        # ----------------------------------
        self._init_provided('bgcolor', arg, bgcolor)
        self._init_provided('center', arg, center)
        self._init_provided('coastlinecolor', arg, coastlinecolor)
        self._init_provided('coastlinewidth', arg, coastlinewidth)
        self._init_provided('countrycolor', arg, countrycolor)
        self._init_provided('countrywidth', arg, countrywidth)
        self._init_provided('domain', arg, domain)
        self._init_provided('fitbounds', arg, fitbounds)
        self._init_provided('framecolor', arg, framecolor)
        self._init_provided('framewidth', arg, framewidth)
        self._init_provided('lakecolor', arg, lakecolor)
        self._init_provided('landcolor', arg, landcolor)
        self._init_provided('lataxis', arg, lataxis)
        self._init_provided('lonaxis', arg, lonaxis)
        self._init_provided('oceancolor', arg, oceancolor)
        self._init_provided('projection', arg, projection)
        self._init_provided('resolution', arg, resolution)
        self._init_provided('rivercolor', arg, rivercolor)
        self._init_provided('riverwidth', arg, riverwidth)
        self._init_provided('scope', arg, scope)
        self._init_provided('showcoastlines', arg, showcoastlines)
        self._init_provided('showcountries', arg, showcountries)
        self._init_provided('showframe', arg, showframe)
        self._init_provided('showlakes', arg, showlakes)
        self._init_provided('showland', arg, showland)
        self._init_provided('showocean', arg, showocean)
        self._init_provided('showrivers', arg, showrivers)
        self._init_provided('showsubunits', arg, showsubunits)
        self._init_provided('subunitcolor', arg, subunitcolor)
        self._init_provided('subunitwidth', arg, subunitwidth)
        self._init_provided('uirevision', arg, uirevision)
        self._init_provided('visible', arg, visible)

        # Process unknown kwargs
        # ----------------------
        self._process_kwargs(**dict(arg, **kwargs))

        # Reset skip_invalid
        # ------------------
        self._skip_invalid = False
