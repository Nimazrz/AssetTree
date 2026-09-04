import re

with open("app/src/main/java/com/example/ui/dialogs/SettingsDialog.kt", "r") as f:
    content = f.read()

# Add imports if missing
if "import androidx.compose.material3.Tab" not in content:
    content = content.replace("import androidx.compose.material3.*", "import androidx.compose.material3.*\nimport androidx.compose.material3.TabRow\nimport androidx.compose.material3.Tab\nimport androidx.compose.material3.TabRowDefaults\nimport androidx.compose.material3.TabRowDefaults.tabIndicatorOffset")

# Insert TabRow and state
tabs_code = """
                var selectedTabIndex by remember { mutableStateOf(0) }
                val tabs = listOf("ظاهر و تم", "شخصی‌سازی", "داده و گزارش")

                TabRow(
                    selectedTabIndex = selectedTabIndex,
                    containerColor = colors.surfaceVariant,
                    contentColor = colors.primary,
                    indicator = { tabPositions ->
                        TabRowDefaults.Indicator(
                            Modifier.tabIndicatorOffset(tabPositions[selectedTabIndex]),
                            color = colors.primary
                        )
                    }
                ) {
                    tabs.forEachIndexed { index, title ->
                        Tab(
                            selected = selectedTabIndex == index,
                            onClick = { selectedTabIndex = index },
                            text = { Text(title, fontSize = 13.sp, fontWeight = if (selectedTabIndex == index) FontWeight.Bold else FontWeight.Normal) },
                            selectedContentColor = colors.primary,
                            unselectedContentColor = colors.textSecondary
                        )
                    }
                }

                // Body
"""
content = content.replace("                // Body\n", tabs_code)

# Now we need to wrap the sections inside the body Column.
# We will split the body by the Card comments.

body_start_idx = content.find("                Column(\n                    modifier = Modifier\n                        .fillMaxWidth()\n                        .weight(1f)\n                        .padding(16.dp)")

if body_start_idx != -1:
    # Find the closing brace of this column
    # Let's do it simply:
    # 1. Theme & Color Palette Card -> if (selectedTabIndex == 0) {
    content = content.replace("                    // 1. Theme & Color Palette Card", "                    if (selectedTabIndex == 0) {\n                    // 1. Theme & Color Palette Card")
    
    # 1.8 Customization of Chart ... is the last of Appearance? Wait, Chart & View Tabs Order is Display Customization.
    # So before 1.8 we close Tab 0 and open Tab 1.
    content = content.replace("                    // 1.8 Customization of Chart & View Tabs Order", "                    }\n                    if (selectedTabIndex == 1) {\n                    // 1.8 Customization of Chart & View Tabs Order")
    
    # Before 5. Data Backup & Restore we close Tab 1 and open Tab 2.
    # Wait, the PDF report is 7. Data backup is 5. Reset is 6. Wipe is 6.5.
    content = content.replace("                    // 5. Data Backup & Restore", "                    }\n                    if (selectedTabIndex == 2) {\n                    // 5. Data Backup & Restore")
    
    # And after the PDF Report generation card, we need to close Tab 2.
    # The end of the Column is before `    if (showResetConfirm) {`
    # Let's find the closing brace of the Column.
    end_of_column_marker = "    if (showResetConfirm) {"
    content = content.replace(end_of_column_marker, "                    }\n                }\n" + end_of_column_marker)
    # Wait, the `if (showResetConfirm) {` is outside the main `Dialog`? No, it's inside `SettingsDialog` but outside `Dialog`?
    # Let's check where `if (showResetConfirm)` is.
    
    # It is right after the `Dialog` block.
    # So the Column ends, then the `Card` ends, then the `Dialog` ends.
    # So there are three closing braces before `if (showResetConfirm) {`.
    
with open("app/src/main/java/com/example/ui/dialogs/SettingsDialog.kt", "w") as f:
    f.write(content)

print("Done")
