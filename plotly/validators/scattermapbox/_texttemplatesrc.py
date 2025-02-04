

import _plotly_utils.basevalidators as _bv


class TexttemplatesrcValidator(_bv.SrcValidator):
    def __init__(self, plotly_name='texttemplatesrc',
                       parent_name='scattermapbox',
                       **kwargs):
        super().__init__(plotly_name=plotly_name,
                         parent_name=parent_name,
                 edit_type=kwargs.pop('edit_type', 'none'),
        **kwargs)