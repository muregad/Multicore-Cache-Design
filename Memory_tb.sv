

module Memory_tb ();

	reg rd_en, wr_en;
  	reg [31:0] address, rd_value;
  	bit [31:0] wr_value;

	Memory m(.rd_en(rd_en), .wr_en(wr_en), .address(address), .wr_value(wr_value), .rd_value(rd_value));

	initial begin
		
		rd_en = 1'b0;
		wr_en = 1'b0;
		address = 32'h00000000;
		wr_value = 32'h00000000;
      
		$display("rd_en=%0b wr_en=%0b address=0x%0h wr_value=0x%0h rd_value=0x%0h ", rd_en, wr_en, address, wr_value, rd_value);

		#5;

		rd_en = 1'b1;
		address = 32'h00000001;
      $display("0x%0h", m.rd_value);
		$display("rd_en=%0b wr_en=%0b address=0x%0h wr_value=0x%0h rd_value=0x%0h ", rd_en, wr_en, address, wr_value, rd_value);

		#5;

		rd_en = 1'b0;
		wr_en = 1'b1;
		address = 32'h00000001;
		wr_value = 32'h000000FF;
		$display("rd_en=%0b wr_en=%0b address=0x%0h wr_value=0x%0h rd_value=0x%0h ", rd_en, wr_en, address, wr_value, rd_value);

		#5;
		
		rd_en = 1'b1;
		wr_en = 1'b0;
		address = 32'h00000001;
		$display("rd_en=%0b wr_en=%0b address=0x%0h wr_value=0x%0h rd_value=0x%0h ", rd_en, wr_en, address, wr_value, rd_value);

		#5;

		$finish;
		




	end


endmodule : Memory_tb
