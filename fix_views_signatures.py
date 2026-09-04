import os
import re

views = [
    "app/src/main/java/com/example/ui/views/TreemapChartView.kt",
    "app/src/main/java/com/example/ui/views/SunburstChartView.kt",
    "app/src/main/java/com/example/ui/views/BarChartView.kt",
    "app/src/main/java/com/example/ui/views/AnalyticsDashboardView.kt"
]

for view in views:
    with open(view, "r") as f:
        content = f.read()

    if "SharedViewHeader(activeView" not in content:
        # Just replace the first "    Column(" with "    Column(\n        SharedViewHeader(activeView = activeView, onSelectView = onSelectView, settings = settings, showSearchAndSort = false)"
        content = content.replace("    Column(\n", "    Column(\n        SharedViewHeader(activeView = activeView, onSelectView = onSelectView, settings = settings, showSearchAndSort = false)\n", 1)

    with open(view, "w") as f:
        f.write(content)

