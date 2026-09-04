with open("app/src/main/java/com/example/MainActivity.kt", "r") as f:
    content = f.read()

old_bar = """                        AppViewMode.BAR_CHART -> {
                            BarChartView(
                                activeView = activeView,
                                onSelectView = { viewModel.setActiveView(it) },
                                rootCalculated = root,
                                settings = displaySettings,
                                onSelectNodeDetails = { viewModel.setDetailsNode(it) }
                            )
                        }"""

new_bar = """                        AppViewMode.BAR_CHART -> {
                            BarChartView(
                                activeView = activeView,
                                onSelectView = { viewModel.setActiveView(it) },
                                rootCalculated = root,
                                settings = displaySettings,
                                onSelectNodeDetails = { viewModel.setDetailsNode(it) }
                            )
                        }
                        AppViewMode.PIE_CHART -> {
                            PieChartView(
                                activeView = activeView,
                                onSelectView = { viewModel.setActiveView(it) },
                                rootCalculated = root,
                                settings = displaySettings,
                                onSelectNodeDetails = { viewModel.setDetailsNode(it) }
                            )
                        }"""

content = content.replace(old_bar, new_bar)

with open("app/src/main/java/com/example/MainActivity.kt", "w") as f:
    f.write(content)
