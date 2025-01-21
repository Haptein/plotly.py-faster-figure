

import _plotly_utils.basevalidators as _bv


class ZValidator(_bv.CompoundValidator):
    def __init__(self, plotly_name='z',
                       parent_name='volume.caps',
                       **kwargs):
        super(ZValidator, self).__init__(plotly_name=plotly_name,
                         parent_name=parent_name,
                 data_class_str=kwargs.pop('data_class_str', 'Z'),
                 data_docs=kwargs.pop('data_docs', """
"""),
        **kwargs)