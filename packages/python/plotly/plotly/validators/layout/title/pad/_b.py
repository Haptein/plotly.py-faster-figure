import _plotly_utils.basevalidators as _bv


class BValidator(_bv.NumberValidator):
    def __init__(self, plotly_name="b", parent_name="layout.title.pad", **kwargs):
        super(BValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "layoutstyle"),
            **kwargs,
        )
