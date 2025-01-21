

import _plotly_utils.basevalidators as _bv


class XanchorValidator(_bv.EnumeratedValidator):
    def __init__(self, plotly_name='xanchor',
                       parent_name='scattergeo.marker.colorbar',
                       **kwargs):
        super(XanchorValidator, self).__init__(plotly_name=plotly_name,
                         parent_name=parent_name,
                 edit_type=kwargs.pop('edit_type', 'calc'),
                 values=kwargs.pop('values', ['left', 'center', 'right']),
        **kwargs)