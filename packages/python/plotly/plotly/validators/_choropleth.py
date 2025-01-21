import _plotly_utils.basevalidators


class ChoroplethValidator(_plotly_utils.basevalidators.CompoundValidator):
    def __init__(self, plotly_name="choropleth", parent_name="", **kwargs):
        super(ChoroplethValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            data_class_str=kwargs.pop("data_class_str", "Choropleth"),
            **kwargs,
        )
