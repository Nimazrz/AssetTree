import re

with open("app/src/main/java/com/example/ui/views/TreemapChartView.kt", "r") as f:
    content = f.read()

# 1. Update the call to TreemapTileComposable
old_call = r"""                        TreemapTileComposable\(
                            tile = tile,
                            isSelected = selectedNode\?\.id == tile\.node\.id,
                            settings = settings,
                            onClick = \{ selectedNode = tile\.node \},
                            onDoubleClick = \{ onSelectNodeDetails\(tile\.node\) \}
                        \)"""

new_call = """                        TreemapTileComposable(
                            tile = tile,
                            isSelected = selectedNode?.id == tile.node.id,
                            settings = settings,
                            scale = scale,
                            onClick = { selectedNode = tile.node },
                            onDoubleClick = { onSelectNodeDetails(tile.node) }
                        )"""
content = re.sub(old_call, new_call, content)

# 2. Update the definition of TreemapTileComposable
old_def = r"""fun TreemapTileComposable\(
    tile: TreemapTile,
    isSelected: Boolean,
    settings: DisplaySettings,
    onClick: \(\) -> Unit,
    onDoubleClick: \(\) -> Unit
\) \{"""

new_def = """fun TreemapTileComposable(
    tile: TreemapTile,
    isSelected: Boolean,
    settings: DisplaySettings,
    scale: Float,
    onClick: () -> Unit,
    onDoubleClick: () -> Unit
) {"""
content = re.sub(old_def, new_def, content)

# 3. Update the font sizing and visibility logic inside TreemapTileComposable
old_logic = r"""    val tileArea = widthPx \* heightPx
    val dimensionScale = kotlin\.math\.sqrt\(tileArea\.toDouble\(\)\)\.toFloat\(\)

    // Dynamic font sizing strictly proportional to the tile area percentage \(وظیفه ۲\)
    val nameFontSize = \(dimensionScale \* 0\.125f\)\.coerceIn\(8\.5f, 28f\)\.sp
    val percentFontSize = \(dimensionScale \* 0\.155f\)\.coerceIn\(9\.5f, 32f\)\.sp
    val valueFontSize = \(dimensionScale \* 0\.085f\)\.coerceIn\(7\.5f, 18f\)\.sp
    val compactFontSize = \(dimensionScale \* 0\.10f\)\.coerceIn\(7\.5f, 11\.5f\)\.sp

    val showDetails = widthPx > 50f && heightPx > 34f
    val showCompactText = widthPx > 26f && heightPx > 16f
    val showValue = heightPx > 58f && widthPx > 65f"""

new_logic = """    val tileArea = widthPx * heightPx
    val dimensionScale = kotlin.math.sqrt(tileArea.toDouble()).toFloat()

    // Text scaling proportional to area and dynamically responding to zoom (وظیفه: تناسب با مساحت و زوم)
    val nameFontSize = (dimensionScale * 0.15f).coerceIn(2f, 100f).sp
    val percentFontSize = (dimensionScale * 0.18f).coerceIn(2.5f, 120f).sp
    val valueFontSize = (dimensionScale * 0.10f).coerceIn(1.5f, 80f).sp
    val compactFontSize = (dimensionScale * 0.12f).coerceIn(2f, 80f).sp

    val effectiveWidth = widthPx * scale
    val effectiveHeight = heightPx * scale

    val showDetails = effectiveWidth > 50f && effectiveHeight > 34f
    val showCompactText = effectiveWidth > 26f && effectiveHeight > 16f
    val showValue = effectiveHeight > 58f && effectiveWidth > 65f"""
content = re.sub(old_logic, new_logic, content)

with open("app/src/main/java/com/example/ui/views/TreemapChartView.kt", "w") as f:
    f.write(content)
