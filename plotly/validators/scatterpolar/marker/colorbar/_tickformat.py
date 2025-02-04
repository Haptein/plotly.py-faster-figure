

import _plotly_utils.basevalidators as _bv


class TickformatValidator(_bv.StringValidator):
    def __init__(self, plotly_name='tickformat',
                       parent_name='scatterpolar.marker.colorbar',
                       **kwargs):
        super().__init__(plotly_name=plotly_name,
                         parent_name=parent_name,
                 edit_type=kwargs.pop('edit_type', 'colorbars'),
        **kwargs)