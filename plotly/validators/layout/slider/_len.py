import _plotly_utils.basevalidators as _bv


class LenValidator(_bv.NumberValidator):
    def __init__(self, plotly_name="len", parent_name="layout.slider", **kwargs):
        super().__init__(
            plotly_name,
            parent_name,
            edit_type=kwargs.pop("edit_type", "arraydraw"),
            min=kwargs.pop("min", 0),
            **kwargs,
        )
