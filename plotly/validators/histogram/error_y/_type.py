import _plotly_utils.basevalidators as _bv


class TypeValidator(_bv.EnumeratedValidator):
    def __init__(self, plotly_name="type", parent_name="histogram.error_y", **kwargs):
        super().__init__(
            plotly_name,
            parent_name,
            edit_type=kwargs.pop("edit_type", "calc"),
            values=kwargs.pop("values", ["percent", "constant", "sqrt", "data"]),
            **kwargs,
        )
