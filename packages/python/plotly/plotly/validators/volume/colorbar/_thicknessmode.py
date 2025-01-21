

import _plotly_utils.basevalidators as _bv


class ThicknessmodeValidator(_bv.EnumeratedValidator):
    def __init__(self, plotly_name='thicknessmode',
                       parent_name='volume.colorbar',
                       **kwargs):
        super(ThicknessmodeValidator, self).__init__(plotly_name=plotly_name,
                         parent_name=parent_name,
                 edit_type=kwargs.pop('edit_type', 'calc'),
                 values=kwargs.pop('values', ['fraction', 'pixels']),
        **kwargs)