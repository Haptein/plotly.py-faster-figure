

import _plotly_utils.basevalidators


class CloseValidator(_plotly_utils.basevalidators.DataArrayValidator):
    def __init__(self, plotly_name='close',
                       parent_name='candlestick',
                       **kwargs):
        super(CloseValidator, self).__init__(plotly_name=plotly_name,
                         parent_name=parent_name,
                 edit_type=kwargs.pop('edit_type', 'calc'),
        **kwargs)