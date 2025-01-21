import _plotly_utils.basevalidators as _bv


class CategoryorderValidator(_bv.EnumeratedValidator):
    def __init__(
        self, plotly_name="categoryorder", parent_name="parcats.dimension", **kwargs
    ):
        super(CategoryorderValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "calc"),
            values=kwargs.pop(
                "values",
                ["trace", "category ascending", "category descending", "array"],
            ),
            **kwargs,
        )
