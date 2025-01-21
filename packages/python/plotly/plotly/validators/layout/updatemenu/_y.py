

import _plotly_utils.basevalidators as _bv


class YValidator(_bv.NumberValidator):
    def __init__(self, plotly_name='y',
                       parent_name='layout.updatemenu',
                       **kwargs):
        super(YValidator, self).__init__(plotly_name=plotly_name,
                         parent_name=parent_name,
                 edit_type=kwargs.pop('edit_type', 'arraydraw'),
                 max=kwargs.pop('max', 3),
                 min=kwargs.pop('min', -2),
        **kwargs)