import _plotly_utils.basevalidators as _bv


class ValueValidator(_bv.StringValidator):
    def __init__(
        self,
        plotly_name="value",
        parent_name="parcats.line.colorbar.tickformatstop",
        **kwargs,
    ):
        super(ValueValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "colorbars"),
            **kwargs,
        )
