package com.example

import android.content.Context
import androidx.test.core.app.ApplicationProvider
import com.example.core.TreeEngine
import com.example.data.local.ROOT_NODE_ID
import com.example.data.model.StoredNodeEntity
import org.junit.Assert.assertEquals
import org.junit.Test
import org.junit.runner.RunWith
import org.robolectric.RobolectricTestRunner
import org.robolectric.annotation.Config

@RunWith(RobolectricTestRunner::class)
@Config(sdk = [36])
class ExampleRobolectricTest {

    @Test
    fun `read string from context`() {
        val context = ApplicationProvider.getApplicationContext<Context>()
        val appName = context.getString(R.string.app_name)
        assertEquals("AssetTree", appName)
    }

    @Test
    fun `tree calculation rolls up values accurately`() {
        val nodes = listOf(
            StoredNodeEntity(id = ROOT_NODE_ID, name = "کل دارایی‌ها", parentId = null, quantity = 1.0, unit = "سبد", unitPrice = 0.0),
            StoredNodeEntity(id = "group1", name = "سهام", parentId = ROOT_NODE_ID, quantity = 1.0, unit = "گروه", unitPrice = 0.0),
            StoredNodeEntity(id = "leaf1", name = "فولاد", parentId = "group1", quantity = 100.0, unit = "سهم", unitPrice = 5000.0),
            StoredNodeEntity(id = "leaf2", name = "فملی", parentId = "group1", quantity = 200.0, unit = "سهم", unitPrice = 3000.0)
        )

        val result = TreeEngine.evaluateTree(nodes)
        val root = result.rootCalculated
        // leaf1 = 500,000, leaf2 = 600,000 => total group1 = 1,100,000 => root = 1,100,000
        assertEquals(1100000.0, root.totalValue, 0.001)
        assertEquals(3, root.childCount)
        assertEquals(2, root.children[0].childCount)
    }
}
