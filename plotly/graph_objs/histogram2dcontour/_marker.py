from plotly.basedatatypes import BaseTraceHierarchyType as _BaseTraceHierarchyType
import copy as _copy


class Marker(_BaseTraceHierarchyType):

    _parent_path_str = "histogram2dcontour"
    _path_str = "histogram2dcontour.marker"
    _valid_props = {"color", "colorsrc"}

    @property
    def color(self):
        """
        Sets the aggregation data.

        The 'color' property is an array that may be specified as a tuple,
        list, numpy array, or pandas Series

        Returns
        -------
        numpy.ndarray
        """
        return self["color"]

    @color.setter
    def color(self, val):
        self["color"] = val

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

    @property
    def _prop_descriptions(self):
        return """\
        color
            Sets the aggregation data.
        colorsrc
            Sets the source reference on Chart Studio Cloud for
            `color`.
        """

    def __init__(self, arg=None, color=None, colorsrc=None, **kwargs):
        """
        Construct a new Marker object

        Parameters
        ----------
        arg
            dict of properties compatible with this constructor or
            an instance of
            :class:`plotly.graph_objs.histogram2dcontour.Marker`
        color
            Sets the aggregation data.
        colorsrc
            Sets the source reference on Chart Studio Cloud for
            `color`.

        Returns
        -------
        Marker
        """
        super().__init__("marker")
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
The first argument to the plotly.graph_objs.histogram2dcontour.Marker
constructor must be a dict or
an instance of :class:`plotly.graph_objs.histogram2dcontour.Marker`"""
            )

        self._skip_invalid = kwargs.pop("skip_invalid", False)
        self._validate = kwargs.pop("_validate", True)

        self._init_provided("color", arg, color)
        self._init_provided("colorsrc", arg, colorsrc)
        self._process_kwargs(**dict(arg, **kwargs))
        self._skip_invalid = False
