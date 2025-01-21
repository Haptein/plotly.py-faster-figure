

import _plotly_utils.basevalidators as _bv


class ColorValidator(_bv.DataArrayValidator):
    def __init__(self, plotly_name='color',
                       parent_name='histogram2dcontour.marker',
                       **kwargs):
        super(ColorValidator, self).__init__(plotly_name=plotly_name,
                         parent_name=parent_name,
                 edit_type=kwargs.pop('edit_type', 'calc'),
        **kwargs)