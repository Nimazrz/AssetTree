with open("app/src/main/java/com/example/MainActivity.kt", "r") as f:
    content = f.read()

content = content.replace(
    "SunburstChartView(\n                                rootNode = root",
    "SunburstChartView(\n                                activeView = activeView,\n                                onSelectView = { viewModel.setActiveView(it) },\n                                rootNode = root"
)

content = content.replace(
    "BarChartView(\n                                rootCalculated = root",
    "BarChartView(\n                                activeView = activeView,\n                                onSelectView = { viewModel.setActiveView(it) },\n                                rootCalculated = root"
)

content = content.replace(
    "TreemapChartView(\n                                rootCalculated = root",
    "TreemapChartView(\n                                activeView = activeView,\n                                onSelectView = { viewModel.setActiveView(it) },\n                                rootCalculated = root"
)

content = content.replace(
    "AnalyticsDashboardView(\n                                rootCalculated = root",
    "AnalyticsDashboardView(\n                                activeView = activeView,\n                                onSelectView = { viewModel.setActiveView(it) },\n                                rootCalculated = root"
)

with open("app/src/main/java/com/example/MainActivity.kt", "w") as f:
    f.write(content)

