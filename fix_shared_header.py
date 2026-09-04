with open("app/src/main/java/com/example/ui/components/SharedViewHeader.kt", "r") as f:
    content = f.read()

# Make the Search box transparent so it blends with the parent surface
old_colors = """                    colors = OutlinedTextFieldDefaults.colors(
                        focusedContainerColor = colors.inputBackground,
                        unfocusedContainerColor = colors.inputBackground,
                        focusedBorderColor = Color.Transparent,
                        unfocusedBorderColor = Color.Transparent,"""

new_colors = """                    colors = OutlinedTextFieldDefaults.colors(
                        focusedContainerColor = androidx.compose.ui.graphics.Color.Transparent,
                        unfocusedContainerColor = androidx.compose.ui.graphics.Color.Transparent,
                        focusedBorderColor = Color.Transparent,
                        unfocusedBorderColor = Color.Transparent,"""
content = content.replace(old_colors, new_colors)

# Also maybe they saw "نوع نمودار" and "مرتب سازی" in my previous code and now it's gone?
# Let's ensure there are no borders on the Surface itself (it has none, just shape and color).

with open("app/src/main/java/com/example/ui/components/SharedViewHeader.kt", "w") as f:
    f.write(content)
