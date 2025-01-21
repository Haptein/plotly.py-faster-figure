import _plotly_utils.basevalidators as _bv


class TicklabelpositionValidator(_bv.EnumeratedValidator):
    def __init__(
        self,
        plotly_name="ticklabelposition",
        parent_name="scatter3d.line.colorbar",
        **kwargs,
    ):
        super(TicklabelpositionValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "calc"),
            values=kwargs.pop(
                "values",
                [
                    "outside",
                    "inside",
                    "outside top",
                    "inside top",
                    "outside left",
                    "inside left",
                    "outside right",
                    "inside right",
                    "outside bottom",
                    "inside bottom",
                ],
            ),
            **kwargs,
        )
