
module Memory 
 (
	input bit rd_en,
	input bit wr_en,
	input bit [31:0] address,
	input bit [31:0] wr_value,
	output bit [31:0] rd_value);

 reg [31:0] data_mem[2^32:0];

 initial begin
 	
 	for(int i = 0; i < $size(data_mem); i++) begin
      data_mem[i] = 32'h00000000; // To-Be-Changed
 	end

 end

always @ *
begin
	
	if (rd_en) begin
		rd_value = data_mem[address];
      $display("Reading ===> Read Value = 0x%0h", rd_value);
	end

	if (wr_en) begin
		data_mem[address] = wr_value;
      $display("Writing ===> Written Value = 0x%0h", data_mem[address]);
	end

end


endmodule 

