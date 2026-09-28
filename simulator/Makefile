PYTHON ?= python3

.PHONY: test hdl-generate hdl-test hdl-conformance

test:
	$(PYTHON) -m unittest -v test_edulogic.py

hdl-generate:
	$(PYTHON) edulogic.py examples/half-adder.json --verilog > build-half-adder.v
	diff -u examples/half-adder.v build-half-adder.v

hdl-test: hdl-generate
	iverilog -g2012 -s half_adder_tb -o /tmp/half-adder.vvp build-half-adder.v examples/half-adder.tb.v
	vvp /tmp/half-adder.vvp
	$(PYTHON) edulogic.py examples/counter4-control.json --verilog > build-counter4-control.v
	iverilog -g2012 -s counter4_control_tb -o /tmp/counter4-control.vvp build-counter4-control.v examples/counter4-control.tb.v
	vvp /tmp/counter4-control.vvp

hdl-conformance:
	$(PYTHON) edulogic.py examples/half-adder.json --vectors examples/half-adder.vectors.json
	$(PYTHON) edulogic.py examples/counter4-control.json --sequence examples/counter4-control.sequence.json
