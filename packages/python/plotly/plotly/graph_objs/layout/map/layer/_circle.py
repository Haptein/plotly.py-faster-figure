from plotly.basedatatypes import BaseLayoutHierarchyType as _BaseLayoutHierarchyType
import copy as _copy


class Circle(_BaseLayoutHierarchyType):

    _parent_path_str = "layout.map.layer"
    _path_str = "layout.map.layer.circle"
    _valid_props = {"radius"}

    @property
    def radius(self):
        return self["radius"]

    @radius.setter
    def radius(self, val):
        self["radius"] = val

    @property
    def _prop_descriptions(self):
        return """\
        """

    def __init__(self, arg=None, radius=None, **kwargs):
        super(Circle, self).__init__("circle")

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
The first argument to the plotly.graph_objs.layout.map.layer.Circle
constructor must be a dict or
an instance of :class:`plotly.graph_objs.layout.map.layer.Circle`"""
            )

        self._skip_invalid = kwargs.pop("skip_invalid", False)
        self._validate = kwargs.pop("_validate", True)

        _v = arg.pop("radius", None)
        _v = radius if radius is not None else _v
        if _v is not None:
            self["radius"] = _v
        self._process_kwargs(**dict(arg, **kwargs))
        self._skip_invalid = False
