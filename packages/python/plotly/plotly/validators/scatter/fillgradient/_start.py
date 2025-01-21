

import _plotly_utils.basevalidators as _bv


class StartValidator(_bv.NumberValidator):
    def __init__(self, plotly_name='start',
                       parent_name='scatter.fillgradient',
                       **kwargs):
        super(StartValidator, self).__init__(plotly_name=plotly_name,
                         parent_name=parent_name,
                 edit_type=kwargs.pop('edit_type', 'calc'),
        **kwargs)