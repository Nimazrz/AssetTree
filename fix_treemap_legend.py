with open("app/src/main/java/com/example/ui/views/TreemapChartView.kt", "r") as f:
    content = f.read()

content = content.replace("        // Selected Tile Inspector Bottom Card", "        com.example.ui.components.SharedAssetLegend(settings)\n\n        // Selected Tile Inspector Bottom Card")

with open("app/src/main/java/com/example/ui/views/TreemapChartView.kt", "w") as f:
    f.write(content)
