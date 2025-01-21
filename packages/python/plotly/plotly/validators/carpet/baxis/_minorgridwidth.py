import _plotly_utils.basevalidators as _bv


class MinorgridwidthValidator(_bv.NumberValidator):
    def __init__(
        self, plotly_name="minorgridwidth", parent_name="carpet.baxis", **kwargs
    ):
        super(MinorgridwidthValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "calc"),
            min=kwargs.pop("min", 0),
            **kwargs,
        )
