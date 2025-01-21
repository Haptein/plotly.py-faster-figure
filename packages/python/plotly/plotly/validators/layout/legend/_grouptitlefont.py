import _plotly_utils.basevalidators


class GrouptitlefontValidator(_plotly_utils.basevalidators.CompoundValidator):
    def __init__(
        self, plotly_name="grouptitlefont", parent_name="layout.legend", **kwargs
    ):
        super(GrouptitlefontValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            data_class_str=kwargs.pop("data_class_str", "Grouptitlefont"),
            **kwargs,
        )
