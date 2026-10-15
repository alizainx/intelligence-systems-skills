`default_nettype none
module sync_fifo_sva #(
    parameter int unsigned DEPTH = 4,
    parameter int unsigned DATA_W = 16
) (
    input  logic              clk,
    input  logic              rst_n,
    input  logic              push,
    input  logic [DATA_W-1:0] din,
    input  logic              pop,
    output logic [DATA_W-1:0] dout,
    output logic              full,
    output logic              empty
);
    logic [$clog2(DEPTH):0] count;
    assign full  = (count == DEPTH[$bits(count)-1:0]);
    assign empty = (count == '0);

    always_ff @(posedge clk or negedge rst_n) begin
        if (!rst_n) begin
            count <= '0;
            dout  <= '0;
        end else begin
            unique case ({push && !full, pop && !empty})
                2'b10: count <= count + 1'b1;
                2'b01: count <= count - 1'b1;
                default: count <= count;
            endcase
            if (push && !full) dout <= din;
        end
    end

    // Formal SVA invariant: count never exceeds DEPTH
    ap_no_overflow: assert property (@(posedge clk) disable iff (!rst_n) count <= DEPTH);
endmodule
`default_nettype wire
