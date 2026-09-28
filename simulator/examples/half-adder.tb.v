module half_adder_tb;
  reg A, B;
  wire SUM, CARRY;
  integer errors = 0;
  half_adder dut(A, B, SUM, CARRY);
  task check;
    input a, b, sum, carry;
    begin
      A=a; B=b; #1;
      if (SUM !== sum || CARRY !== carry) begin
        $display("FAIL A=%b B=%b SUM=%b CARRY=%b", A,B,SUM,CARRY);
        errors=errors+1;
      end
    end
  endtask
  initial begin
    check(0,0,0,0); check(0,1,1,0); check(1,0,1,0); check(1,1,0,1);
    if (errors == 0) $display("PASS half-adder");
    else $fatal(1, "%0d failures", errors);
    $finish;
  end
endmodule
