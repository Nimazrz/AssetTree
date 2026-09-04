import re

with open("app/src/main/java/com/example/ui/views/TreemapChartView.kt", "r") as f:
    content = f.read()

# Add necessary imports
imports = """import androidx.compose.ui.input.pointer.pointerInput
import androidx.compose.foundation.gestures.detectTransformGestures
import androidx.compose.ui.graphics.graphicsLayer
"""
content = content.replace("import androidx.compose.ui.Modifier", imports + "import androidx.compose.ui.Modifier")

# Find the main Box holding the map tiles
box_start = r'        BoxWithConstraints\(modifier = Modifier\n            \.fillMaxWidth\(\)\n            \.weight\(1f\)\) \{'

new_box = """        BoxWithConstraints(modifier = Modifier
            .fillMaxWidth()
            .weight(1f)
            .clip(RoundedCornerShape(12.dp))) {
            
            val totalWidth = constraints.maxWidth.toFloat()
            val totalHeight = constraints.maxHeight.toFloat()
            
            var scale by remember { mutableStateOf(1f) }
            var offset by remember { mutableStateOf(androidx.compose.ui.geometry.Offset.Zero) }

            Box(
                modifier = Modifier
                    .fillMaxSize()
                    .pointerInput(Unit) {
                        detectTransformGestures { centroid, pan, zoom, _ ->
                            val oldScale = scale
                            scale = (scale * zoom).coerceIn(1f, 5f)
                            val fraction = (scale / oldScale)
                            offset = (offset + centroid - pan) * fraction - centroid
                            
                            // Bounds calculation
                            val maxX = (scale - 1) * totalWidth / 2
                            val maxY = (scale - 1) * totalHeight / 2
                            offset = androidx.compose.ui.geometry.Offset(
                                x = offset.x.coerceIn(-maxX, maxX),
                                y = offset.y.coerceIn(-maxY, maxY)
                            )
                        }
                    }
                    .graphicsLayer {
                        scaleX = scale
                        scaleY = scale
                        translationX = -offset.x
                        translationY = -offset.y
                    }
            ) {"""

content = re.sub(box_start, new_box, content)
content = content.replace("val totalWidth = constraints.maxWidth.toFloat()\n            val totalHeight = constraints.maxHeight.toFloat()", "") # Remove duplicates since I added them up top.

# I need to find where the BoxWithConstraints ends. 
# It's at the end of the file. So I'll add an extra `}` just before the `if (selectedTile != null)` dialog.
end_dialog = r'        if \(selectedTile != null\) \{'
content = re.sub(end_dialog, "            }\n" + end_dialog, content)

with open("app/src/main/java/com/example/ui/views/TreemapChartView.kt", "w") as f:
    f.write(content)

