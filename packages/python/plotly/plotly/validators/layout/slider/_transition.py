import _plotly_utils.basevalidators


class TransitionValidator(_plotly_utils.basevalidators.CompoundValidator):
    def __init__(self, plotly_name="transition", parent_name="layout.slider", **kwargs):
        super(TransitionValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            data_class_str=kwargs.pop("data_class_str", "Transition"),
            **kwargs,
        )
