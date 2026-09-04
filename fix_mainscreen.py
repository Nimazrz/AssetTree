import re

with open("app/src/main/java/com/example/ui/screens/MainScreen.kt", "r") as f:
    content = f.read()

content = content.replace("import com.example.ui.views.TreemapChartView", "import com.example.ui.views.TreemapChartView\nimport com.example.ui.views.PieChartView")

view_logic = """                    AppViewMode.BAR_CHART -> {
                        BarChartView(
                            activeView = activeView,
                            onSelectView = { activeView = it },
                            rootCalculated = rootCalculated,
                            settings = displaySettings,
                            onSelectNodeDetails = { node ->
                                selectedNodeForDetails = node.id
                            }
                        )
                    }
                    AppViewMode.PIE_CHART -> {
                        PieChartView(
                            activeView = activeView,
                            onSelectView = { activeView = it },
                            rootCalculated = rootCalculated,
                            settings = displaySettings,
                            onSelectNodeDetails = { node ->
                                selectedNodeForDetails = node.id
                            }
                        )
                    }"""

content = content.replace("""                    AppViewMode.BAR_CHART -> {
                        BarChartView(
                            activeView = activeView,
                            onSelectView = { activeView = it },
                            rootCalculated = rootCalculated,
                            settings = displaySettings,
                            onSelectNodeDetails = { node ->
                                selectedNodeForDetails = node.id
                            }
                        )
                    }""", view_logic)

with open("app/src/main/java/com/example/ui/screens/MainScreen.kt", "w") as f:
    f.write(content)
