import _plotly_utils.basevalidators as _bv


class LenmodeValidator(_bv.EnumeratedValidator):
    def __init__(
        self, plotly_name="lenmode", parent_name="isosurface.colorbar", **kwargs
    ):
        super().__init__(
            plotly_name,
            parent_name,
            edit_type=kwargs.pop("edit_type", "calc"),
            values=kwargs.pop("values", ["fraction", "pixels"]),
            **kwargs,
        )
