# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):
    def test_foo(self):
        items = [Item("foo", 0, 0)]
    # example of test that checks for logical errors
    def test_sulfuras_should_not_decrease_quality(self):
        items = [Item("Sulfuras", 5, 80)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals("fixme", items[0].name)
        sulfuras_item = items[0]
        self.assertEquals(80, sulfuras_item.quality)
        self.assertEquals(4, sulfuras_item.sell_in)
        self.assertEquals("Sulfuras", sulfuras_item.name)
    def test_gilded_rose_list_all_items(self):
        items = [Item("Sulfuras", 5, 80)]
        gilded_rose = GildedRose(items)
        all_items = gilded_rose.get_items()
        self.assertEquals(["Sulfuras"], all_items)

    def test_normal_item_degrades_by_2(self):
        items = [Item("normal item", 10, 20)]
        gr = GildedRose(items)
        gr.update_quality()
        self.assertEqual(items[0].quality, 18,
                         f"Expected quality of 18, got {items[0].quality}"
                         )

    def test_aged_brie_decreases_in_quality(self):
        items = [Item("Aged Brie", 5, 10)]
        gr = GildedRose(items)
        gr.update_quality()
        self.assertEqual(items[0].quality, 9,
                         f"Expected quality of 9, got {items[0].quality}"
                         )

    def test_backstage_pass_quality_remains_same_past_concert(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 0, 20)]
        gr = GildedRose(items)
        gr.update_quality()
        self.assertEqual(items[0].quality, 20,
                         f"Expected quality of 20, got {items[0].quality}"
                         )

    def test_syntax_error(self):
        eval("1=1")


if __name__ == '__main__':
    unittest.main()
