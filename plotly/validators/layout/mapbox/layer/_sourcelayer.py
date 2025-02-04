

import _plotly_utils.basevalidators as _bv


class SourcelayerValidator(_bv.StringValidator):
    def __init__(self, plotly_name='sourcelayer',
                       parent_name='layout.mapbox.layer',
                       **kwargs):
        super().__init__(plotly_name=plotly_name,
                         parent_name=parent_name,
                 edit_type=kwargs.pop('edit_type', 'plot'),
        **kwargs)