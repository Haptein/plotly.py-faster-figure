import _plotly_utils.basevalidators as _bv


class ValueValidator(_bv.NumberValidator):
    def __init__(self, plotly_name="value", parent_name="histogram.error_x", **kwargs):
        super().__init__(
            plotly_name,
            parent_name,
            edit_type=kwargs.pop("edit_type", "calc"),
            min=kwargs.pop("min", 0),
            **kwargs,
        )
