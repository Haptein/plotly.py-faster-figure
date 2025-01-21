import _plotly_utils.basevalidators as _bv


class HovertextValidator(_bv.DataArrayValidator):
    def __init__(self, plotly_name="hovertext", parent_name="contour", **kwargs):
        super(HovertextValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "calc"),
            **kwargs,
        )
