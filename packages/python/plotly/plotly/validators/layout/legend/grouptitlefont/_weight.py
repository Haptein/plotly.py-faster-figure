

import _plotly_utils.basevalidators as _bv


class WeightValidator(_bv.IntegerValidator):
    def __init__(self, plotly_name='weight',
                       parent_name='layout.legend.grouptitlefont',
                       **kwargs):
        super(WeightValidator, self).__init__(plotly_name=plotly_name,
                         parent_name=parent_name,
                 edit_type=kwargs.pop('edit_type', 'legend'),
                 extras=kwargs.pop('extras', ['normal', 'bold']),
                 max=kwargs.pop('max', 1000),
                 min=kwargs.pop('min', 1),
        **kwargs)