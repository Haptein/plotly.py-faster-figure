import _plotly_utils.basevalidators as _bv


class AnnotationsValidator(_bv.CompoundArrayValidator):
    def __init__(self, plotly_name="annotations", parent_name="layout", **kwargs):
        super().__init__(
            plotly_name,
            parent_name,
            data_class_str=kwargs.pop("data_class_str", "Annotation"),
            data_docs=kwargs.pop(
                "data_docs",
                """
""",
            ),
            **kwargs,
        )
