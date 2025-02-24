import _plotly_utils.basevalidators as _bv


class TokenValidator(_bv.StringValidator):
    def __init__(self, plotly_name="token", parent_name="table.stream", **kwargs):
        super().__init__(
            plotly_name,
            parent_name,
            edit_type=kwargs.pop("edit_type", "calc"),
            no_blank=kwargs.pop("no_blank", True),
            strict=kwargs.pop("strict", True),
            **kwargs,
        )
