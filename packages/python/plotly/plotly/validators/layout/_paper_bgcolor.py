import _plotly_utils.basevalidators as _bv


class Paper_BgcolorValidator(_bv.ColorValidator):
    def __init__(self, plotly_name="paper_bgcolor", parent_name="layout", **kwargs):
        super(Paper_BgcolorValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "plot"),
            **kwargs,
        )
