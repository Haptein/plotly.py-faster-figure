import _plotly_utils.basevalidators as _bv


class TickprefixValidator(_bv.StringValidator):
    def __init__(
        self, plotly_name="tickprefix", parent_name="streamtube.colorbar", **kwargs
    ):
        super(TickprefixValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "colorbars"),
            **kwargs,
        )
