import _plotly_utils.basevalidators as _bv


class SizerefValidator(_bv.NumberValidator):
    def __init__(
        self, plotly_name="sizeref", parent_name="scattersmith.marker", **kwargs
    ):
        super().__init__(
            plotly_name,
            parent_name,
            edit_type=kwargs.pop("edit_type", "calc"),
            **kwargs,
        )
