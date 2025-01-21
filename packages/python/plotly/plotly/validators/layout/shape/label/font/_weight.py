

import _plotly_utils.basevalidators as _bv


class WeightValidator(_bv.IntegerValidator):
    def __init__(self, plotly_name='weight',
                       parent_name='layout.shape.label.font',
                       **kwargs):
        super(WeightValidator, self).__init__(plotly_name=plotly_name,
                         parent_name=parent_name,
                 edit_type=kwargs.pop('edit_type', 'calc+arraydraw'),
                 extras=kwargs.pop('extras', ['normal', 'bold']),
                 max=kwargs.pop('max', 1000),
                 min=kwargs.pop('min', 1),
        **kwargs)