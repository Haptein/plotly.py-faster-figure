

import _plotly_utils.basevalidators as _bv


class TextcaseValidator(_bv.EnumeratedValidator):
    def __init__(self, plotly_name='textcase',
                       parent_name='densitymapbox.legendgrouptitle.font',
                       **kwargs):
        super().__init__(plotly_name=plotly_name,
                         parent_name=parent_name,
                 edit_type=kwargs.pop('edit_type', 'style'),
                 values=kwargs.pop('values', ['normal', 'word caps', 'upper', 'lower']),
        **kwargs)