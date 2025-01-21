

import _plotly_utils.basevalidators as _bv


class CautoValidator(_bv.BooleanValidator):
    def __init__(self, plotly_name='cauto',
                       parent_name='funnel.marker',
                       **kwargs):
        super(CautoValidator, self).__init__(plotly_name=plotly_name,
                         parent_name=parent_name,
                 edit_type=kwargs.pop('edit_type', 'calc'),
                 implied_edits=kwargs.pop('implied_edits', {}),
        **kwargs)