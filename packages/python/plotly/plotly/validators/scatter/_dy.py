

import _plotly_utils.basevalidators as _bv


class DyValidator(_bv.NumberValidator):
    def __init__(self, plotly_name='dy',
                       parent_name='scatter',
                       **kwargs):
        super(DyValidator, self).__init__(plotly_name=plotly_name,
                         parent_name=parent_name,
                 anim=kwargs.pop('anim', True),
                 edit_type=kwargs.pop('edit_type', 'calc'),
        **kwargs)