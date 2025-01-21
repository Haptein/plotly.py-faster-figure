import _plotly_utils.basevalidators as _bv


class XValidator(_bv.NumberValidator):
    def __init__(
        self, plotly_name="x", parent_name="scatterpolargl.marker.colorbar", **kwargs
    ):
        super(XValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "calc"),
            **kwargs,
        )
