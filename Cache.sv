`define size 1024
`define associativity 4

module Cache( input bit clk, input bit reset,  input bit [31:0]address, input bit [31:0]inValue,input bit readyToRead, input bit RdWr, input bit [1:0]proc_ID , input bit shared, input bit[1:0] currProc_ID, 
		output bit [31:0]addressOut, output bit [31:0]outValue, output bit RdMs, output bit WrMs, output bit WrBk, output bit [1:0]proc_IDOut, output bit sharedOut);

reg [31:0] CachedData [(`size /4)-1 :0][(`associativity)-1:0]; // needs changing to address block
reg [29:0] blockTag [(`size /4)-1 :0][(`associativity)-1:0]; //needs changing to address tag
reg [1:0] cachedStates [(`size /4)-1 :0][(`associativity)-1:0];
reg [1:0] LRU [(`size /4)-1 :0];
reg [1:0] cachedState;
reg [23:0]tag;
reg [7:0]index;
reg [1:0]BLK;
reg existing;
reg currLRU; 

initial begin 
for (int i=0; i<(`size/4); i++)begin
 for (int j=0;j<(`associativity);j++)begin
	CachedData[i][j] = '0;
	cachedStates[i][j]= '0;
 end
  LRU[i]='0;
end
cachedState =0;
end 

always @ *
begin
		if (!reset) begin
		tag = address[31:8];
		index = address [7:0]; 
		//$display(index);
		//$display(tag);
		RdMs = 0;
		WrMs = 0;
		existing = 0;
		currLRU = LRU[index];
		WrBk=0;
		//$display("LRU: %d", currLRU);

		if (blockTag[index][0] == tag) begin
			BLK = 0;
			existing = 1;
		end
		else if (blockTag[index][1] == tag) begin
			BLK = 1;
			existing = 1; 
		end
		else if (blockTag[index][2] == tag) begin
			BLK = 2;
			existing = 1;  
		end
		else if (blockTag[index][3] == tag) begin
			BLK = 3;
			existing = 1; 
		end
		//$display("Existing: %d",existing);
		if (proc_ID==currProc_ID) begin
		if (RdWr & existing) begin // read operation
			outValue = CachedData[index][BLK];
			RdMs = 0;
		end
		else if (!RdWr & existing) begin
			CachedData[index][BLK] = inValue;
			WrMs = 0;
		end
		if (RdWr & !existing) begin // read operation
			RdMs = 1;
		end
		else if (!RdWr & !existing) begin // Write operation
			WrMs = 1;
		end
		if (!existing) begin
			cachedState = cachedStates [index][currLRU];
		//	$display("Cached state inside if: %d",cachedState);
		//	$display("Cached state inside from array if: %d",cachedStates [index][currLRU]);
			if (cachedState == 2'b11) begin
				outValue = CachedData[index][currLRU];
				WrBk = 1;
			end
			if (RdWr & readyToRead) begin
				CachedData[index][currLRU] = inValue;
				blockTag[index][currLRU] = tag;
				existing = 1;
				BLK = currLRU; 
				RdMs=0; 
				case(currLRU)
					2'b00:begin
						currLRU = 2'b01;
					end
					2'b01:begin
						currLRU = 2'b10;
					end
					2'b10:begin
						currLRU = 2'b11;
					end
					2'b11:begin
						currLRU = 2'b00;
					end
				endcase
			end
			else if ((!RdWr)) begin
				CachedData[index][currLRU] = inValue;
				blockTag[index][currLRU] = tag;
				existing = 1;
				BLK = currLRU;
				WrMs=0; 
				case(currLRU)
					2'b00:begin
						currLRU = 2'b01;
					end
					2'b01:begin
						currLRU = 2'b10;
					end
					2'b10:begin
						currLRU = 2'b11;
					end
					2'b11:begin
						currLRU = 2'b00;
					end
				endcase
			end
			LRU[index] = currLRU;
		end
		//if (RdWr) begin // read operation
		//   if (blockTag[index][0] == tag) begin
		//	outValue = CachedData[index][0];
		//	RdMs = 0;
		//	BLK = 0;
		//end
		//   else if (blockTag[index][1] == tag) begin
		//	outValue = CachedData[index][1]; 
		//	RdMs=0;
		//	BLK = 1; 
		//end
		//   else if (blockTag[index][2] == tag) begin
		//	outValue = CachedData[index][2];
		//	RdMs=0;
		//	BLK = 2;  
		//end
		//   else if (blockTag[index][3] == tag) begin
		//	outValue = CachedData[index][3];
		//	RdMs=0;
		//	BLK = 3; 
		//end
		//end
		//else begin // write operation
		//   if (blockTag[index][0] == tag) begin
		//	CachedData[index][0] = inValue;
		//	WrMs=0;
		//	BLK = 0;  
		//end
		//   else if (blockTag[index][1] == tag) begin
		//	CachedData[index][1] = inValue;
		//	WrMs=0;
		//	BLK = 1;   
		//end
		//   else if (blockTag[index][2] == tag) begin
		//	CachedData[index][2] = inValue;
		//	WrMs=0; 
		//	BLK = 2;  
		//end
		//   else if (blockTag[index][3] == tag) begin
		//	CachedData[index][3] = inValue;
		//	WrMs=0;
		//	BLK = 3;    
		//end
		//end
		end
		if (existing) begin
			cachedState = cachedStates [index][BLK];
			if ((cachedState == 2'b01) | (cachedState == 2'b10) | (cachedState == 2'b11)) begin
				sharedOut = 1;
			end
			else 
					sharedOut = 0;
		end
		if (proc_ID == currProc_ID) begin
			proc_IDOut = currProc_ID;
		end
		else begin 
			WrMs = 0;
			RdMs = 0; // to ensure it doesnt cause any problems
		end
	end
	else begin
		for (int i=0; i<(`size/4); i++)begin
 			for (int j=0;j<(`associativity);j++)begin
				CachedData[i][j] = '0;
				cachedStates[i][j]= '0;
				blockTag[i][j]='x;

			end
		end
	
	end
end

always @ (posedge clk)
begin 
//$display("The current nnstate is: %d", cachedState);
//$display(cachedStates[0][0]);
//$display("readms = %d",RdMs);
//$display("shared = %d",shared);
//$display("writems = %d",WrMs);
//$display("RdWr= %d", RdWr);
//$display("shared of this block = %d",sharedOut);
//if (existing)
//$display("data = %d",CachedData[index][BLK]);
//else
//$display("data = %d",CachedData[index][currLRU]);

if(!reset) begin
	case(cachedState)
	2'b00: // INVALID
		begin
		if (shared & RdWr& (proc_ID == currProc_ID)) begin 
			cachedState = 2'b01; // Shared
		end
		else if (!shared & RdWr & (proc_ID == currProc_ID)) begin
			cachedState = 2'b10;  // EXCLUSIVE
		end
		if ((!RdWr) & (proc_ID == currProc_ID)) begin 
			cachedState = 2'b11;  // MODIFIED
		end
		end
	2'b01: // SHARED
		begin
		if (!RdWr & (proc_ID == currProc_ID)) begin 
			cachedState = 2'b11;  // MODIFIED
		end
		else if (!RdWr & (proc_ID != currProc_ID)) begin
			cachedState = 2'b00; // INVALID
		end
		end
	2'b10: // EXCLUSIVE
		begin
		if (RdWr & (proc_ID != currProc_ID)) begin
			cachedState = 2'b01; // SHARED
		end
		if (!RdWr & (proc_ID == currProc_ID)) begin
			cachedState = 2'b11; // MODIFIED
		end
		else if (!RdWr & (proc_ID != currProc_ID)) begin 
			cachedState = 2'b00; // INVALID
		end
		end
	2'b11: // MODIFIED
		begin
		if (!RdWr & (proc_ID != currProc_ID)) begin
			cachedState = 2'b00; // INVALID
			outValue = CachedData[index][BLK];
			WrBk = 1;
		end
		if (RdWr & (proc_ID != currProc_ID)) begin
			cachedState = 2'b01; // SHARED
			outValue = CachedData[index][BLK];
			WrBk = 1;
		end
		end
	endcase
	if(existing)
	cachedStates [index][BLK] = cachedState;
	else
	cachedStates [index][currLRU] = cachedState;
	end
end


endmodule  