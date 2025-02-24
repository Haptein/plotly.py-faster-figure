import _plotly_utils.basevalidators as _bv


class YhoverformatValidator(_bv.StringValidator):
    def __init__(self, plotly_name="yhoverformat", parent_name="violin", **kwargs):
        super().__init__(
            plotly_name,
            parent_name,
            edit_type=kwargs.pop("edit_type", "none"),
            **kwargs,
        )
