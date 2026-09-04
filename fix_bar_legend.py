with open("app/src/main/java/com/example/ui/views/BarChartView.kt", "r") as f:
    content = f.read()

content = content.replace("        // Selected Node Info", "        com.example.ui.components.SharedAssetLegend(settings)\n\n        // Selected Node Info")

with open("app/src/main/java/com/example/ui/views/BarChartView.kt", "w") as f:
    f.write(content)
