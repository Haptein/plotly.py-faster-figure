

import _plotly_utils.basevalidators as _bv


class StyleValidator(_bv.AnyValidator):
    def __init__(self, plotly_name='style',
                       parent_name='layout.mapbox',
                       **kwargs):
        super().__init__(plotly_name=plotly_name,
                         parent_name=parent_name,
                 edit_type=kwargs.pop('edit_type', 'plot'),
                 values=kwargs.pop('values', ['basic', 'streets', 'outdoors', 'light', 'dark', 'satellite', 'satellite-streets', 'carto-darkmatter', 'carto-positron', 'open-street-map', 'stamen-terrain', 'stamen-toner', 'stamen-watercolor', 'white-bg']),
        **kwargs)