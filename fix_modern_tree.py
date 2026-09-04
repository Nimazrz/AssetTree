import re

with open("app/src/main/java/com/example/ui/views/ModernTreeView.kt", "r") as f:
    content = f.read()

# Replace the Card header with SharedViewHeader
# The Card starts at item(key = "search_and_toolbar") {
card_pattern = r'item\(key = "search_and_toolbar"\) \{.*?Card\([\s\S]*?\}\s*\)\s*\}\s*\}'
new_header = """item(key = "search_and_toolbar") {
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
content = re.sub(card_pattern, new_header, content)

with open("app/src/main/java/com/example/ui/views/ModernTreeView.kt", "w") as f:
    f.write(content)
