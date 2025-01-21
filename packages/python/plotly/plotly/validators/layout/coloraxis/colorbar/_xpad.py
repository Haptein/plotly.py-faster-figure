import _plotly_utils.basevalidators as _bv


class XpadValidator(_bv.NumberValidator):
    def __init__(
        self, plotly_name="xpad", parent_name="layout.coloraxis.colorbar", **kwargs
    ):
        super(XpadValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "colorbars"),
            min=kwargs.pop("min", 0),
            **kwargs,
        )
