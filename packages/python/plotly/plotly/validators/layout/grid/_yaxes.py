import _plotly_utils.basevalidators as _bv


class YaxesValidator(_bv.InfoArrayValidator):
    def __init__(self, plotly_name="yaxes", parent_name="layout.grid", **kwargs):
        super(YaxesValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "plot"),
            free_length=kwargs.pop("free_length", True),
            items=kwargs.pop(
                "items",
                {
                    "editType": "plot",
                    "valType": "enumerated",
                    "values": ["/^y([2-9]|[1-9][0-9]+)?( domain)?$/", ""],
                },
            ),
            **kwargs,
        )
