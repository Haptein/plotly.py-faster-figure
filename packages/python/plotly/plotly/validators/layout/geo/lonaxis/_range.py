import _plotly_utils.basevalidators as _bv


class RangeValidator(_bv.InfoArrayValidator):
    def __init__(self, plotly_name="range", parent_name="layout.geo.lonaxis", **kwargs):
        super(RangeValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "plot"),
            items=kwargs.pop(
                "items",
                [
                    {"editType": "plot", "valType": "number"},
                    {"editType": "plot", "valType": "number"},
                ],
            ),
            **kwargs,
        )
