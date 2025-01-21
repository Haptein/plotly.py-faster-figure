

import _plotly_utils.basevalidators as _bv


class Tick0Validator(_bv.NumberValidator):
    def __init__(self, plotly_name='tick0',
                       parent_name='layout.geo.lonaxis',
                       **kwargs):
        super(Tick0Validator, self).__init__(plotly_name=plotly_name,
                         parent_name=parent_name,
                 edit_type=kwargs.pop('edit_type', 'plot'),
        **kwargs)