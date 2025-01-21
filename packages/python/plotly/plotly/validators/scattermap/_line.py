import _plotly_utils.basevalidators as _bv


class LineValidator(_bv.CompoundValidator):
    def __init__(self, plotly_name="line", parent_name="scattermap", **kwargs):
        super(LineValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            data_class_str=kwargs.pop("data_class_str", "Line"),
            data_docs=kwargs.pop(
                "data_docs",
                """
            color
                Sets the line color.
            width
                Sets the line width (in px).
""",
            ),
            **kwargs,
        )
