import _plotly_utils.basevalidators as _bv


class BarcornerradiusValidator(_bv.AnyValidator):
    def __init__(self, plotly_name="barcornerradius", parent_name="layout", **kwargs):
        super().__init__(
            plotly_name,
            parent_name,
            edit_type=kwargs.pop("edit_type", "calc"),
            **kwargs,
        )
