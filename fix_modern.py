with open("app/src/main/java/com/example/ui/views/ModernTreeView.kt", "r") as f:
    content = f.read()

old_start = """    LazyColumn(
        modifier = Modifier
            .fillMaxSize()
            .testTag("modern_tree_list"),"""
new_start = """    Column(modifier = Modifier.fillMaxSize()) {
    LazyColumn(
        modifier = Modifier
            .fillMaxWidth()
            .weight(1f)
            .testTag("modern_tree_list"),"""
content = content.replace(old_start, new_start)

old_end = """        }
    }
}

@OptIn(ExperimentalFoundationApi::class)"""
new_end = """        }
    }
    com.example.ui.components.SharedAssetLegend(settings)
}
}

@OptIn(ExperimentalFoundationApi::class)"""
content = content.replace(old_end, new_end)

with open("app/src/main/java/com/example/ui/views/ModernTreeView.kt", "w") as f:
    f.write(content)
