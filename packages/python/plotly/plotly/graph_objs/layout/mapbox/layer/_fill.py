from plotly.basedatatypes import BaseLayoutHierarchyType as _BaseLayoutHierarchyType
import copy as _copy


class Fill(_BaseLayoutHierarchyType):

    _parent_path_str = "layout.mapbox.layer"
    _path_str = "layout.mapbox.layer.fill"
    _valid_props = {"outlinecolor"}

    @property
    def outlinecolor(self):
        return self["outlinecolor"]

    @outlinecolor.setter
    def outlinecolor(self, val):
        self["outlinecolor"] = val

    @property
    def _prop_descriptions(self):
        return """\
        """

    def __init__(self, arg=None, outlinecolor=None, **kwargs):
        super(Fill, self).__init__("fill")

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
The first argument to the plotly.graph_objs.layout.mapbox.layer.Fill
constructor must be a dict or
an instance of :class:`plotly.graph_objs.layout.mapbox.layer.Fill`"""
            )

        self._skip_invalid = kwargs.pop("skip_invalid", False)
        self._validate = kwargs.pop("_validate", True)

        _v = arg.pop("outlinecolor", None)
        _v = outlinecolor if outlinecolor is not None else _v
        if _v is not None:
            self["outlinecolor"] = _v
        self._process_kwargs(**dict(arg, **kwargs))
        self._skip_invalid = False
