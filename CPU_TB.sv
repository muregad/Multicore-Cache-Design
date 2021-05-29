`timescale 1ns / 1ps
class p;
bit rd_wr;
bit [1:0] proc_ID;
endclass
module CPU_TB;
bit clk;
bit rd_wr;
bit [1:0] proc_ID;
bit [31:0]address;
bit [31:0]inValue;
bit[7:0] full_state;
always #5 clk = ~clk;

CPU dut( .clk(clk), .proc_ID(proc_ID), .rd_wr(rd_wr),.address(address), .full_state(full_state));


initial 
begin
proc_ID=1;
rd_wr=1;
dut.inValue=32'h3;
#10
$display("----------------------------------------------");
$display("operation rd_wr: %d for proc: %d",rd_wr,proc_ID);
$display("proc 0 is in state: %d", dut.cache0.cachedState);
$display("proc 1 is in state: %d", dut.cache1.cachedState);
$display("proc 2 is in state: %d", dut.cache2.cachedState);
$display("proc 3 is in state: %d", dut.cache3.cachedState);
$display("----------------------------------------------");
#20
proc_ID=2;
rd_wr=1;
#10
$display("----------------------------------------------");
$display("operation rd_wr: %d for proc: %d",rd_wr,proc_ID);
$display("proc 0 is in state: %d", dut.cache0.cachedState);
$display("proc 1 is in state: %d", dut.cache1.cachedState);
$display("proc 2 is in state: %d", dut.cache2.cachedState);
$display("proc 3 is in state: %d", dut.cache3.cachedState);
$display("----------------------------------------------");
#20
proc_ID=3;
rd_wr=0;
#10
$display("----------------------------------------------");
$display("operation rd_wr: %d for proc: %d",rd_wr,proc_ID);
$display("proc 0 is in state: %d", dut.cache0.cachedState);
$display("proc 1 is in state: %d", dut.cache1.cachedState);
$display("proc 2 is in state: %d", dut.cache2.cachedState);
$display("proc 3 is in state: %d", dut.cache3.cachedState);
$display("----------------------------------------------");
#20
proc_ID=2;
rd_wr=1;
#10
$display("----------------------------------------------");
$display("operation rd_wr: %d for proc: %d",rd_wr,proc_ID);
$display("proc 0 is in state: %d", dut.cache0.cachedState);
$display("proc 1 is in state: %d", dut.cache1.cachedState);
$display("proc 2 is in state: %d", dut.cache2.cachedState);
$display("proc 3 is in state: %d", dut.cache3.cachedState);
$display("----------------------------------------------");
#20
proc_ID=1;
rd_wr=0;
#10
$display("----------------------------------------------");
$display("operation rd_wr: %d for proc: %d",rd_wr,proc_ID);
$display("proc 0 is in state: %d", dut.cache0.cachedState);
$display("proc 1 is in state: %d", dut.cache1.cachedState);
$display("proc 2 is in state: %d", dut.cache2.cachedState);
$display("proc 3 is in state: %d", dut.cache3.cachedState);
$display("----------------------------------------------");
#20
proc_ID=1;
rd_wr=1;
#10
$display("----------------------------------------------");
$display("operation rd_wr: %d for proc: %d",rd_wr,proc_ID);
$display("proc 0 is in state: %d", dut.cache0.cachedState);
$display("proc 1 is in state: %d", dut.cache1.cachedState);
$display("proc 2 is in state: %d", dut.cache2.cachedState);
$display("proc 3 is in state: %d", dut.cache3.cachedState);
$display("----------------------------------------------");
#20
proc_ID=2;
rd_wr=1;
#10
$display("----------------------------------------------");
$display("operation rd_wr: %d for proc: %d",rd_wr,proc_ID);
$display("proc 0 is in state: %d", dut.cache0.cachedState);
$display("proc 1 is in state: %d", dut.cache1.cachedState);
$display("proc 2 is in state: %d", dut.cache2.cachedState);
$display("proc 3 is in state: %d", dut.cache3.cachedState);
$display("----------------------------------------------");
#20
proc_ID=3;
rd_wr=1;
#10
$display("----------------------------------------------");
$display("operation rd_wr: %d for proc: %d",rd_wr,proc_ID);
$display("proc 0 is in state: %d", dut.cache0.cachedState);
$display("proc 1 is in state: %d", dut.cache1.cachedState);
$display("proc 2 is in state: %d", dut.cache2.cachedState);
$display("proc 3 is in state: %d", dut.cache3.cachedState);
$display("----------------------------------------------");

end

endmodule

