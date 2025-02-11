import sys
from _plotly_utils.importers import relative_import

__all__, __getattr__, __dir__ = relative_import(
    __name__,
    [],
    [
        "._yhoverformat.YhoverformatValidator",
        "._yaxes.YaxesValidator",
        "._xhoverformat.XhoverformatValidator",
        "._xaxes.XaxesValidator",
        "._visible.VisibleValidator",
        "._unselected.UnselectedValidator",
        "._uirevision.UirevisionValidator",
        "._uid.UidValidator",
        "._textsrc.TextsrcValidator",
        "._text.TextValidator",
        "._stream.StreamValidator",
        "._showupperhalf.ShowupperhalfValidator",
        "._showlowerhalf.ShowlowerhalfValidator",
        "._showlegend.ShowlegendValidator",
        "._selectedpoints.SelectedpointsValidator",
        "._selected.SelectedValidator",
        "._opacity.OpacityValidator",
        "._name.NameValidator",
        "._metasrc.MetasrcValidator",
        "._meta.MetaValidator",
        "._marker.MarkerValidator",
        "._legendwidth.LegendwidthValidator",
        "._legendrank.LegendrankValidator",
        "._legendgrouptitle.LegendgrouptitleValidator",
        "._legendgroup.LegendgroupValidator",
        "._legend.LegendValidator",
        "._idssrc.IdssrcValidator",
        "._ids.IdsValidator",
        "._hovertextsrc.HovertextsrcValidator",
        "._hovertext.HovertextValidator",
        "._hovertemplatesrc.HovertemplatesrcValidator",
        "._hovertemplate.HovertemplateValidator",
        "._hoverlabel.HoverlabelValidator",
        "._hoverinfosrc.HoverinfosrcValidator",
        "._hoverinfo.HoverinfoValidator",
        "._dimensiondefaults.DimensiondefaultsValidator",
        "._dimensions.DimensionsValidator",
        "._diagonal.DiagonalValidator",
        "._customdatasrc.CustomdatasrcValidator",
        "._customdata.CustomdataValidator",
    ],
)
