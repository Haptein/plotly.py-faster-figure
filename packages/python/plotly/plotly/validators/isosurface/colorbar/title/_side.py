import _plotly_utils.basevalidators as _bv


class SideValidator(_bv.EnumeratedValidator):
    def __init__(
        self, plotly_name="side", parent_name="isosurface.colorbar.title", **kwargs
    ):
        super(SideValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "calc"),
            values=kwargs.pop("values", ["right", "top", "bottom"]),
            **kwargs,
        )
