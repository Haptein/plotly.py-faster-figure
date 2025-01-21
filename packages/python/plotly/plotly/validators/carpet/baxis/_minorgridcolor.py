import _plotly_utils.basevalidators as _bv


class MinorgridcolorValidator(_bv.ColorValidator):
    def __init__(
        self, plotly_name="minorgridcolor", parent_name="carpet.baxis", **kwargs
    ):
        super(MinorgridcolorValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "calc"),
            **kwargs,
        )
