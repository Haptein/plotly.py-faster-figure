import _plotly_utils.basevalidators


class ScatterternaryValidator(_plotly_utils.basevalidators.CompoundArrayValidator):
    def __init__(
        self, plotly_name="scatterternary", parent_name="layout.template.data", **kwargs
    ):
        super(ScatterternaryValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            data_class_str=kwargs.pop("data_class_str", "Scatterternary"),
            **kwargs,
        )
