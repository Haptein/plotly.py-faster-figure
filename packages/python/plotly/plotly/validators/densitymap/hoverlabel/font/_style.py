

import _plotly_utils.basevalidators as _bv


class StyleValidator(_bv.EnumeratedValidator):
    def __init__(self, plotly_name='style',
                       parent_name='densitymap.hoverlabel.font',
                       **kwargs):
        super(StyleValidator, self).__init__(plotly_name=plotly_name,
                         parent_name=parent_name,
                 array_ok=kwargs.pop('array_ok', True),
                 edit_type=kwargs.pop('edit_type', 'none'),
                 values=kwargs.pop('values', ['normal', 'italic']),
        **kwargs)