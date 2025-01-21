

import _plotly_utils.basevalidators as _bv


class Yperiod0Validator(_bv.AnyValidator):
    def __init__(self, plotly_name='yperiod0',
                       parent_name='waterfall',
                       **kwargs):
        super(Yperiod0Validator, self).__init__(plotly_name=plotly_name,
                         parent_name=parent_name,
                 edit_type=kwargs.pop('edit_type', 'calc'),
        **kwargs)