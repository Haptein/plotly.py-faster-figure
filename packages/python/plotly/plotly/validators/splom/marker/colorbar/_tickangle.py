

import _plotly_utils.basevalidators as _bv


class TickangleValidator(_bv.AngleValidator):
    def __init__(self, plotly_name='tickangle',
                       parent_name='splom.marker.colorbar',
                       **kwargs):
        super(TickangleValidator, self).__init__(plotly_name=plotly_name,
                         parent_name=parent_name,
                 edit_type=kwargs.pop('edit_type', 'colorbars'),
        **kwargs)