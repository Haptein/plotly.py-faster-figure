import _plotly_utils.basevalidators as _bv


class BarmodeValidator(_bv.EnumeratedValidator):
    def __init__(self, plotly_name="barmode", parent_name="layout", **kwargs):
        super(BarmodeValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "calc"),
            values=kwargs.pop("values", ["stack", "group", "overlay", "relative"]),
            **kwargs,
        )
