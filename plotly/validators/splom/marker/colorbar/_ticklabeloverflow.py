import _plotly_utils.basevalidators as _bv


class TicklabeloverflowValidator(_bv.EnumeratedValidator):
    def __init__(
        self,
        plotly_name="ticklabeloverflow",
        parent_name="splom.marker.colorbar",
        **kwargs,
    ):
        super().__init__(
            plotly_name,
            parent_name,
            edit_type=kwargs.pop("edit_type", "colorbars"),
            values=kwargs.pop("values", ["allow", "hide past div", "hide past domain"]),
            **kwargs,
        )
