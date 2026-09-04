package com.example.ui.components

import androidx.compose.foundation.background
import androidx.compose.foundation.clickable
import androidx.compose.foundation.layout.*
import androidx.compose.foundation.shape.RoundedCornerShape
import androidx.compose.material.icons.Icons
import androidx.compose.material.icons.filled.*
import androidx.compose.material3.*
import androidx.compose.runtime.*
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.hapticfeedback.HapticFeedbackType
import androidx.compose.ui.platform.LocalHapticFeedback
import androidx.compose.ui.unit.dp
import androidx.compose.ui.unit.sp
import androidx.compose.ui.text.font.FontWeight
import com.example.data.model.AppViewMode
import com.example.data.model.DisplaySettings
import com.example.data.model.SortConfig
import com.example.data.model.SortField
import com.example.ui.theme.AppTheme

@Composable
fun SharedViewHeader(
    activeView: AppViewMode,
    settings: DisplaySettings,
    onSelectView: (AppViewMode) -> Unit,
    searchQuery: String = "",
    onSearchChange: (String) -> Unit = {},
    sortConfig: SortConfig = SortConfig(),
    onUpdateSort: (SortConfig) -> Unit = {},
    onExpandAll: () -> Unit = {},
    onCollapseAll: () -> Unit = {},
    showSearchAndSort: Boolean = true
) {
    val colors = AppTheme.colors
    val haptic = LocalHapticFeedback.current
    var showChartDropdown by remember { mutableStateOf(false) }
    var showSortMenu by remember { mutableStateOf(false) }
    val viewModes = settings.customViewOrder.ifEmpty { AppViewMode.values().toList() }

    Surface(
        color = colors.surface,
        modifier = Modifier.fillMaxWidth().padding(horizontal = 8.dp, vertical = 4.dp)
    ) {
        Column(
            modifier = Modifier.fillMaxWidth().padding(8.dp),
            verticalArrangement = Arrangement.spacedBy(8.dp)
        ) {
            // Row 1: Chart Selector + Sort + Expand/Collapse
            Row(
                modifier = Modifier.fillMaxWidth(),
                horizontalArrangement = Arrangement.SpaceBetween,
                verticalAlignment = Alignment.CenterVertically
            ) {
                // Chart Selector (Left)
                Box {
                    Row(
                        verticalAlignment = Alignment.CenterVertically,
                        horizontalArrangement = Arrangement.spacedBy(4.dp),
                        modifier = Modifier
                            .clickable { showChartDropdown = true }
                            .padding(horizontal = 4.dp, vertical = 2.dp)
                    ) {
                        Icon(
                            imageVector = when (activeView) {
                                AppViewMode.TREEMAP -> Icons.Default.Dashboard
                                AppViewMode.CLASSIC_TREE -> Icons.Default.FormatListBulleted
                                AppViewMode.TREE -> Icons.Default.AccountTree
                                AppViewMode.CHART -> Icons.Default.PieChart
                                AppViewMode.BAR_CHART -> Icons.Default.BarChart
                                AppViewMode.ANALYTICS -> Icons.Default.Analytics
                            },
                            contentDescription = null,
                            tint = colors.primary,
                            modifier = Modifier.size(16.dp)
                        )
                        Text(
                            text = activeView.titleFa,
                            fontSize = 12.sp,
                            fontWeight = FontWeight.Bold,
                            color = colors.primary
                        )
                        Icon(
                            imageVector = Icons.Default.ArrowDropDown,
                            contentDescription = null,
                            tint = colors.primary,
                            modifier = Modifier.size(16.dp)
                        )
                    }

                    DropdownMenu(
                        expanded = showChartDropdown,
                        onDismissRequest = { showChartDropdown = false },
                        modifier = Modifier.background(colors.surface)
                    ) {
                        viewModes.forEach { mode ->
                            val isSelected = activeView == mode
                            DropdownMenuItem(
                                text = {
                                    Text(
                                        text = mode.titleFa,
                                        fontSize = 12.sp,
                                        fontWeight = if (isSelected) FontWeight.Bold else FontWeight.Normal,
                                        color = if (isSelected) colors.primary else colors.textPrimary
                                    )
                                },
                                onClick = {
                                    showChartDropdown = false
                                    haptic.performHapticFeedback(HapticFeedbackType.TextHandleMove)
                                    onSelectView(mode)
                                }
                            )
                        }
                    }
                }

                if (showSearchAndSort) {
                    // Sort (Middle-Right)
                    Box {
                        Row(
                            verticalAlignment = Alignment.CenterVertically,
                            horizontalArrangement = Arrangement.spacedBy(4.dp),
                            modifier = Modifier
                                .clickable { showSortMenu = true }
                                .padding(horizontal = 4.dp, vertical = 2.dp)
                        ) {
                            Icon(
                                imageVector = Icons.Default.Sort,
                                contentDescription = null,
                                tint = colors.primary,
                                modifier = Modifier.size(16.dp)
                            )
                            Text(
                                text = sortConfig.field.labelFa,
                                fontSize = 12.sp,
                                fontWeight = FontWeight.Bold,
                                color = colors.primary
                            )
                        }

                        DropdownMenu(
                            expanded = showSortMenu,
                            onDismissRequest = { showSortMenu = false },
                            modifier = Modifier.background(colors.surface)
                        ) {
                            SortField.values().forEach { field ->
                                val isSelected = sortConfig.field == field
                                DropdownMenuItem(
                                    text = { Text(field.labelFa, fontSize = 12.sp, color = colors.textPrimary) },
                                    onClick = {
                                        showSortMenu = false
                                        if (isSelected) {
                                            onUpdateSort(sortConfig.copy(direction = if (sortConfig.direction == com.example.data.model.SortDirection.ASC) com.example.data.model.SortDirection.DESC else com.example.data.model.SortDirection.ASC))
                                        } else {
                                            onUpdateSort(sortConfig.copy(field = field, direction = com.example.data.model.SortDirection.DESC))
                                        }
                                    },
                                    trailingIcon = if (isSelected) {
                                        {
                                            Icon(
                                                imageVector = if (sortConfig.direction == com.example.data.model.SortDirection.ASC) Icons.Default.ArrowUpward else Icons.Default.ArrowDownward,
                                                contentDescription = null,
                                                tint = colors.primary,
                                                modifier = Modifier.size(16.dp)
                                            )
                                        }
                                    } else null
                                )
                            }
                        }
                    }

                    // Expand / Collapse (Right)
                    Row(horizontalArrangement = Arrangement.spacedBy(4.dp)) {
                        IconButton(onClick = onExpandAll, modifier = Modifier.size(24.dp)) {
                            Icon(Icons.Default.UnfoldMore, contentDescription = "بسط دادن", tint = colors.primary, modifier = Modifier.size(16.dp))
                        }
                        IconButton(onClick = onCollapseAll, modifier = Modifier.size(24.dp)) {
                            Icon(Icons.Default.UnfoldLess, contentDescription = "جمع کردن", tint = colors.primary, modifier = Modifier.size(16.dp))
                        }
                    }
                }
            }

            // Row 2: Search (Only for tree views)
            if (showSearchAndSort) {
                OutlinedTextField(
                    value = searchQuery,
                    onValueChange = onSearchChange,
                    placeholder = { Text("جستجوی نماد، نام دارایی یا کد حسابداری...", fontSize = 11.sp, color = colors.textSecondary) },
                    textStyle = LocalTextStyle.current.copy(fontSize = 12.sp, color = colors.inputText),
                    singleLine = true,
                    leadingIcon = { Icon(Icons.Default.Search, contentDescription = "جستجو", tint = colors.primary, modifier = Modifier.size(16.dp)) },
                    trailingIcon = {
                        if (searchQuery.isNotEmpty()) {
                            IconButton(onClick = { onSearchChange("") }, modifier = Modifier.size(24.dp)) {
                                Icon(Icons.Default.Clear, contentDescription = "پاک کردن", tint = colors.textSecondary, modifier = Modifier.size(16.dp))
                            }
                        }
                    },
                    shape = RoundedCornerShape(10.dp),
                    colors = OutlinedTextFieldDefaults.colors(
                        focusedContainerColor = colors.inputBackground,
                        unfocusedContainerColor = colors.inputBackground,
                        focusedBorderColor = Color.Transparent,
                        unfocusedBorderColor = Color.Transparent,
                        cursorColor = colors.primary
                    ),
                    modifier = Modifier.fillMaxWidth().height(44.dp)
                )
            }
        }
    }
}
