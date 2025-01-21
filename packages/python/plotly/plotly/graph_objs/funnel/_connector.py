from plotly.basedatatypes import BaseTraceHierarchyType as _BaseTraceHierarchyType
import copy as _copy


class Connector(_BaseTraceHierarchyType):

    _parent_path_str = "funnel"
    _path_str = "funnel.connector"
    _valid_props = {"fillcolor", "line", "visible"}

    @property
    def fillcolor(self):
        return self["fillcolor"]

    @fillcolor.setter
    def fillcolor(self, val):
        self["fillcolor"] = val

    @property
    def line(self):
        return self["line"]

    @line.setter
    def line(self, val):
        self["line"] = val

    @property
    def visible(self):
        return self["visible"]

    @visible.setter
    def visible(self, val):
        self["visible"] = val

    @property
    def _prop_descriptions(self):
        return """\
        """

    def __init__(self, arg=None, fillcolor=None, line=None, visible=None, **kwargs):
        super(Connector, self).__init__("connector")

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
The first argument to the plotly.graph_objs.funnel.Connector
constructor must be a dict or
an instance of :class:`plotly.graph_objs.funnel.Connector`"""
            )

        self._skip_invalid = kwargs.pop("skip_invalid", False)
        self._validate = kwargs.pop("_validate", True)

        _v = arg.pop("fillcolor", None)
        _v = fillcolor if fillcolor is not None else _v
        if _v is not None:
            self["fillcolor"] = _v
        _v = arg.pop("line", None)
        _v = line if line is not None else _v
        if _v is not None:
            self["line"] = _v
        _v = arg.pop("visible", None)
        _v = visible if visible is not None else _v
        if _v is not None:
            self["visible"] = _v
        self._process_kwargs(**dict(arg, **kwargs))
        self._skip_invalid = False
