

import _plotly_utils.basevalidators as _bv


class ConstraintextValidator(_bv.EnumeratedValidator):
    def __init__(self, plotly_name='constraintext',
                       parent_name='bar',
                       **kwargs):
        super(ConstraintextValidator, self).__init__(plotly_name=plotly_name,
                         parent_name=parent_name,
                 edit_type=kwargs.pop('edit_type', 'calc'),
                 values=kwargs.pop('values', ['inside', 'outside', 'both', 'none']),
        **kwargs)