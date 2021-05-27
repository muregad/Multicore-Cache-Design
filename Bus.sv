
module Bus (
	input bit clk,    
	input bit [1:0] proc_ID,
	input bit [31:0] address,
	input bit [31:0] value,
	input bit RdMs,
	input bit WrMs,
	input bit WrBk,
	input bit shared,
	output bit [1:0] proc_ID_out,
	output bit [31:0] address_out,
	output bit [31:0] value_out,
	output bit readyToRead,
	output bit rd_wr,
	output bit shared_out);
	
	Memory mem(.rd_en(RdMs), .wr_en(WrBk), .address(address), .wr_value(value), .rd_value(value_out));

	always @ * begin
		
		proc_ID_out = proc_ID;
		address_out = address;
		shared_out = shared;

		if(RdMs) begin
			rd_wr = 1'b1;
			readyToRead = 1'b1;
		end

		if(WrMs) begin
			rd_wr = 1'b0;
		end


	end


	



endmodule : Bus