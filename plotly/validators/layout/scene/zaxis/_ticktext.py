import _plotly_utils.basevalidators as _bv


class TicktextValidator(_bv.DataArrayValidator):
    def __init__(
        self, plotly_name="ticktext", parent_name="layout.scene.zaxis", **kwargs
    ):
        super().__init__(
            plotly_name,
            parent_name,
            edit_type=kwargs.pop("edit_type", "plot"),
            **kwargs,
        )
