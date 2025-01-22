

import _plotly_utils.basevalidators


class SideValidator(_plotly_utils.basevalidators.EnumeratedValidator):
    def __init__(self, plotly_name='side',
                       parent_name='violin',
                       **kwargs):
        super(SideValidator, self).__init__(plotly_name=plotly_name,
                         parent_name=parent_name,
                 edit_type=kwargs.pop('edit_type', 'calc'),
                 values=kwargs.pop('values', ['both', 'positive', 'negative']),
        **kwargs)