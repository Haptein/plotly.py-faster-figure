

import _plotly_utils.basevalidators as _bv


class CheatertypeValidator(_bv.EnumeratedValidator):
    def __init__(self, plotly_name='cheatertype',
                       parent_name='carpet.baxis',
                       **kwargs):
        super(CheatertypeValidator, self).__init__(plotly_name=plotly_name,
                         parent_name=parent_name,
                 edit_type=kwargs.pop('edit_type', 'calc'),
                 values=kwargs.pop('values', ['index', 'value']),
        **kwargs)