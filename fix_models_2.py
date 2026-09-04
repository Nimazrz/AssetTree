import re
with open("app/src/main/java/com/example/data/model/Models.kt", "r") as f:
    content = f.read()

content = content.replace("    )\n)\n\nenum class SortField", "    ),\n    val customAssetColors: Map<String, Long> = emptyMap()\n)\n\nenum class SortField")

with open("app/src/main/java/com/example/data/model/Models.kt", "w") as f:
    f.write(content)
