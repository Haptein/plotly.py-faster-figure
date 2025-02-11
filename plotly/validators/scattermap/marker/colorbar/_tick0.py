import _plotly_utils.basevalidators as _bv


class Tick0Validator(_bv.AnyValidator):
    def __init__(
        self, plotly_name="tick0", parent_name="scattermap.marker.colorbar", **kwargs
    ):
        super().__init__(
            plotly_name,
            parent_name,
            edit_type=kwargs.pop("edit_type", "calc"),
            implied_edits=kwargs.pop("implied_edits", {"tickmode": "linear"}),
            **kwargs,
        )
