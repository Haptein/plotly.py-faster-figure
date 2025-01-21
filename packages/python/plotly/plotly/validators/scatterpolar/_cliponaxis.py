import _plotly_utils.basevalidators as _bv


class CliponaxisValidator(_bv.BooleanValidator):
    def __init__(self, plotly_name="cliponaxis", parent_name="scatterpolar", **kwargs):
        super(CliponaxisValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "plot"),
            **kwargs,
        )
