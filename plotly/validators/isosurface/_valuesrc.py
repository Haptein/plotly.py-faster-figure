

import _plotly_utils.basevalidators as _bv


class ValuesrcValidator(_bv.SrcValidator):
    def __init__(self, plotly_name='valuesrc',
                       parent_name='isosurface',
                       **kwargs):
        super().__init__(plotly_name=plotly_name,
                         parent_name=parent_name,
                 edit_type=kwargs.pop('edit_type', 'none'),
        **kwargs)