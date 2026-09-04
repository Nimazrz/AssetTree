import re

with open("app/src/main/java/com/example/ui/views/TreemapChartView.kt", "r") as f:
    content = f.read()

bad_pan = r'offset = \(offset \+ centroid - pan\) \* fraction - centroid[\s\S]*?y = offset\.y\.coerceIn\(-maxY, maxY\)\n                            \)'
good_pan = """offset = androidx.compose.ui.geometry.Offset(
                                x = offset.x + pan.x,
                                y = offset.y + pan.y
                            )
                            val maxX = (scale - 1) * totalWidth / 2
                            val maxY = (scale - 1) * totalHeight / 2
                            offset = androidx.compose.ui.geometry.Offset(
                                x = offset.x.coerceIn(-maxX, maxX),
                                y = offset.y.coerceIn(-maxY, maxY)
                            )"""

content = re.sub(bad_pan, good_pan, content)
content = content.replace("translationX = -offset.x\n                        translationY = -offset.y", "translationX = offset.x\n                        translationY = offset.y")

with open("app/src/main/java/com/example/ui/views/TreemapChartView.kt", "w") as f:
    f.write(content)
