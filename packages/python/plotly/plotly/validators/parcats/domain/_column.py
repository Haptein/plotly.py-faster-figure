import _plotly_utils.basevalidators as _bv


class ColumnValidator(_bv.IntegerValidator):
    def __init__(self, plotly_name="column", parent_name="parcats.domain", **kwargs):
        super(ColumnValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "calc"),
            min=kwargs.pop("min", 0),
            **kwargs,
        )
