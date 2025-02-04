

import _plotly_utils.basevalidators as _bv


class ThicknessmodeValidator(_bv.EnumeratedValidator):
    def __init__(self, plotly_name='thicknessmode',
                       parent_name='histogram.marker.colorbar',
                       **kwargs):
        super().__init__(plotly_name=plotly_name,
                         parent_name=parent_name,
                 edit_type=kwargs.pop('edit_type', 'colorbars'),
                 values=kwargs.pop('values', ['fraction', 'pixels']),
        **kwargs)