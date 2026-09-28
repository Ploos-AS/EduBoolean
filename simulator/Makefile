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

hdl-conformance:
	$(PYTHON) -m unittest -v test_edulogic.py
