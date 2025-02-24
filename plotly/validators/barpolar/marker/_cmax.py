import _plotly_utils.basevalidators as _bv


class CmaxValidator(_bv.NumberValidator):
    def __init__(self, plotly_name="cmax", parent_name="barpolar.marker", **kwargs):
        super().__init__(
            plotly_name,
            parent_name,
            edit_type=kwargs.pop("edit_type", "plot"),
            implied_edits=kwargs.pop("implied_edits", {"cauto": False}),
            **kwargs,
        )
