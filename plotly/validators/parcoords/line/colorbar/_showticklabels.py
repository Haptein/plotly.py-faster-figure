import _plotly_utils.basevalidators as _bv


class ShowticklabelsValidator(_bv.BooleanValidator):
    def __init__(
        self,
        plotly_name="showticklabels",
        parent_name="parcoords.line.colorbar",
        **kwargs,
    ):
        super().__init__(
            plotly_name,
            parent_name,
            edit_type=kwargs.pop("edit_type", "colorbars"),
            **kwargs,
        )
