import _plotly_utils.basevalidators as _bv


class YgapValidator(_bv.NumberValidator):
    def __init__(self, plotly_name="ygap", parent_name="heatmap", **kwargs):
        super(YgapValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "plot"),
            min=kwargs.pop("min", 0),
            **kwargs,
        )
