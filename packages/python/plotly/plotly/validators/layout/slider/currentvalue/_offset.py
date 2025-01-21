import _plotly_utils.basevalidators as _bv


class OffsetValidator(_bv.NumberValidator):
    def __init__(
        self, plotly_name="offset", parent_name="layout.slider.currentvalue", **kwargs
    ):
        super(OffsetValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "arraydraw"),
            **kwargs,
        )
