

import _plotly_utils.basevalidators as _bv


class ExtendpiecolorsValidator(_bv.BooleanValidator):
    def __init__(self, plotly_name='extendpiecolors',
                       parent_name='layout',
                       **kwargs):
        super(ExtendpiecolorsValidator, self).__init__(plotly_name=plotly_name,
                         parent_name=parent_name,
                 edit_type=kwargs.pop('edit_type', 'calc'),
        **kwargs)