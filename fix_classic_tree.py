import re

with open("app/src/main/java/com/example/ui/views/ClassicTreeView.kt", "r") as f:
    content = f.read()

# We need to replace the Card for search/sort with a call to SharedViewHeader
# Let's find the exact block.

# First add import:
if "import com.example.ui.components.SharedViewHeader" not in content:
    content = content.replace("import com.example.utils.NumberFormatUtils", "import com.example.utils.NumberFormatUtils\nimport com.example.ui.components.SharedViewHeader")

# Replace the search toolbar item
# We'll regex match the `item(key = "classic_search_toolbar") { ... }` block
# and replace it with SharedViewHeader

item_regex = re.compile(r'item\(key = "classic_search_toolbar"\) \{.*?\n        \}', re.DOTALL)

replacement = """item(key = "classic_search_toolbar") {
            SharedViewHeader(
                activeView = activeView,
                settings = settings,
                onSelectView = onSelectView,
                searchQuery = searchQuery,
                onSearchChange = { searchQuery = it },
                sortConfig = sortConfig,
                onUpdateSort = onUpdateSort,
                onExpandAll = { 
                    fun expandAll(node: CalculatedNode) {
                        expandedNodeIds[node.id] = true
                        node.children.forEach { expandAll(it) }
                    }
                    expandAll(rootCalculated)
                },
                onCollapseAll = { expandedNodeIds.clear() },
                showSearchAndSort = true
            )
        }"""

content = item_regex.sub(replacement, content)

with open("app/src/main/java/com/example/ui/views/ClassicTreeView.kt", "w") as f:
    f.write(content)

