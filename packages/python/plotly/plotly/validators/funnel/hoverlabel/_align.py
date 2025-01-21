import _plotly_utils.basevalidators as _bv


class AlignValidator(_bv.EnumeratedValidator):
    def __init__(self, plotly_name="align", parent_name="funnel.hoverlabel", **kwargs):
        super(AlignValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            array_ok=kwargs.pop("array_ok", True),
            edit_type=kwargs.pop("edit_type", "none"),
            values=kwargs.pop("values", ["left", "right", "auto"]),
            **kwargs,
        )
