import _plotly_utils.basevalidators as _bv


class TickcolorValidator(_bv.ColorValidator):
    def __init__(
        self,
        plotly_name="tickcolor",
        parent_name="layout.smith.imaginaryaxis",
        **kwargs,
    ):
        super(TickcolorValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "plot"),
            **kwargs,
        )
