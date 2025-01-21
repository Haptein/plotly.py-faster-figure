

import _plotly_utils.basevalidators as _bv


class LevelValidator(_bv.AnyValidator):
    def __init__(self, plotly_name='level',
                       parent_name='treemap',
                       **kwargs):
        super(LevelValidator, self).__init__(plotly_name=plotly_name,
                         parent_name=parent_name,
                 anim=kwargs.pop('anim', True),
                 edit_type=kwargs.pop('edit_type', 'plot'),
        **kwargs)