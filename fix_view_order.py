import re
with open("app/src/main/java/com/example/data/model/Models.kt", "r") as f:
    content = f.read()

content = content.replace("AppViewMode.BAR_CHART,", "AppViewMode.BAR_CHART,\n        AppViewMode.PIE_CHART,")

with open("app/src/main/java/com/example/data/model/Models.kt", "w") as f:
    f.write(content)
