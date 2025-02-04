

import _plotly_utils.basevalidators as _bv


class HoverinfoValidator(_bv.FlaglistValidator):
    def __init__(self, plotly_name='hoverinfo',
                       parent_name='cone',
                       **kwargs):
        super().__init__(plotly_name=plotly_name,
                         parent_name=parent_name,
                 array_ok=kwargs.pop('array_ok', True),
                 edit_type=kwargs.pop('edit_type', 'calc'),
                 extras=kwargs.pop('extras', ['all', 'none', 'skip']),
                 flags=kwargs.pop('flags', ['x', 'y', 'z', 'u', 'v', 'w', 'norm', 'text', 'name']),
        **kwargs)