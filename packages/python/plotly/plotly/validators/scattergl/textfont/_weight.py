import _plotly_utils.basevalidators as _bv


class WeightValidator(_bv.EnumeratedValidator):
    def __init__(
        self, plotly_name="weight", parent_name="scattergl.textfont", **kwargs
    ):
        super(WeightValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            array_ok=kwargs.pop("array_ok", True),
            edit_type=kwargs.pop("edit_type", "calc"),
            values=kwargs.pop("values", ["normal", "bold"]),
            **kwargs,
        )
