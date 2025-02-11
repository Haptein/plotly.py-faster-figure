import _plotly_utils.basevalidators as _bv


class CountValidator(_bv.IntegerValidator):
    def __init__(self, plotly_name="count", parent_name="isosurface.surface", **kwargs):
        super().__init__(
            plotly_name,
            parent_name,
            edit_type=kwargs.pop("edit_type", "calc"),
            min=kwargs.pop("min", 1),
            **kwargs,
        )
