import re

with open("app/src/main/java/com/example/ui/views/ModernTreeView.kt", "r") as f:
    content = f.read()

if "import com.example.ui.components.SharedViewHeader" not in content:
    content = content.replace("import com.example.utils.NumberFormatUtils", "import com.example.utils.NumberFormatUtils\nimport com.example.ui.components.SharedViewHeader")

# Replace the search toolbar item
item_regex = re.compile(r'item\(key = "modern_search_toolbar"\) \{.*?\n        \}', re.DOTALL)

replacement = """item(key = "modern_search_toolbar") {
            SharedViewHeader(
                activeView = activeView,
                settings = settings,
                onSelectView = onSelectView,
                searchQuery = searchQuery,
                onSearchChange = { searchQuery = it },
                sortConfig = sortConfig,
                onUpdateSort = onUpdateSort,
                onExpandAll = { expandAll(rootCalculated) },
                onCollapseAll = { collapseAll() },
                showSearchAndSort = true
            )
        }"""

content = item_regex.sub(replacement, content)

with open("app/src/main/java/com/example/ui/views/ModernTreeView.kt", "w") as f:
    f.write(content)

