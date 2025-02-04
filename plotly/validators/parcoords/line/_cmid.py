

import _plotly_utils.basevalidators as _bv


class CmidValidator(_bv.NumberValidator):
    def __init__(self, plotly_name='cmid',
                       parent_name='parcoords.line',
                       **kwargs):
        super().__init__(plotly_name=plotly_name,
                         parent_name=parent_name,
                 edit_type=kwargs.pop('edit_type', 'calc'),
                 implied_edits=kwargs.pop('implied_edits', {}),
        **kwargs)