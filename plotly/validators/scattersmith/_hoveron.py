

import _plotly_utils.basevalidators as _bv


class HoveronValidator(_bv.FlaglistValidator):
    def __init__(self, plotly_name='hoveron',
                       parent_name='scattersmith',
                       **kwargs):
        super().__init__(plotly_name=plotly_name,
                         parent_name=parent_name,
                 edit_type=kwargs.pop('edit_type', 'style'),
                 flags=kwargs.pop('flags', ['points', 'fills']),
        **kwargs)