import _plotly_utils.basevalidators as _bv


class ActivebgcolorValidator(_bv.ColorValidator):
    def __init__(
        self, plotly_name="activebgcolor", parent_name="layout.slider", **kwargs
    ):
        super().__init__(
            plotly_name,
            parent_name,
            edit_type=kwargs.pop("edit_type", "arraydraw"),
            **kwargs,
        )
