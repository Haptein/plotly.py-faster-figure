import _plotly_utils.basevalidators as _bv


class HovertextValidator(_bv.StringValidator):
    def __init__(self, plotly_name="hovertext", parent_name="pie", **kwargs):
        super(HovertextValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            array_ok=kwargs.pop("array_ok", True),
            edit_type=kwargs.pop("edit_type", "style"),
            **kwargs,
        )
