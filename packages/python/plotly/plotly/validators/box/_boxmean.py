import _plotly_utils.basevalidators as _bv


class BoxmeanValidator(_bv.EnumeratedValidator):
    def __init__(self, plotly_name="boxmean", parent_name="box", **kwargs):
        super(BoxmeanValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "calc"),
            values=kwargs.pop("values", [True, "sd", False]),
            **kwargs,
        )
