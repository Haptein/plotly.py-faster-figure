import _plotly_utils.basevalidators as _bv


class YperiodalignmentValidator(_bv.EnumeratedValidator):
    def __init__(self, plotly_name="yperiodalignment", parent_name="heatmap", **kwargs):
        super(YperiodalignmentValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "calc"),
            implied_edits=kwargs.pop("implied_edits", {"ytype": "scaled"}),
            values=kwargs.pop("values", ["start", "middle", "end"]),
            **kwargs,
        )
