with open("app/src/main/java/com/example/MainActivity.kt", "r") as f:
    content = f.read()

content = content.replace(
    "ModernTreeView(\n                                rootCalculated = root",
    "ModernTreeView(\n                                activeView = activeView,\n                                onSelectView = { viewModel.setActiveView(it) },\n                                rootCalculated = root"
)

content = content.replace(
    "ClassicTreeView(\n                                rootCalculated = root",
    "ClassicTreeView(\n                                activeView = activeView,\n                                onSelectView = { viewModel.setActiveView(it) },\n                                rootCalculated = root"
)

with open("app/src/main/java/com/example/MainActivity.kt", "w") as f:
    f.write(content)

