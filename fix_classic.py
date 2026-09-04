with open("app/src/main/java/com/example/ui/views/ClassicTreeView.kt", "r") as f:
    content = f.read()

old_box = """    Box(
        modifier = Modifier
            .fillMaxSize()
            .horizontalScroll(horizontalScrollState)
    ) {"""

new_box = """    Column(modifier = Modifier.fillMaxSize()) {
    Box(
        modifier = Modifier
            .weight(1f)
            .horizontalScroll(horizontalScrollState)
    ) {"""
content = content.replace(old_box, new_box)

old_end = """        }
    }
}
}

@OptIn(ExperimentalFoundationApi::class)"""
new_end = """        }
    }
}
    com.example.ui.components.SharedAssetLegend(settings)
}

@OptIn(ExperimentalFoundationApi::class)"""
content = content.replace(old_end, new_end)

with open("app/src/main/java/com/example/ui/views/ClassicTreeView.kt", "w") as f:
    f.write(content)
