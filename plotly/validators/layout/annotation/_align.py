import _plotly_utils.basevalidators as _bv


class AlignValidator(_bv.EnumeratedValidator):
    def __init__(self, plotly_name="align", parent_name="layout.annotation", **kwargs):
        super().__init__(
            plotly_name,
            parent_name,
            edit_type=kwargs.pop("edit_type", "arraydraw"),
            values=kwargs.pop("values", ["left", "center", "right"]),
            **kwargs,
        )
