`timescale 1ns / 1ps

module CPU_TB;
bit clk;
bit rd_wr;
logic [1:0] proc_ID;
always #5 clk = ~clk;

CPU dut( .clk(clk), .proc_ID(proc_ID), .rd_wr(rd_wr));

initial begin
#20
proc_ID=1;
rd_wr=1;
$display("proc 0 is in state: %d", dut.cache0.cachedState);
$display("proc 1 is in state: %d", dut.cache1.cachedState);
$display("proc 2 is in state: %d", dut.cache2.cachedState);
$display("proc 3 is in state: %d", dut.cache3.cachedState);
#20

end

endmodule
