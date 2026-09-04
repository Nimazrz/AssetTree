import re

with open("app/src/main/java/com/example/utils/AssetColorUtils.kt", "r") as f:
    content = f.read()

# Add customColors parameter to getPaletteForNode
content = content.replace("fun getPaletteForNode(name: String, categoryTag: String? = null): AssetColorTheme {", 
                          "fun getPaletteForNode(name: String, categoryTag: String? = null, customColors: Map<String, Long> = emptyMap()): AssetColorTheme {")

# Add the logic for customColors at the very top of getPaletteForNode
custom_logic = """fun getPaletteForNode(name: String, categoryTag: String? = null, customColors: Map<String, Long> = emptyMap()): AssetColorTheme {
        val combined = "${name.lowercase()} ${categoryTag?.lowercase() ?: ""}"
        
        // 1. Check custom colors first
        val matchingCustomColor = customColors.entries.firstOrNull { combined.contains(it.key.lowercase()) }
        if (matchingCustomColor != null) {
            val p = Color(matchingCustomColor.value)
            return AssetColorTheme(
                primary = p,
                lightTint = p.copy(alpha=0.6f),
                darkShade = p.copy(alpha=0.9f),
                containerBgDark = p.copy(alpha=0.2f),
                containerBgLight = p.copy(alpha=0.15f),
                textOrIconColor = p
            )
        }
        
"""
content = content.replace("fun getPaletteForNode(name: String, categoryTag: String? = null, customColors: Map<String, Long> = emptyMap()): AssetColorTheme {\n        val combined = \"${name.lowercase()} ${categoryTag?.lowercase() ?: \"\"}\"", custom_logic)

# Update getNodeShadedColor
content = content.replace("fun getNodeShadedColor(", "fun getNodeShadedColor(\n        customColors: Map<String, Long> = emptyMap(),")
content = content.replace("val palette = getPaletteForNode(name, categoryTag)", "val palette = getPaletteForNode(name, categoryTag, customColors)")

with open("app/src/main/java/com/example/utils/AssetColorUtils.kt", "w") as f:
    f.write(content)

