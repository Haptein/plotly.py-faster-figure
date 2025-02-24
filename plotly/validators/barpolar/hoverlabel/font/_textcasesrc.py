import _plotly_utils.basevalidators as _bv


class TextcasesrcValidator(_bv.SrcValidator):
    def __init__(
        self,
        plotly_name="textcasesrc",
        parent_name="barpolar.hoverlabel.font",
        **kwargs,
    ):
        super().__init__(
            plotly_name,
            parent_name,
            edit_type=kwargs.pop("edit_type", "none"),
            **kwargs,
        )
