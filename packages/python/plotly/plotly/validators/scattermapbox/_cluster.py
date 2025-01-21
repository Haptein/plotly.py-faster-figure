

import _plotly_utils.basevalidators as _bv


class ClusterValidator(_bv.CompoundValidator):
    def __init__(self, plotly_name='cluster',
                       parent_name='scattermapbox',
                       **kwargs):
        super(ClusterValidator, self).__init__(plotly_name=plotly_name,
                         parent_name=parent_name,
                 data_class_str=kwargs.pop('data_class_str', 'Cluster'),
                 data_docs=kwargs.pop('data_docs', """
"""),
        **kwargs)