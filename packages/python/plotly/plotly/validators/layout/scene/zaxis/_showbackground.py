

import _plotly_utils.basevalidators as _bv


class ShowbackgroundValidator(_bv.BooleanValidator):
    def __init__(self, plotly_name='showbackground',
                       parent_name='layout.scene.zaxis',
                       **kwargs):
        super(ShowbackgroundValidator, self).__init__(plotly_name=plotly_name,
                         parent_name=parent_name,
                 edit_type=kwargs.pop('edit_type', 'plot'),
        **kwargs)