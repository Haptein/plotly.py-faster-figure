import _plotly_utils.basevalidators as _bv


class NameValidator(_bv.StringValidator):
    def __init__(self, plotly_name="name", parent_name="layout.image", **kwargs):
        super().__init__(
            plotly_name,
            parent_name,
            edit_type=kwargs.pop("edit_type", "none"),
            **kwargs,
        )
