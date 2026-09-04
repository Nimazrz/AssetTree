import re
with open("app/src/main/java/com/example/ui/views/ClassicTreeView.kt", "r") as f:
    content = f.read()

# I will find "@OptIn(ExperimentalFoundationApi::class)" and replace it to add the missing brace for the function
content = content.replace("    com.example.ui.components.SharedAssetLegend(settings)\n}\n\n@OptIn", "    com.example.ui.components.SharedAssetLegend(settings)\n}\n}\n\n@OptIn")

# And wait, the other error was: Unresolved reference 'ClassicTreeNodeRow'. That was because the parsing broke.
# There was also `TreeBranchLines` syntax error? "Syntax error: Expecting '}' at 464".
# Let's check line 464 in ClassicTreeView.kt.
