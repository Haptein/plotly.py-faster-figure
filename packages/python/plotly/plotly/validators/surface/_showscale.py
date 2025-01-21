

import _plotly_utils.basevalidators as _bv


class ShowscaleValidator(_bv.BooleanValidator):
    def __init__(self, plotly_name='showscale',
                       parent_name='surface',
                       **kwargs):
        super(ShowscaleValidator, self).__init__(plotly_name=plotly_name,
                         parent_name=parent_name,
                 edit_type=kwargs.pop('edit_type', 'calc'),
        **kwargs)