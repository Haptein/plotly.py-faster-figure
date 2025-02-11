import _plotly_utils.basevalidators as _bv


class ArrayValidator(_bv.DataArrayValidator):
    def __init__(self, plotly_name="array", parent_name="scattergl.error_x", **kwargs):
        super().__init__(
            plotly_name,
            parent_name,
            edit_type=kwargs.pop("edit_type", "calc"),
            **kwargs,
        )
