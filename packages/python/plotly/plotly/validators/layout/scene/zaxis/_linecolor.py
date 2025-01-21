import _plotly_utils.basevalidators as _bv


class LinecolorValidator(_bv.ColorValidator):
    def __init__(
        self, plotly_name="linecolor", parent_name="layout.scene.zaxis", **kwargs
    ):
        super(LinecolorValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "plot"),
            **kwargs,
        )
