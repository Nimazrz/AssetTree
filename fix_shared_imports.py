with open("app/src/main/java/com/example/ui/components/SharedViewHeader.kt", "r") as f:
    content = f.read()

content = content.replace("import androidx.compose.ui.draw.clip\nimport androidx.compose.foundation.shape.CircleShape\npackage com.example.ui.components\n", "package com.example.ui.components\n\nimport androidx.compose.ui.draw.clip\nimport androidx.compose.foundation.shape.CircleShape\nimport androidx.compose.foundation.horizontalScroll\nimport androidx.compose.foundation.rememberScrollState\n")

with open("app/src/main/java/com/example/ui/components/SharedViewHeader.kt", "w") as f:
    f.write(content)
