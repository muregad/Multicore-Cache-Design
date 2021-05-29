class Instruction;
  rand bit [1:0] proc_ID;
  rand bit rd_wr;
  bit [31:0] address;
  rand bit [2:0]prob;
endclass

module TestBench #(parameter RANDOM=0);
    bit clk;
    Instruction instr;
    always #5 clk = ~clk;
    //CPU dut( .clk(clk), .proc_ID(instr.proc_ID), .rd_wr(instr.rd_wr),.address(instr.address));
    bit rd_wr;
    bit [1:0] proc_ID;
    bit [31:0]address;    
    bit[7:0] full_state;
    bit[7:0] currState;
    bit[7:0] nextState;
    bit reset;
    int fd;
    int fd2;
    string line;
    bit ran;
    // bit [31:0]inValue;
    // always #5 clk = ~clk;

    CPU dut( .clk(clk), .reset(reset), .proc_ID(proc_ID), .rd_wr(rd_wr),.address(address), .full_state(full_state));

    initial begin
       // Instruction instr;
       ran=RANDOM;
       while(1) begin
            $display("Random is : %d",RANDOM);
            if (ran) begin
                    $display("In Random");
                    fd = $fopen("set.csv", "w");
                    fd2 = $fopen("newstate.csv", "w");
                    instr = new();
                    proc_ID = instr.proc_ID;
                    rd_wr = instr.rd_wr;
                    address = 0;
                    repeat(1500) begin
                        instr.randomize();
                        if (instr.prob == 7)begin
                            reset = 1;
                        end
                        else
                            reset = 0;
                        currState = full_state;
                        proc_ID = instr.proc_ID;
                        rd_wr = instr.rd_wr;
                        #10
                        $display("\tProcessor ID = %0d \t Read/Write = %0d \t Address = %0d",instr.proc_ID,instr.rd_wr,address);
                        disp();
                        #20
                        nextState = full_state;
                        write_instr(currState,proc_ID,rd_wr,nextState);
                        // ;
                    end
                    $fclose(fd);
                    $fclose(fd2);
                    $display("This was random");
                    $stop;
            end
            else begin
                    $display("Reading From File");
                    fd = $fopen("set.csv", "r");
                    address = 0;
                    reset = 0;
                    while(!$feof(fd)) begin
                        $fscanf(fd,"%d,%d,%d,%d,%d,%d \n",currState[1:0],currState[3:2],currState[5:4],currState[7:6],proc_ID,rd_wr);
                        #10
                        $display("\tProcessor ID = %0d \t Read/Write = %0d \t Address = %0d",proc_ID,rd_wr,address);
                        disp();
                        #20
                        // nextState = full_state;
                        // write_instr(currState,proc_ID,rd_wr,nextState);
                        ;
                    end
                    $fclose(fd);
                    $display("this was directed");
                    $stop;
            end
        end
    end

    function void write_instr(input bit [7:0]currState,input bit [1:0]proc_ID,input bit rd_wr, input bit [7:0]state);
	    $fwrite(fd,"%d,%d,%d,%d,%d,%d \n",currState[1:0],currState[3:2],currState[5:4],currState[7:6],proc_ID,rd_wr);
        $fwrite(fd2,"%d,%d,%d,%d\n",state[1:0],state[3:2],state[5:4],state[7:6]);
    endfunction

    function void disp();
        $display("----------------------------------------------");
        $display("operation rd_wr: %d for proc: %d",rd_wr,proc_ID);
        $display("proc 0 is in state: %d", dut.cache0.cachedState);
        $display("proc 1 is in state: %d", dut.cache1.cachedState);
        $display("proc 2 is in state: %d", dut.cache2.cachedState);
        $display("proc 3 is in state: %d", dut.cache3.cachedState);
        $display("----------------------------------------------");
    endfunction
endmodule