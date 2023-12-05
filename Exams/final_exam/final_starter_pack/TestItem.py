import unittest
from final import Item


class TestItem(unittest.TestCase):
    def setUp(self):
        self.cereal = Item("Frosted Flakes", 1, "05/10/2024")
        self.coffee = Item("Peets", 10, "10/15/2024")
        self.milk = Item("Milk", 2, "12/22/2023")
        self.eggs = Item("Eggs", 18.5, "12/12/2023")

    def test_set_get_quantity(self):
        self.assertEqual(1, self.cereal.get_quantity(), "Wrong Quantity")
        item = Item("Caviar", 0, "12/31/2023")
        self.assertEqual(0, item.get_quantity());
        item.set_quantity(10.9);
        self.assertEqual(10, item.get_quantity());
        item.set_quantity(10000);
        self.assertEqual(10000, item.get_quantity());
        self.assertEqual(18, self.eggs.get_quantity())

    def test_get_name(self):
        self.assertEqual("Frosted Flakes", self.cereal.get_name(), "Wrong name - Flakes")
        item = Item("Caviar", 0, "11/11/2024")
        self.assertEqual("CAVIAR", item.get_name().upper(), "Wrong name - caviar")

    def test_to_string(self):
        self.assertEqual("Frosted Flakes:1:05/10/2024", self.cereal.__str__())
        item = Item("Caviar", 0, "??/??/????")
        self.assertEqual("Caviar:0:??/??/????", item.__str__())

    def test_equals(self):
        self.assertEqual(self.cereal, self.cereal)
        self.assertNotEqual(self.cereal, self.coffee)
        milk = Item("mIlK", 2, "12/22/2023")
        eggs = Item("eggS", 18, "12/12/2023")
        self.assertEqual(milk, self.milk)
        self.assertEqual(eggs, self.eggs)

    def test_bad_quantity(self):
        with self.assertRaises(ValueError):
            item = Item("Evaporated Milk", -1, "11/11/1906")

    def test_set_bad_quantity(self):
        with self.assertRaises(ValueError):
            item = Item("Virtual Beef", 1, "12/12/2012")
            item.set_quantity(-10)

    def test_methods(self):
        if hasattr(self.cereal, "set_name") or hasattr(self.cereal, "setName") \
           or hasattr(self.cereal, "set_Name"):
                self.fail("Should NOT have a setter for name attribute!")


if __name__ == "__main__":
    unittest.main(verbosity=3)

