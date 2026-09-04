with open("app/src/main/java/com/example/ui/views/TreemapChartView.kt", "r") as f:
    content = f.read()

bad_def = """private fun computeTreemapLayout(
            customAssetColors = settings.customAssetColors,
    customAssetColors: Map<String, Long>,"""
good_def = """private fun computeTreemapLayout(
    customAssetColors: Map<String, Long>,"""
content = content.replace(bad_def, good_def)

# Also let's check the call site
bad_call = """computeTreemapLayout(
            customAssetColors = settings.customAssetColors,
            customAssetColors = settings.customAssetColors,"""
good_call = """computeTreemapLayout(
            customAssetColors = settings.customAssetColors,"""
content = content.replace(bad_call, good_call)

with open("app/src/main/java/com/example/ui/views/TreemapChartView.kt", "w") as f:
    f.write(content)
