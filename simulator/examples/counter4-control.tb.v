module counter4_control_tb;
  reg clk=0, ENABLE=0, RESET=1;
  wire Q_3, Q_2, Q_1, Q_0;
  integer errors=0;
  counter4_control dut(clk, ENABLE, RESET, Q_3, Q_2, Q_1, Q_0);

  task pulse; begin #1 clk=1; #1 clk=0; end endtask
  task check;
    input [3:0] expected;
    begin
      if ({Q_3,Q_2,Q_1,Q_0} !== expected) begin
        $display("FAIL got=%b%b%b%b expected=%b",Q_3,Q_2,Q_1,Q_0,expected);
        errors=errors+1;
      end
    end
  endtask

  initial begin
    pulse; check(4'b0000);
    RESET=0; ENABLE=1; pulse; check(4'b0001);
    pulse; check(4'b0010);
    ENABLE=0; pulse; check(4'b0010);
    ENABLE=1; pulse; check(4'b0011);
    RESET=1; pulse; check(4'b0000);
    if(errors) $fatal(1,"%0d failures",errors);
    $display("PASS counter4-control");
    $finish;
  end
endmodule
