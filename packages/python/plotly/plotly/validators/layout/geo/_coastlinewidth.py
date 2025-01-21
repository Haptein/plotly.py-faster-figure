import _plotly_utils.basevalidators as _bv


class CoastlinewidthValidator(_bv.NumberValidator):
    def __init__(
        self, plotly_name="coastlinewidth", parent_name="layout.geo", **kwargs
    ):
        super(CoastlinewidthValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "plot"),
            min=kwargs.pop("min", 0),
            **kwargs,
        )
