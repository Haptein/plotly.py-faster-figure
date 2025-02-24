import _plotly_utils.basevalidators as _bv


class LinewidthValidator(_bv.NumberValidator):
    def __init__(self, plotly_name="linewidth", parent_name="carpet.baxis", **kwargs):
        super().__init__(
            plotly_name,
            parent_name,
            edit_type=kwargs.pop("edit_type", "calc"),
            min=kwargs.pop("min", 0),
            **kwargs,
        )
