import _plotly_utils.basevalidators


class LonaxisValidator(_plotly_utils.basevalidators.CompoundValidator):
    def __init__(self, plotly_name="lonaxis", parent_name="layout.geo", **kwargs):
        super(LonaxisValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            data_class_str=kwargs.pop("data_class_str", "Lonaxis"),
            **kwargs,
        )
