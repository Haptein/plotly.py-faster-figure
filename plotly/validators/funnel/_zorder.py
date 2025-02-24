import _plotly_utils.basevalidators as _bv


class ZorderValidator(_bv.IntegerValidator):
    def __init__(self, plotly_name="zorder", parent_name="funnel", **kwargs):
        super().__init__(
            plotly_name,
            parent_name,
            edit_type=kwargs.pop("edit_type", "plot"),
            **kwargs,
        )
