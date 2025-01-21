import _plotly_utils.basevalidators as _bv


class Y0Validator(_bv.AnyValidator):
    def __init__(self, plotly_name="y0", parent_name="violin", **kwargs):
        super(Y0Validator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "calc+clearAxisTypes"),
            **kwargs,
        )
