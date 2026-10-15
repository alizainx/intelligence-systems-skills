// SystemVerilog Synthesizable 2-Flip-Flop Clock-Domain Crossing (CDC) Synchronizer & Counter
module cdc_sync_and_counter (
    input  logic       clk,
    input  logic       rst_n,
    input  logic       async_in,
    output logic       sync_out,
    output logic [7:0] count_q
);
    logic meta_q;
    always_ff @(posedge clk or negedge rst_n) begin
        if (!rst_n) begin
            meta_q   <= 1'b0;
            sync_out <= 1'b0;
            count_q  <= 8'd0;
        end else begin
            meta_q   <= async_in;  // Non-blocking (<=) mandatory in sequential always_ff!
            sync_out <= meta_q;
            count_q  <= count_q + 8'd1;
        end
    end
endmodule
