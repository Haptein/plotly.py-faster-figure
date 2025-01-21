

import _plotly_utils.basevalidators as _bv


class TreemapValidator(_bv.CompoundArrayValidator):
    def __init__(self, plotly_name='treemap',
                       parent_name='layout.template.data',
                       **kwargs):
        super(TreemapValidator, self).__init__(plotly_name=plotly_name,
                         parent_name=parent_name,
                 data_class_str=kwargs.pop('data_class_str', 'Treemap'),
                 data_docs=kwargs.pop('data_docs', """
"""),
        **kwargs)