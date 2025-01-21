import _plotly_utils.basevalidators


class TickformatstopdefaultsValidator(_plotly_utils.basevalidators.CompoundValidator):
    def __init__(
        self,
        plotly_name="tickformatstopdefaults",
        parent_name="scattercarpet.marker.colorbar",
        **kwargs,
    ):
        super(TickformatstopdefaultsValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            data_class_str=kwargs.pop("data_class_str", "Tickformatstop"),
            **kwargs,
        )
