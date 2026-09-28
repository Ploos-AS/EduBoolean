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

    def test_signal_introspection(self):
        c = {"format":"edulogic-1","inputs":["A","B"],"outputs":["F"],"gates":[
          {"type":"AND","inputs":["A","B"],"output":"X"},
          {"type":"NOT","inputs":["X"],"output":"F"}]}
        self.assertEqual(edulogic.evaluate_signals(c, {"A":1,"B":0}), {"A":1,"B":0,"X":0,"F":1})

    def test_vector_suite(self):
        c = self.load_example("half-adder.json")
        suite = json.loads((ROOT / "examples" / "half-adder.vectors.json").read_text())
        self.assertTrue(all(r["ok"] for r in edulogic.run_vectors(c, suite)))

    def test_teaching_metadata_validation(self):
        c = self.load_example("half-adder.json")
        edulogic.validate(c)

    def test_order_independent_gate_list(self):
        c={"format":"edulogic-1","inputs":["A","B"],"outputs":["F"],"gates":[
          {"type":"NOT","inputs":["X"],"output":"F"},
          {"type":"AND","inputs":["A","B"],"output":"X"}]}
        self.assertEqual(edulogic.evaluate(c,{"A":1,"B":1}),{"F":0})

    def test_dff_tick_samples_atomically(self):
        c = self.load_example("counter2.json")
        self.assertEqual(edulogic.initial_state(c), {"Q1":0,"Q0":0})
        self.assertEqual(edulogic.tick(c, {}, {"Q1":0,"Q0":0}), {"Q1":0,"Q0":1})
        self.assertEqual(edulogic.tick(c, {}, {"Q1":0,"Q0":1}), {"Q1":1,"Q0":0})

    def test_counter2_sequence(self):
        c = self.load_example("counter2.json")
        self.assertEqual(edulogic.run_ticks(c, 8), [
            {"Q1":0,"Q0":0}, {"Q1":0,"Q0":1}, {"Q1":1,"Q0":0},
            {"Q1":1,"Q0":1}, {"Q1":0,"Q0":0}, {"Q1":0,"Q0":1},
            {"Q1":1,"Q0":0}, {"Q1":1,"Q0":1}, {"Q1":0,"Q0":0}
        ])

    def test_counter_enable_reset_sequence(self):
        c = self.load_example("counter4-control.json")
        suite = json.loads((ROOT / "examples" / "counter4-control.sequence.json").read_text())
        results = edulogic.run_sequence(c, suite)
        self.assertTrue(all(r["ok"] for r in results))

    def test_register_load_enable_reset(self):
        c={"format":"edulogic-1","inputs":["D0","D1","EN","RST"],"outputs":["Q[0]","Q[1]"],
           "state":[{"type":"REGISTER","q":"Q","width":2,"d":["D0","D1"],"enable":"EN","reset":"RST"}],
           "gates":[]}
        s=edulogic.initial_state(c)
        s=edulogic.tick(c,{"D0":1,"D1":1,"EN":1,"RST":0},s)
        self.assertEqual(s,{"Q[0]":1,"Q[1]":1})
        s=edulogic.tick(c,{"D0":0,"D1":0,"EN":0,"RST":0},s)
        self.assertEqual(s,{"Q[0]":1,"Q[1]":1})
        s=edulogic.tick(c,{"D0":1,"D1":1,"EN":0,"RST":1},s)
        self.assertEqual(s,{"Q[0]":0,"Q[1]":0})

    def test_cycle_is_rejected(self):
        c={"format":"edulogic-1","inputs":["A"],"outputs":["F"],"gates":[
          {"type":"AND","inputs":["A","F"],"output":"F"}]}
        with self.assertRaises(ValueError):
            edulogic.evaluate(c,{"A":1})

if __name__ == "__main__":
    unittest.main()
