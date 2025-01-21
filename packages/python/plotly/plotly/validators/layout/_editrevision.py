import _plotly_utils.basevalidators as _bv


class EditrevisionValidator(_bv.AnyValidator):
    def __init__(self, plotly_name="editrevision", parent_name="layout", **kwargs):
        super(EditrevisionValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "none"),
            **kwargs,
        )
