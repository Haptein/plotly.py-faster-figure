from plotly.basedatatypes import BaseTraceHierarchyType as _BaseTraceHierarchyType
import copy as _copy


class Textfont(_BaseTraceHierarchyType):

    _parent_path_str = "scatterpolar.unselected"
    _path_str = "scatterpolar.unselected.textfont"
    _valid_props = {"color"}

    @property
    def color(self):
        """
        Sets the text font color of unselected points, applied only
        when a selection exists.

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
    def _prop_descriptions(self):
        return """\
        color
            Sets the text font color of unselected points, applied
            only when a selection exists.
        """

    def __init__(self, arg=None, color=None, **kwargs):
        """
        Construct a new Textfont object

        Parameters
        ----------
        arg
            dict of properties compatible with this constructor or
            an instance of :class:`plotly.graph_objs.scatterpolar.u
            nselected.Textfont`
        color
            Sets the text font color of unselected points, applied
            only when a selection exists.

        Returns
        -------
        Textfont
        """
        super().__init__("textfont")
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
The first argument to the plotly.graph_objs.scatterpolar.unselected.Textfont
constructor must be a dict or
an instance of :class:`plotly.graph_objs.scatterpolar.unselected.Textfont`"""
            )

        self._skip_invalid = kwargs.pop("skip_invalid", False)
        self._validate = kwargs.pop("_validate", True)

        self._init_provided("color", arg, color)
        self._process_kwargs(**dict(arg, **kwargs))
        self._skip_invalid = False
