import _plotly_utils.basevalidators as _bv


class NcontoursValidator(_bv.IntegerValidator):
    def __init__(self, plotly_name="ncontours", parent_name="contourcarpet", **kwargs):
        super(NcontoursValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "calc"),
            min=kwargs.pop("min", 1),
            **kwargs,
        )
