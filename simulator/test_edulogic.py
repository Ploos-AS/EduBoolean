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

    def test_stateful_validation(self):
        edulogic.validate(self.load_example("counter2.json"))
        edulogic.validate(self.load_example("counter4-control.json"))

    def test_duplicate_inputs_rejected(self):
        c={"format":"edulogic-1","inputs":["A","A"],"outputs":["A"],"gates":[]}
        with self.assertRaises(ValueError): edulogic.validate(c)

    def test_unknown_state_references_rejected(self):
        c={"format":"edulogic-1","inputs":[],"outputs":["Q"],
           "state":[{"type":"DFF","q":"Q","d":"MISSING"}],"gates":[]}
        with self.assertRaises(ValueError): edulogic.validate(c)

    def test_register_width_mismatch_rejected(self):
        c={"format":"edulogic-1","inputs":["D"],"outputs":["Q[0]","Q[1]"],
           "state":[{"type":"REGISTER","q":"Q","width":2,"d":["D"]}],"gates":[]}
        with self.assertRaises(ValueError): edulogic.validate(c)

    def test_unknown_gate_input_rejected(self):
        c={"format":"edulogic-1","inputs":["A"],"outputs":["F"],
           "gates":[{"type":"AND","inputs":["A","MISSING"],"output":"F"}]}
        with self.assertRaises(ValueError): edulogic.validate(c)

    def test_truth_table_rejects_stateful_circuit(self):
        with self.assertRaises(ValueError):
            edulogic.truth_table(self.load_example("counter2.json"))

    def test_vector_format_and_target_are_validated(self):
        c=self.load_example("half-adder.json")
        with self.assertRaises(ValueError):
            edulogic.run_vectors(c, {"format":"wrong","vectors":[]})
        with self.assertRaises(ValueError):
            edulogic.run_vectors(c, {"format":"edulogic-vectors-1","circuit":"other","vectors":[]})

    def test_sequence_format_and_target_are_validated(self):
        c=self.load_example("counter4-control.json")
        with self.assertRaises(ValueError):
            edulogic.run_sequence(c, {"format":"wrong","steps":[]})
        with self.assertRaises(ValueError):
            edulogic.run_sequence(c, {"format":"edulogic-sequence-1","circuit":"other","steps":[]})

    def test_sequence_generates_rtl_oracle(self):
        c=self.load_example("counter4-control.json")
        suite=json.loads((ROOT / "examples" / "counter4-control.sequence.json").read_text())
        tb=edulogic.export_sequence_testbench(c,suite)
        self.assertIn("module counter4_control_sequence_tb;",tb)
        self.assertIn("counter4_control dut(clk, ENABLE, RESET, Q_3, Q_2, Q_1, Q_0);",tb)
        self.assertIn("PASS generated sequence",tb)
        self.assertIn("FAIL step 5 Q_0",tb)

    def test_verilog_half_adder_golden(self):
        c = self.load_example("half-adder.json")
        golden = (ROOT / "examples" / "half-adder.v").read_text()
        self.assertEqual(edulogic.export_verilog(c), golden)

    def test_verilog_counter_has_clocked_state(self):
        c = self.load_example("counter4-control.json")
        v = edulogic.export_verilog(c)
        self.assertIn("input clk;", v)
        self.assertIn("always @(posedge clk)", v)
        self.assertIn("if (RESET)", v)
        self.assertIn("if (ENABLE)", v)
        self.assertIn("<= 1'b0;", v)
        self.assertIn("output reg Q_3;", v)
        self.assertIn("output reg Q_0;", v)
        self.assertIn("{Q_3, Q_2, Q_1, Q_0} <= {Q_3, Q_2, Q_1, Q_0} + 4'd1;", v)

    def test_cycle_is_rejected(self):
        c={"format":"edulogic-1","inputs":["A"],"outputs":["F"],"gates":[
          {"type":"AND","inputs":["A","F"],"output":"F"}]}
        with self.assertRaises(ValueError):
            edulogic.evaluate(c,{"A":1})

if __name__ == "__main__":
    unittest.main()
