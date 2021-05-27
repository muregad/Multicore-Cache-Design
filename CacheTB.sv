module tb;
bit clk;
reg [31:0]address;
reg [31:0]inValue;
bit readyToRead; 
bit RdWr;
reg [1:0]proc_ID;
bit shared;
reg [1:0]currProc_ID;
reg [31:0]addressOut;
reg [31:0]outValue;
bit RdMs;
bit WrMs;
bit WrBk;
reg [1:0]proc_IDOut;
bit sharedOut;
always #5 clk = ~clk;

Cache dut(.clk(clk),.address(address),.inValue(inValue),.readyToRead(readyToRead),.RdWr(RdWr),.proc_ID(proc_ID),.shared(shared),.currProc_ID(currProc_ID),
.addressOut(addressOut),.outValue(outValue),.RdMs(RdMs),.WrMs(WrMs),.WrBk(WrBk),.proc_IDOut(proc_IDOut),.sharedOut(sharedOut));

initial
begin 
address = 4;
inValue =5;
currProc_ID=2;
#5
readyToRead=0;
$display("proc 2 is in state: %d", dut.cachedState);
end 




endmodule