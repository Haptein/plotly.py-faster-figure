

import _plotly_utils.basevalidators as _bv


class ShowtickprefixValidator(_bv.EnumeratedValidator):
    def __init__(self, plotly_name='showtickprefix',
                       parent_name='layout.ternary.caxis',
                       **kwargs):
        super().__init__(plotly_name=plotly_name,
                         parent_name=parent_name,
                 edit_type=kwargs.pop('edit_type', 'plot'),
                 values=kwargs.pop('values', ['all', 'first', 'last', 'none']),
        **kwargs)