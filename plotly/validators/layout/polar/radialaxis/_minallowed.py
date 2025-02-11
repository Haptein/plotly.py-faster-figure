import _plotly_utils.basevalidators as _bv


class MinallowedValidator(_bv.AnyValidator):
    def __init__(
        self, plotly_name="minallowed", parent_name="layout.polar.radialaxis", **kwargs
    ):
        super().__init__(
            plotly_name,
            parent_name,
            edit_type=kwargs.pop("edit_type", "plot"),
            implied_edits=kwargs.pop("implied_edits", {"^autorange": False}),
            **kwargs,
        )
