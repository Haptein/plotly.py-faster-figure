

import _plotly_utils.basevalidators as _bv


class QuartilemethodValidator(_bv.EnumeratedValidator):
    def __init__(self, plotly_name='quartilemethod',
                       parent_name='violin',
                       **kwargs):
        super().__init__(plotly_name=plotly_name,
                         parent_name=parent_name,
                 edit_type=kwargs.pop('edit_type', 'calc'),
                 values=kwargs.pop('values', ['linear', 'exclusive', 'inclusive']),
        **kwargs)