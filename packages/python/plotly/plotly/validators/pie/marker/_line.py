import _plotly_utils.basevalidators as _bv


class LineValidator(_bv.CompoundValidator):
    def __init__(self, plotly_name="line", parent_name="pie.marker", **kwargs):
        super(LineValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            data_class_str=kwargs.pop("data_class_str", "Line"),
            data_docs=kwargs.pop(
                "data_docs",
                """
            color
                Sets the color of the line enclosing each
                sector.
            colorsrc
                Sets the source reference on Chart Studio Cloud
                for `color`.
            width
                Sets the width (in px) of the line enclosing
                each sector.
            widthsrc
                Sets the source reference on Chart Studio Cloud
                for `width`.
""",
            ),
            **kwargs,
        )
