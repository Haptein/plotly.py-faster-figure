from plotly.basedatatypes import BaseTraceHierarchyType as _BaseTraceHierarchyType
import copy as _copy


class Line(_BaseTraceHierarchyType):

    _parent_path_str = "contourcarpet"
    _path_str = "contourcarpet.line"
    _valid_props = {"color", "dash", "smoothing", "width"}

    @property
    def color(self):
        """
        Sets the color of the contour level. Has no effect if
        `contours.coloring` is set to "lines".

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
        return self["color"]

    @color.setter
    def color(self, val):
        self["color"] = val

    @property
    def dash(self):
        """
        Sets the dash style of lines. Set to a dash type string
        ("solid", "dot", "dash", "longdash", "dashdot", or
        "longdashdot") or a dash length list in px (eg
        "5px,10px,2px,2px").

        The 'dash' property is an enumeration that may be specified as:
          - One of the following dash styles:
                ['solid', 'dot', 'dash', 'longdash', 'dashdot', 'longdashdot']
          - A string containing a dash length list in pixels or percentages
                (e.g. '5px 10px 2px 2px', '5, 10, 2, 2', '10% 20% 40%', etc.)

        Returns
        -------
        str
        """
        return self["dash"]

    @dash.setter
    def dash(self, val):
        self["dash"] = val

    @property
    def smoothing(self):
        """
        Sets the amount of smoothing for the contour lines, where 0
        corresponds to no smoothing.

        The 'smoothing' property is a number and may be specified as:
          - An int or float in the interval [0, 1.3]

        Returns
        -------
        int|float
        """
        return self["smoothing"]

    @smoothing.setter
    def smoothing(self, val):
        self["smoothing"] = val

    @property
    def width(self):
        """
        Sets the contour line width in (in px) Defaults to 0.5 when
        `contours.type` is "levels". Defaults to 2 when `contour.type`
        is "constraint".

        The 'width' property is a number and may be specified as:
          - An int or float in the interval [0, inf]

        Returns
        -------
        int|float
        """
        return self["width"]

    @width.setter
    def width(self, val):
        self["width"] = val

    @property
    def _prop_descriptions(self):
        return """\
        color
            Sets the color of the contour level. Has no effect if
            `contours.coloring` is set to "lines".
        dash
            Sets the dash style of lines. Set to a dash type string
            ("solid", "dot", "dash", "longdash", "dashdot", or
            "longdashdot") or a dash length list in px (eg
            "5px,10px,2px,2px").
        smoothing
            Sets the amount of smoothing for the contour lines,
            where 0 corresponds to no smoothing.
        width
            Sets the contour line width in (in px) Defaults to 0.5
            when `contours.type` is "levels". Defaults to 2 when
            `contour.type` is "constraint".
        """

    def __init__(
        self, arg=None, color=None, dash=None, smoothing=None, width=None, **kwargs
    ):
        """
        Construct a new Line object

        Parameters
        ----------
        arg
            dict of properties compatible with this constructor or
            an instance of
            :class:`plotly.graph_objs.contourcarpet.Line`
        color
            Sets the color of the contour level. Has no effect if
            `contours.coloring` is set to "lines".
        dash
            Sets the dash style of lines. Set to a dash type string
            ("solid", "dot", "dash", "longdash", "dashdot", or
            "longdashdot") or a dash length list in px (eg
            "5px,10px,2px,2px").
        smoothing
            Sets the amount of smoothing for the contour lines,
            where 0 corresponds to no smoothing.
        width
            Sets the contour line width in (in px) Defaults to 0.5
            when `contours.type` is "levels". Defaults to 2 when
            `contour.type` is "constraint".

        Returns
        -------
        Line
        """
        super().__init__("line")
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
The first argument to the plotly.graph_objs.contourcarpet.Line
constructor must be a dict or
an instance of :class:`plotly.graph_objs.contourcarpet.Line`"""
            )

        self._skip_invalid = kwargs.pop("skip_invalid", False)
        self._validate = kwargs.pop("_validate", True)

        self._init_provided("color", arg, color)
        self._init_provided("dash", arg, dash)
        self._init_provided("smoothing", arg, smoothing)
        self._init_provided("width", arg, width)
        self._process_kwargs(**dict(arg, **kwargs))
        self._skip_invalid = False
