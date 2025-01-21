import _plotly_utils.basevalidators as _bv


class UsecolormapValidator(_bv.BooleanValidator):
    def __init__(
        self, plotly_name="usecolormap", parent_name="surface.contours.x", **kwargs
    ):
        super(UsecolormapValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "calc"),
            **kwargs,
        )
