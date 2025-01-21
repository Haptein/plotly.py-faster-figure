import _plotly_utils.basevalidators as _bv


class SymbolsrcValidator(_bv.SrcValidator):
    def __init__(
        self, plotly_name="symbolsrc", parent_name="scatterternary.marker", **kwargs
    ):
        super(SymbolsrcValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "none"),
            **kwargs,
        )
