import _plotly_utils.basevalidators as _bv


class SourceValidator(_bv.AnyValidator):
    def __init__(self, plotly_name="source", parent_name="layout.map.layer", **kwargs):
        super().__init__(
            plotly_name,
            parent_name,
            edit_type=kwargs.pop("edit_type", "plot"),
            **kwargs,
        )
