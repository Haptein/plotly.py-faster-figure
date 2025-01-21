import _plotly_utils.basevalidators as _bv


class StartValidator(_bv.NumberValidator):
    def __init__(self, plotly_name="start", parent_name="contour.contours", **kwargs):
        super(StartValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "plot"),
            implied_edits=kwargs.pop("implied_edits", {"^autocontour": False}),
            **kwargs,
        )
