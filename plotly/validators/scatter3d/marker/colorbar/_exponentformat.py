import _plotly_utils.basevalidators as _bv


class ExponentformatValidator(_bv.EnumeratedValidator):
    def __init__(
        self,
        plotly_name="exponentformat",
        parent_name="scatter3d.marker.colorbar",
        **kwargs,
    ):
        super().__init__(
            plotly_name,
            parent_name,
            edit_type=kwargs.pop("edit_type", "calc"),
            values=kwargs.pop("values", ["none", "e", "E", "power", "SI", "B"]),
            **kwargs,
        )
