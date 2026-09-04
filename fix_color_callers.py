import os

files_to_check = [
    "app/src/main/java/com/example/ui/views/ClassicTreeView.kt",
    "app/src/main/java/com/example/ui/views/ModernTreeView.kt",
    "app/src/main/java/com/example/ui/views/SunburstChartView.kt",
    "app/src/main/java/com/example/ui/views/BarChartView.kt",
    "app/src/main/java/com/example/ui/views/TreemapChartView.kt"
]

for file_path in files_to_check:
    with open(file_path, "r") as f:
        content = f.read()
    
    # getNodeShadedColor(node.name -> getNodeShadedColor(settings.customAssetColors, node.name
    content = content.replace("AssetColorUtils.getNodeShadedColor(node.name", "AssetColorUtils.getNodeShadedColor(settings.customAssetColors, node.name")
    # Sunburst has it slightly different maybe?
    content = content.replace("AssetColorUtils.getNodeShadedColor(\n                                    node.name", "AssetColorUtils.getNodeShadedColor(\n                                    settings.customAssetColors,\n                                    node.name")
    content = content.replace("AssetColorUtils.getNodeShadedColor(\n                                categoryName", "AssetColorUtils.getNodeShadedColor(\n                                settings.customAssetColors,\n                                categoryName")
    content = content.replace("AssetColorUtils.getNodeShadedColor(categoryName", "AssetColorUtils.getNodeShadedColor(settings.customAssetColors, categoryName")
    
    # Treemap getPaletteForNode
    content = content.replace("AssetColorUtils.getPaletteForNode(categoryNode.name, categoryNode.categoryTag)", "AssetColorUtils.getPaletteForNode(categoryNode.name, categoryNode.categoryTag, settings.customAssetColors)")
    
    with open(file_path, "w") as f:
        f.write(content)

