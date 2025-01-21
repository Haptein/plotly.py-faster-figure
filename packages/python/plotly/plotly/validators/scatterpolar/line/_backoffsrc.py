import _plotly_utils.basevalidators as _bv


class BackoffsrcValidator(_bv.SrcValidator):
    def __init__(
        self, plotly_name="backoffsrc", parent_name="scatterpolar.line", **kwargs
    ):
        super(BackoffsrcValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "none"),
            **kwargs,
        )
