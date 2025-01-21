import _plotly_utils.basevalidators as _bv


class CircleValidator(_bv.CompoundValidator):
    def __init__(self, plotly_name="circle", parent_name="layout.map.layer", **kwargs):
        super(CircleValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            data_class_str=kwargs.pop("data_class_str", "Circle"),
            data_docs=kwargs.pop(
                "data_docs",
                """
            radius
                Sets the circle radius (map.layer.paint.circle-
                radius). Has an effect only when `type` is set
                to "circle".
""",
            ),
            **kwargs,
        )
