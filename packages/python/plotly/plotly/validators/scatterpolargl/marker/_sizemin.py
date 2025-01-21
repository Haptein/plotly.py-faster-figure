import _plotly_utils.basevalidators as _bv


class SizeminValidator(_bv.NumberValidator):
    def __init__(
        self, plotly_name="sizemin", parent_name="scatterpolargl.marker", **kwargs
    ):
        super(SizeminValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "calc"),
            min=kwargs.pop("min", 0),
            **kwargs,
        )
