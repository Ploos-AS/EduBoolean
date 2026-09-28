import json
import unittest
from pathlib import Path
import edulogic

ROOT = Path(__file__).parent

class EduLogicTests(unittest.TestCase):
    def load_example(self, name):
        return json.loads((ROOT / "examples" / name).read_text())

    def test_gate_truths(self):
        c = self.load_example("all-gates.json")
        self.assertEqual(edulogic.evaluate(c, {"A": 0, "B": 0}),
            {"NOT_A":1,"AND":0,"OR":0,"XOR":0,"NAND":1,"NOR":1,"XNOR":1})
        self.assertEqual(edulogic.evaluate(c, {"A": 1, "B": 0}),
            {"NOT_A":0,"AND":0,"OR":1,"XOR":1,"NAND":1,"NOR":0,"XNOR":0})
        self.assertEqual(edulogic.evaluate(c, {"A": 1, "B": 1}),
            {"NOT_A":0,"AND":1,"OR":1,"XOR":0,"NAND":0,"NOR":0,"XNOR":1})

    def test_half_adder_truth_table(self):
        c = self.load_example("half-adder.json")
        got = [(tuple(x.values()), tuple(y.values())) for x,y in edulogic.truth_table(c)]
        self.assertEqual(got, [
            ((0,0),(0,0)), ((0,1),(1,0)),
            ((1,0),(1,0)), ((1,1),(0,1))
        ])

    def test_order_independent_gate_list(self):
        c={"format":"edulogic-1","inputs":["A","B"],"outputs":["F"],"gates":[
          {"type":"NOT","inputs":["X"],"output":"F"},
          {"type":"AND","inputs":["A","B"],"output":"X"}]}
        self.assertEqual(edulogic.evaluate(c,{"A":1,"B":1}),{"F":0})

    def test_cycle_is_rejected(self):
        c={"format":"edulogic-1","inputs":["A"],"outputs":["F"],"gates":[
          {"type":"AND","inputs":["A","F"],"output":"F"}]}
        with self.assertRaises(ValueError):
            edulogic.evaluate(c,{"A":1})

if __name__ == "__main__":
    unittest.main()
