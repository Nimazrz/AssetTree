with open("app/src/main/java/com/example/ui/dialogs/SettingsDialog.kt", "r") as f:
    content = f.read()

if "import androidx.compose.material3.Tab" not in content:
    content = content.replace("import androidx.compose.material3.*", "import androidx.compose.material3.*\nimport androidx.compose.material3.TabRow\nimport androidx.compose.material3.Tab\nimport androidx.compose.material3.TabRowDefaults\nimport androidx.compose.material3.TabRowDefaults.tabIndicatorOffset")

tabs_code = """
                var selectedTabIndex by remember { mutableStateOf(0) }
                val tabs = listOf("پوسته و ظاهر", "تنظیمات نمایش", "داده و بک‌آپ")

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

content = content.replace("                    // 1. Theme & Color Palette Card", "                    if (selectedTabIndex == 0) {\n                    // 1. Theme & Color Palette Card")
content = content.replace("                    // 1.8 Customization of Chart", "                    }\n                    if (selectedTabIndex == 1) {\n                    // 1.8 Customization of Chart")
content = content.replace("                    // 5. Data Backup & Restore", "                    }\n                    if (selectedTabIndex == 2) {\n                    // 5. Data Backup & Restore")

# We need to find where to put the final closing brace for `if (selectedTabIndex == 2) {`
# It should be right after the end of the PDF report card, before the `}` that closes the Column containing the cards.
# Let's find the string:
target = """                            }
                        }
                    }
                }
            }
        }
    }

    if (showResetConfirm) {"""
# The 5th closing brace is the card, 6th is the column, 7th is dialog.
# We want to put `                    }\n` before the 6th closing brace.
replacement = """                            }
                        }
                    }
                }
            }
                    }
        }
    }

    if (showResetConfirm) {"""
content = content.replace(target, replacement)

with open("app/src/main/java/com/example/ui/dialogs/SettingsDialog.kt", "w") as f:
    f.write(content)

print("Done")
