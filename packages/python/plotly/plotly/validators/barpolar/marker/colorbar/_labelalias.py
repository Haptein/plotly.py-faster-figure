

import _plotly_utils.basevalidators as _bv


class LabelaliasValidator(_bv.AnyValidator):
    def __init__(self, plotly_name='labelalias',
                       parent_name='barpolar.marker.colorbar',
                       **kwargs):
        super(LabelaliasValidator, self).__init__(plotly_name=plotly_name,
                         parent_name=parent_name,
                 edit_type=kwargs.pop('edit_type', 'colorbars'),
        **kwargs)