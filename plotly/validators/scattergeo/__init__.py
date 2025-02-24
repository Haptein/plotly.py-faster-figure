import sys
from _plotly_utils.importers import relative_import

__all__, __getattr__, __dir__ = relative_import(
    __name__,
    [],
    [
        "._visible.VisibleValidator",
        "._unselected.UnselectedValidator",
        "._uirevision.UirevisionValidator",
        "._uid.UidValidator",
        "._texttemplatesrc.TexttemplatesrcValidator",
        "._texttemplate.TexttemplateValidator",
        "._textsrc.TextsrcValidator",
        "._textpositionsrc.TextpositionsrcValidator",
        "._textposition.TextpositionValidator",
        "._textfont.TextfontValidator",
        "._text.TextValidator",
        "._stream.StreamValidator",
        "._showlegend.ShowlegendValidator",
        "._selectedpoints.SelectedpointsValidator",
        "._selected.SelectedValidator",
        "._opacity.OpacityValidator",
        "._name.NameValidator",
        "._mode.ModeValidator",
        "._metasrc.MetasrcValidator",
        "._meta.MetaValidator",
        "._marker.MarkerValidator",
        "._lonsrc.LonsrcValidator",
        "._lon.LonValidator",
        "._locationssrc.LocationssrcValidator",
        "._locations.LocationsValidator",
        "._locationmode.LocationmodeValidator",
        "._line.LineValidator",
        "._legendwidth.LegendwidthValidator",
        "._legendrank.LegendrankValidator",
        "._legendgrouptitle.LegendgrouptitleValidator",
        "._legendgroup.LegendgroupValidator",
        "._legend.LegendValidator",
        "._latsrc.LatsrcValidator",
        "._lat.LatValidator",
        "._idssrc.IdssrcValidator",
        "._ids.IdsValidator",
        "._hovertextsrc.HovertextsrcValidator",
        "._hovertext.HovertextValidator",
        "._hovertemplatesrc.HovertemplatesrcValidator",
        "._hovertemplate.HovertemplateValidator",
        "._hoverlabel.HoverlabelValidator",
        "._hoverinfosrc.HoverinfosrcValidator",
        "._hoverinfo.HoverinfoValidator",
        "._geojson.GeojsonValidator",
        "._geo.GeoValidator",
        "._fillcolor.FillcolorValidator",
        "._fill.FillValidator",
        "._featureidkey.FeatureidkeyValidator",
        "._customdatasrc.CustomdatasrcValidator",
        "._customdata.CustomdataValidator",
        "._connectgaps.ConnectgapsValidator",
    ],
)
