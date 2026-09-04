import re

with open("app/src/main/java/com/example/ui/views/ModernTreeView.kt", "r") as f:
    content = f.read()

start_index = content.find('item(key = "search_and_toolbar") {')
end_index = content.find('// 3. Tree Items List')

if start_index != -1 and end_index != -1:
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
        }
        
        """
    content = content[:start_index] + new_header + content[end_index:]
    with open("app/src/main/java/com/example/ui/views/ModernTreeView.kt", "w") as f:
        f.write(content)
    print("ModernTreeView updated successfully!")
else:
    print("Could not find start or end index.")
