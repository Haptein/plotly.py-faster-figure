

import _plotly_utils.basevalidators


class LineValidator(_plotly_utils.basevalidators.CompoundValidator):
    def __init__(self, plotly_name='line',
                       parent_name='indicator.gauge.threshold',
                       **kwargs):
        super(LineValidator, self).__init__(plotly_name=plotly_name,
                         parent_name=parent_name,
                 data_class_str=kwargs.pop('data_class_str', 'Line'),
                 data_docs=kwargs.pop('data_docs', """
            color
                Sets the color of the threshold line.
            width
                Sets the width (in px) of the threshold line.
"""),
        **kwargs)