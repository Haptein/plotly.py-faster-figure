

import _plotly_utils.basevalidators as _bv


class TypeValidator(_bv.EnumeratedValidator):
    def __init__(self, plotly_name='type',
                       parent_name='layout.geo.projection',
                       **kwargs):
        super(TypeValidator, self).__init__(plotly_name=plotly_name,
                         parent_name=parent_name,
                 edit_type=kwargs.pop('edit_type', 'plot'),
                 values=kwargs.pop('values', ['airy', 'aitoff', 'albers', 'albers usa', 'august', 'azimuthal equal area', 'azimuthal equidistant', 'baker', 'bertin1953', 'boggs', 'bonne', 'bottomley', 'bromley', 'collignon', 'conic conformal', 'conic equal area', 'conic equidistant', 'craig', 'craster', 'cylindrical equal area', 'cylindrical stereographic', 'eckert1', 'eckert2', 'eckert3', 'eckert4', 'eckert5', 'eckert6', 'eisenlohr', 'equal earth', 'equirectangular', 'fahey', 'foucaut', 'foucaut sinusoidal', 'ginzburg4', 'ginzburg5', 'ginzburg6', 'ginzburg8', 'ginzburg9', 'gnomonic', 'gringorten', 'gringorten quincuncial', 'guyou', 'hammer', 'hill', 'homolosine', 'hufnagel', 'hyperelliptical', 'kavrayskiy7', 'lagrange', 'larrivee', 'laskowski', 'loximuthal', 'mercator', 'miller', 'mollweide', 'mt flat polar parabolic', 'mt flat polar quartic', 'mt flat polar sinusoidal', 'natural earth', 'natural earth1', 'natural earth2', 'nell hammer', 'nicolosi', 'orthographic', 'patterson', 'peirce quincuncial', 'polyconic', 'rectangular polyconic', 'robinson', 'satellite', 'sinu mollweide', 'sinusoidal', 'stereographic', 'times', 'transverse mercator', 'van der grinten', 'van der grinten2', 'van der grinten3', 'van der grinten4', 'wagner4', 'wagner6', 'wiechel', 'winkel tripel', 'winkel3']),
        **kwargs)