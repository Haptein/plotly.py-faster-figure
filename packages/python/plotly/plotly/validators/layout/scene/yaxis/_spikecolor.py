import _plotly_utils.basevalidators as _bv


class SpikecolorValidator(_bv.ColorValidator):
    def __init__(
        self, plotly_name="spikecolor", parent_name="layout.scene.yaxis", **kwargs
    ):
        super(SpikecolorValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "plot"),
            **kwargs,
        )
