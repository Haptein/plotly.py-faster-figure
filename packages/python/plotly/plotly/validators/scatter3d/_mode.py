

import _plotly_utils.basevalidators as _bv


class ModeValidator(_bv.FlaglistValidator):
    def __init__(self, plotly_name='mode',
                       parent_name='scatter3d',
                       **kwargs):
        super(ModeValidator, self).__init__(plotly_name=plotly_name,
                         parent_name=parent_name,
                 edit_type=kwargs.pop('edit_type', 'calc'),
                 extras=kwargs.pop('extras', ['none']),
                 flags=kwargs.pop('flags', ['lines', 'markers', 'text']),
        **kwargs)