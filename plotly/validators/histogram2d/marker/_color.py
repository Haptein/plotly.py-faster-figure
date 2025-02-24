import _plotly_utils.basevalidators as _bv


class ColorValidator(_bv.DataArrayValidator):
    def __init__(self, plotly_name="color", parent_name="histogram2d.marker", **kwargs):
        super().__init__(
            plotly_name,
            parent_name,
            edit_type=kwargs.pop("edit_type", "calc"),
            **kwargs,
        )
