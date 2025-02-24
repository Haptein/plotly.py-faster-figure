import _plotly_utils.basevalidators as _bv


class CurrentbinValidator(_bv.EnumeratedValidator):
    def __init__(
        self, plotly_name="currentbin", parent_name="histogram.cumulative", **kwargs
    ):
        super().__init__(
            plotly_name,
            parent_name,
            edit_type=kwargs.pop("edit_type", "calc"),
            values=kwargs.pop("values", ["include", "exclude", "half"]),
            **kwargs,
        )
