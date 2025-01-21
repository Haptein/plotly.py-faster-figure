import _plotly_utils.basevalidators as _bv


class BackoffValidator(_bv.NumberValidator):
    def __init__(
        self, plotly_name="backoff", parent_name="scatterpolar.line", **kwargs
    ):
        super(BackoffValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            array_ok=kwargs.pop("array_ok", True),
            edit_type=kwargs.pop("edit_type", "plot"),
            min=kwargs.pop("min", 0),
            **kwargs,
        )
