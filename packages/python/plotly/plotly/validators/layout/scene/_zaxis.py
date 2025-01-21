import _plotly_utils.basevalidators


class ZaxisValidator(_plotly_utils.basevalidators.CompoundValidator):
    def __init__(self, plotly_name="zaxis", parent_name="layout.scene", **kwargs):
        super(ZaxisValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            data_class_str=kwargs.pop("data_class_str", "ZAxis"),
            **kwargs,
        )
