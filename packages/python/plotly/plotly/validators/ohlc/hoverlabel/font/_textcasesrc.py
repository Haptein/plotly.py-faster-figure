

import _plotly_utils.basevalidators as _bv


class TextcasesrcValidator(_bv.SrcValidator):
    def __init__(self, plotly_name='textcasesrc',
                       parent_name='ohlc.hoverlabel.font',
                       **kwargs):
        super(TextcasesrcValidator, self).__init__(plotly_name=plotly_name,
                         parent_name=parent_name,
                 edit_type=kwargs.pop('edit_type', 'none'),
        **kwargs)