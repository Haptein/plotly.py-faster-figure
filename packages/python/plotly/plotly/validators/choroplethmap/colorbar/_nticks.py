import _plotly_utils.basevalidators as _bv


class NticksValidator(_bv.IntegerValidator):
    def __init__(
        self, plotly_name="nticks", parent_name="choroplethmap.colorbar", **kwargs
    ):
        super(NticksValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "colorbars"),
            min=kwargs.pop("min", 0),
            **kwargs,
        )
