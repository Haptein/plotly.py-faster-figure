import _plotly_utils.basevalidators as _bv


class HighlightValidator(_bv.BooleanValidator):
    def __init__(
        self, plotly_name="highlight", parent_name="surface.contours.z", **kwargs
    ):
        super().__init__(
            plotly_name,
            parent_name,
            edit_type=kwargs.pop("edit_type", "calc"),
            **kwargs,
        )
