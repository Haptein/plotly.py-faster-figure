import _plotly_utils.basevalidators as _bv


class DiffuseValidator(_bv.NumberValidator):
    def __init__(self, plotly_name="diffuse", parent_name="volume.lighting", **kwargs):
        super(DiffuseValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "calc"),
            max=kwargs.pop("max", 1),
            min=kwargs.pop("min", 0),
            **kwargs,
        )
