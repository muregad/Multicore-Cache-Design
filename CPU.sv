module CPU (input bit clk, input bit [1:0] proc_ID, input bit rd_wr, input bit[31:0] address);

	logic RdMs0, RdMs1, RdMs2, RdMs3;
	logic shared0, shared1, shared2, shared3;
	logic WrMs0, WrMs1, WrMs2, WrMs3;
	logic [31:0] addressOut[3:0];  
	logic WrBk0, WrBk1, WrBk2, WrBk3;
	logic [1:0] proc_IDOut0, proc_IDOut1, proc_IDOut2, proc_IDOut3;
	logic [31:0] outValue[3:0]; 
	logic [31:0] inValue;
	logic [31:0] address;
	logic readyToRead;
	logic [1:0] proc_ID_out_bus;
	logic sharedOutBus;
	logic rd_wr_redundant;
	logic [31:0] address_redundant;
	logic valueBus;
	Bus bus(.clk(clk),
			.proc_ID(proc_ID),
			.address(addressOut[proc_ID]),
			.value(valueBus),
			.RdMs(RdMs0 || RdMs1 || RdMs2 || RdMs3),
			.WrMs(WrMs0 || WrMs1 || WrMs2 || WrMs3),
			.WrBk(WrBk0 || WrBk1 || WrBk2 || WrBk3),
			.shared(shared0 || shared1 || shared2 || shared3),
			.proc_ID_out(proc_ID_out_bus),
			.address_out(address_redundant), // redundant
			.value_out(inValue),
			.readyToRead(readyToRead),
			.rd_wr(rd_wr_redundant), // redundant
			.shared_out(sharedOutBus));

	Cache cache0(.clk(clk),
				 .address(address),
				 .inValue(inValue),
				 .readyToRead(readyToRead),
				 .RdWr(rd_wr),
				 .proc_ID(proc_ID_out_bus),
				 .currProc_ID(0),
				 .shared(sharedOutBus),
				 .addressOut(addressOut[0]),
				 .outValue(outValue[0]),
				 .RdMs(RdMs0),
				 .WrMs(WrMs0),
				 .WrBk(WrBk0),
				 .proc_IDOut(proc_IDOut0),
				 .sharedOut(shared0));
	
	Cache cache1(.clk(clk),
			 .address(address),
			 .inValue(inValue),
			 .readyToRead(readyToRead),
			 .RdWr(rd_wr),
			 .proc_ID(proc_ID_out_bus),
			 .currProc_ID(1),
			 .shared(sharedOutBus),
			 .addressOut(addressOut[1]),
			 .outValue(outValue[1]),
			 .RdMs(RdMs1),
			 .WrMs(WrMs1),
			 .WrBk(WrBk1),
			 .proc_IDOut(proc_IDOut1),
			 .sharedOut(shared1));

	Cache cache2(.clk(clk),
			 .address(address),
			 .inValue(inValue),
			 .readyToRead(readyToRead),
			 .RdWr(rd_wr),
			 .proc_ID(proc_ID_out_bus),
			 .currProc_ID(2),
			 .shared(sharedOutBus),
			 .addressOut(addressOut[2]),
			 .outValue(outValue[2]),
			 .RdMs(RdMs2),
			 .WrMs(WrMs2),
			 .WrBk(WrBk2),
			 .proc_IDOut(proc_IDOut2),
			 .sharedOut(shared2));

	Cache cache3(.clk(clk),
			 .address(address),
			 .inValue(inValue),
			 .readyToRead(readyToRead),
			 .RdWr(rd_wr),
			 .proc_ID(proc_ID_out_bus),
			 .currProc_ID(3),
			 .shared(sharedOutBus),
			 .addressOut(addressOut[3]),
			 .outValue(outValue[3]),
			 .RdMs(RdMs3),
			 .WrMs(WrMs3),
			 .WrBk(WrBk3),
			 .proc_IDOut(proc_IDOut3), // Redundant
			 .sharedOut(shared3));	

	always @ * begin
		
		if(WrBk0) begin
			valueBus = outValue[0];
		end
		else if(WrBk1) begin
			valueBus = outValue[1];
		end
		else if(WrBk2) begin
			valueBus = outValue[2];
		end
		else if(WrBk3) begin
			valueBus = outValue[3];
		end

	end


endmodule : CPU