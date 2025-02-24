import _plotly_utils.basevalidators as _bv


class SymmetricValidator(_bv.BooleanValidator):
    def __init__(
        self, plotly_name="symmetric", parent_name="scatter3d.error_y", **kwargs
    ):
        super().__init__(
            plotly_name,
            parent_name,
            edit_type=kwargs.pop("edit_type", "calc"),
            **kwargs,
        )
