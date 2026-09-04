import re

with open("app/src/main/java/com/example/data/model/Models.kt", "r") as f:
    content = f.read()

# Add PIE_CHART
content = content.replace("BAR_CHART(\"میله ای\"),", "BAR_CHART(\"میله ای\"),\n    PIE_CHART(\"دایره ای\"),")

# Remove AMOLED_NIGHT
content = re.sub(r'\s*AMOLED_NIGHT[^,]*,', '', content)

# Add customAssetColors to DisplaySettings
if "val customAssetColors: Map<String, Long> = emptyMap()" not in content:
    content = content.replace("val customViewOrder: List<AppViewMode> = emptyList(),", "val customViewOrder: List<AppViewMode> = emptyList(),\n    val customAssetColors: Map<String, Long> = emptyMap(),")

with open("app/src/main/java/com/example/data/model/Models.kt", "w") as f:
    f.write(content)
