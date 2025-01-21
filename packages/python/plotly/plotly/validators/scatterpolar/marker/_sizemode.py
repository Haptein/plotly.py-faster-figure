import _plotly_utils.basevalidators as _bv


class SizemodeValidator(_bv.EnumeratedValidator):
    def __init__(
        self, plotly_name="sizemode", parent_name="scatterpolar.marker", **kwargs
    ):
        super(SizemodeValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "calc"),
            values=kwargs.pop("values", ["diameter", "area"]),
            **kwargs,
        )
