

import _plotly_utils.basevalidators


class ShowticksuffixValidator(_plotly_utils.basevalidators.EnumeratedValidator):
    def __init__(self, plotly_name='showticksuffix',
                       parent_name='layout.yaxis',
                       **kwargs):
        super(ShowticksuffixValidator, self).__init__(plotly_name=plotly_name,
                         parent_name=parent_name,
                 edit_type=kwargs.pop('edit_type', 'ticks'),
                 values=kwargs.pop('values', ['all', 'first', 'last', 'none']),
        **kwargs)