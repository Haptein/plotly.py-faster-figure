import _plotly_utils.basevalidators as _bv


class SizeminValidator(_bv.NumberValidator):
    def __init__(
        self, plotly_name="sizemin", parent_name="scattergeo.marker", **kwargs
    ):
        super().__init__(
            plotly_name,
            parent_name,
            edit_type=kwargs.pop("edit_type", "calc"),
            min=kwargs.pop("min", 0),
            **kwargs,
        )
