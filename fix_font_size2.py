import re

with open("app/src/main/java/com/example/ui/views/TreemapChartView.kt", "r") as f:
    content = f.read()

old_logic = r"""    // Text scaling proportional to area and dynamically responding to zoom \(وظیفه: تناسب با مساحت و زوم\)
    val nameFontSize = \(dimensionScale \* 0\.08f\)\.coerceIn\(4f, 48f\)\.sp
    val percentFontSize = \(dimensionScale \* 0\.10f\)\.coerceIn\(4\.5f, 54f\)\.sp
    val valueFontSize = \(dimensionScale \* 0\.06f\)\.coerceIn\(3\.5f, 32f\)\.sp
    val compactFontSize = \(dimensionScale \* 0\.07f\)\.coerceIn\(4f, 36f\)\.sp"""

new_logic = """    // Text scaling proportional to area and dynamically responding to zoom (وظیفه: تناسب با مساحت و زوم)
    val nameFontSize = (dimensionScale * 0.055f).coerceIn(4f, 36f).sp
    val percentFontSize = (dimensionScale * 0.07f).coerceIn(4.5f, 42f).sp
    val valueFontSize = (dimensionScale * 0.04f).coerceIn(3.5f, 24f).sp
    val compactFontSize = (dimensionScale * 0.05f).coerceIn(4f, 28f).sp"""

content = re.sub(old_logic, new_logic, content)

with open("app/src/main/java/com/example/ui/views/TreemapChartView.kt", "w") as f:
    f.write(content)
