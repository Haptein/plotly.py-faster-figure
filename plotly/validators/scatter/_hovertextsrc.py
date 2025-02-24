import _plotly_utils.basevalidators as _bv


class HovertextsrcValidator(_bv.SrcValidator):
    def __init__(self, plotly_name="hovertextsrc", parent_name="scatter", **kwargs):
        super().__init__(
            plotly_name,
            parent_name,
            edit_type=kwargs.pop("edit_type", "none"),
            **kwargs,
        )
