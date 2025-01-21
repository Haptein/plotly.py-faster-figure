

import _plotly_utils.basevalidators as _bv


class ValuehoverformatValidator(_bv.StringValidator):
    def __init__(self, plotly_name='valuehoverformat',
                       parent_name='isosurface',
                       **kwargs):
        super(ValuehoverformatValidator, self).__init__(plotly_name=plotly_name,
                         parent_name=parent_name,
                 edit_type=kwargs.pop('edit_type', 'calc'),
        **kwargs)