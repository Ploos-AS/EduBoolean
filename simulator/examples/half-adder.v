module half_adder(A, B, SUM, CARRY);
  input A;
  input B;
  output SUM;
  output CARRY;
  assign SUM = A ^ B;
  assign CARRY = A & B;
endmodule
