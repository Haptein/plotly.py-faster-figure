

import _plotly_utils.basevalidators as _bv


class StyleValidator(_bv.EnumeratedValidator):
    def __init__(self, plotly_name='style',
                       parent_name='scatterpolargl.marker.colorbar.tickfont',
                       **kwargs):
        super(StyleValidator, self).__init__(plotly_name=plotly_name,
                         parent_name=parent_name,
                 edit_type=kwargs.pop('edit_type', 'calc'),
                 values=kwargs.pop('values', ['normal', 'italic']),
        **kwargs)